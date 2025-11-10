#!/usr/bin/env python3
"""Test config.yaml syntax and values"""
import yaml

try:
    print("🔍 Testing config.yaml...")
    with open('config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    print("✅ YAML syntax is valid!")
    
    scanner = config.get('market_scanner', {})
    print(f"\n📊 Market Scanner Config:")
    print(f"   - min_reward: {scanner.get('min_reward')}")
    print(f"   - max_competition_bars: {scanner.get('max_competition_bars')}")
    print(f"   - target_categories: {scanner.get('target_categories')}")
    print(f"   - interval: {scanner.get('interval')}")
    
    alerts = config.get('alerts', {})
    print(f"\n🔔 Alerts Config:")
    print(f"   - telegram_enabled: {alerts.get('telegram_enabled')}")
    print(f"   - alert_on_startup: {alerts.get('alert_on_startup')}")
    
except yaml.YAMLError as e:
    print(f"❌ YAML SYNTAX ERROR: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")

