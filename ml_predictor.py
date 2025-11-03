"""
ML Predictor Module
Machine learning for fill prediction and alerts
"""

import torch
import torch.nn as nn
import numpy as np
import pandas as pd
import logging
import json
import asyncio
import aiohttp
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta
import pickle
import os

logger = logging.getLogger(__name__)


class FillPredictor(nn.Module):
    """Neural network for fill probability prediction"""
    
    def __init__(self, input_size: int = 20):
        super(FillPredictor, self).__init__()
        
        self.fc1 = nn.Linear(input_size, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 16)
        self.fc4 = nn.Linear(16, 1)
        
        self.dropout = nn.Dropout(0.2)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.relu(self.fc2(x))
        x = self.dropout(x)
        x = self.relu(self.fc3(x))
        x = self.sigmoid(self.fc4(x))
        return x


class MLPredictor:
    """ML-based prediction and alerting system"""
    
    def __init__(self, config: dict):
        self.config = config
        self.model = FillPredictor()
        self.training_data = []
        self.model_path = 'models/fill_predictor.pt'
        self.alert_webhook = config.get('alert_webhook', '')
        self.telegram_bot_token = config.get('telegram_bot_token', '')
        self.telegram_chat_id = config.get('telegram_chat_id', '')
        self._load_model()
    
    def _load_model(self):
        """Load pre-trained model if exists"""
        try:
            if os.path.exists(self.model_path):
                self.model.load_state_dict(torch.load(self.model_path))
                self.model.eval()
                logger.info("Loaded pre-trained model")
            else:
                logger.info("No pre-trained model found, using new model")
        except Exception as e:
            logger.error(f"Error loading model: {e}")
    
    async def predict_fill(self, order: Dict) -> float:
        """Predict fill probability for an order"""
        try:
            # Extract features
            features = self._extract_features(order)
            
            # Convert to tensor
            input_tensor = torch.FloatTensor(features).unsqueeze(0)
            
            # Predict
            self.model.eval()
            with torch.no_grad():
                probability = self.model(input_tensor).item()
            
            # Log high-risk predictions
            if probability > self.config['fill_risk_threshold']:
                await self.send_alert(f"⚠️ High fill risk detected: {probability:.2%} for market {order.get('market_id', 'unknown')}")
            
            return probability
            
        except Exception as e:
            logger.error(f"Prediction error: {e}")
            return 0.5  # Default neutral probability
    
    def _extract_features(self, order: Dict) -> List[float]:
        """Extract features from order for ML model"""
        features = []
        
        try:
            # Market features
            features.append(order.get('spread', 0.01))
            features.append(order.get('yes_order', {}).get('price', 0.5))
            features.append(order.get('no_order', {}).get('price', 0.5))
            features.append(order.get('yes_order', {}).get('size', 250) / 1000)  # Normalize
            features.append(order.get('no_order', {}).get('size', 250) / 1000)
            
            # Market conditions
            market_data = order.get('market_data', {})
            features.append(market_data.get('volume', 0) / 100000)  # Normalize
            features.append(market_data.get('liquidity', 0) / 10000)
            features.append(market_data.get('bid_volume', 0) / 1000)
            features.append(market_data.get('ask_volume', 0) / 1000)
            features.append(market_data.get('current_spread', 0.02))
            
            # Competition and reward
            features.append(order.get('competition_bars', 2) / 5)  # Normalize to 0-1
            features.append(order.get('reward', 300) / 1000)  # Normalize
            
            # Time features
            hour = datetime.now().hour
            features.append(hour / 24)  # Time of day normalized
            features.append(1 if hour >= 9 and hour <= 17 else 0)  # Business hours
            
            # Category encoding (simplified)
            category = order.get('category', 'other')
            category_map = {'sports': 1, 'crypto': 0.8, 'politics': 0.6, 'other': 0.3}
            features.append(category_map.get(category, 0.3))
            
            # Historical performance (if available)
            features.append(order.get('historical_fill_rate', 0.5))
            features.append(order.get('market_age_hours', 24) / 168)  # Week normalized
            
            # Price efficiency
            yes_price = order.get('yes_order', {}).get('price', 0.5)
            no_price = order.get('no_order', {}).get('price', 0.5)
            efficiency = abs(1.0 - (yes_price + no_price))
            features.append(efficiency)
            
            # Volume spike indicator
            features.append(1 if order.get('volume_spike', False) else 0)
            
            # Padding to ensure correct input size
            while len(features) < 20:
                features.append(0)
            
            return features[:20]  # Ensure exactly 20 features
            
        except Exception as e:
            logger.error(f"Feature extraction error: {e}")
            return [0] * 20  # Return zeros on error
    
    async def train_model(self):
        """Train the ML model on historical data"""
        try:
            if len(self.training_data) < 100:
                logger.info(f"Insufficient training data: {len(self.training_data)} samples")
                return
            
            # Prepare training data
            X, y = self._prepare_training_data()
            
            if len(X) == 0:
                return
            
            # Convert to tensors
            X_tensor = torch.FloatTensor(X)
            y_tensor = torch.FloatTensor(y).unsqueeze(1)
            
            # Training setup
            criterion = nn.BCELoss()
            optimizer = torch.optim.Adam(self.model.parameters(), lr=0.001)
            
            # Training loop
            self.model.train()
            epochs = 50
            batch_size = 32
            
            for epoch in range(epochs):
                total_loss = 0
                
                # Mini-batch training
                for i in range(0, len(X_tensor), batch_size):
                    batch_X = X_tensor[i:i+batch_size]
                    batch_y = y_tensor[i:i+batch_size]
                    
                    optimizer.zero_grad()
                    outputs = self.model(batch_X)
                    loss = criterion(outputs, batch_y)
                    loss.backward()
                    optimizer.step()
                    
                    total_loss += loss.item()
                
                if epoch % 10 == 0:
                    avg_loss = total_loss / (len(X_tensor) / batch_size)
                    logger.info(f"Training epoch {epoch}, loss: {avg_loss:.4f}")
            
            # Save model
            self._save_model()
            
            # Calculate and log accuracy
            accuracy = self._calculate_accuracy(X_tensor, y_tensor)
            logger.info(f"Model training complete. Accuracy: {accuracy:.2%}")
            
            await self.send_alert(f"🤖 ML Model updated. Accuracy: {accuracy:.2%}")
            
        except Exception as e:
            logger.error(f"Training error: {e}")
    
    def _prepare_training_data(self) -> Tuple[List, List]:
        """Prepare training data from historical records"""
        X = []
        y = []
        
        for record in self.training_data:
            features = self._extract_features(record['order'])
            label = 1 if record['filled'] else 0
            
            X.append(features)
            y.append(label)
        
        return X, y
    
    def _calculate_accuracy(self, X: torch.Tensor, y: torch.Tensor) -> float:
        """Calculate model accuracy"""
        self.model.eval()
        with torch.no_grad():
            predictions = self.model(X)
            predicted = (predictions > 0.5).float()
            accuracy = (predicted == y).float().mean().item()
        
        return accuracy
    
    def _save_model(self):
        """Save trained model"""
        try:
            os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
            torch.save(self.model.state_dict(), self.model_path)
            logger.info(f"Model saved to {self.model_path}")
        except Exception as e:
            logger.error(f"Error saving model: {e}")
    
    def add_training_sample(self, order: Dict, filled: bool):
        """Add a sample to training data"""
        self.training_data.append({
            'order': order,
            'filled': filled,
            'timestamp': datetime.now()
        })
        
        # Keep only recent data (last 10000 samples)
        if len(self.training_data) > 10000:
            self.training_data = self.training_data[-10000:]
    
    async def send_alert(self, message: str):
        """Send alert via configured channels"""
        tasks = []
        
        if self.telegram_bot_token and self.telegram_chat_id:
            tasks.append(self._send_telegram_alert(message))
        
        if self.alert_webhook:
            tasks.append(self._send_webhook_alert(message))
        
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
        
        logger.info(f"Alert sent: {message}")
    
    async def _send_telegram_alert(self, message: str):
        """Send alert via Telegram"""
        try:
            url = f"https://api.telegram.org/bot{self.telegram_bot_token}/sendMessage"
            
            data = {
                'chat_id': self.telegram_chat_id,
                'text': message,
                'parse_mode': 'HTML'
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=data) as response:
                    if response.status != 200:
                        logger.error(f"Telegram alert failed: {await response.text()}")
                        
        except Exception as e:
            logger.error(f"Telegram alert error: {e}")
    
    async def _send_webhook_alert(self, message: str):
        """Send alert via webhook (Discord/Slack)"""
        try:
            # Skip if webhook URL is not configured or is placeholder
            if not self.alert_webhook or '...' in self.alert_webhook or 'hooks.slack.com/services/...' in self.alert_webhook:
                return

            data = {
                'content': message,  # Discord format
                'text': message,     # Slack format
                'username': 'Polymarket Bot'
            }

            async with aiohttp.ClientSession() as session:
                async with session.post(self.alert_webhook, json=data, timeout=5) as response:
                    if response.status not in [200, 204]:
                        error_text = await response.text()
                        # Only log error if it's not a configuration issue
                        if response.status != 405:  # 405 = Method Not Allowed (bad webhook URL)
                            logger.error(f"Webhook alert failed: {error_text}")

        except asyncio.TimeoutError:
            logger.debug(f"Webhook timeout (URL may be invalid)")
        except Exception as e:
            # Only log if it's not a connection error (which indicates bad URL)
            if 'Cannot connect' not in str(e):
                logger.debug(f"Webhook alert error: {e}")
    
    def get_model_stats(self) -> Dict:
        """Get model statistics"""
        return {
            'training_samples': len(self.training_data),
            'model_path': self.model_path,
            'model_exists': os.path.exists(self.model_path),
            'fill_risk_threshold': self.config['fill_risk_threshold'],
            'alerts_configured': bool(self.telegram_bot_token or self.alert_webhook)
        }
    
    async def analyze_market_patterns(self) -> Dict:
        """Analyze patterns in market data"""
        if not self.training_data:
            return {}
        
        # Convert to DataFrame for analysis
        df = pd.DataFrame([
            {
                'filled': d['filled'],
                'spread': d['order'].get('spread', 0),
                'category': d['order'].get('category', 'unknown'),
                'reward': d['order'].get('reward', 0),
                'hour': d['timestamp'].hour
            }
            for d in self.training_data
        ])
        
        patterns = {
            'fill_rate_by_category': df.groupby('category')['filled'].mean().to_dict(),
            'fill_rate_by_hour': df.groupby('hour')['filled'].mean().to_dict(),
            'optimal_spread': df[df['filled'] == 1]['spread'].mean() if len(df[df['filled'] == 1]) > 0 else 0.01,
            'avg_reward_filled': df[df['filled'] == 1]['reward'].mean() if len(df[df['filled'] == 1]) > 0 else 0
        }
        
        return patterns