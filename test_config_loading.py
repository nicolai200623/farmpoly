#!/usr/bin/env python3
"""
Test script to verify config loading
"""

import yaml
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_config_loading():
    """Test that config.yaml is loaded correctly"""
    
    print("=" * 80)
    print("Testing config.yaml loading...")
    print("=" * 80)
    
    try:
        with open('config.yaml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        print("\n✅ Config loaded successfully!")
        
        # Check market_scanner section
        scanner_config = config.get('market_scanner', {})
        
        print("\n📊 Market Scanner Config:")
        print(f"   - min_reward: {scanner_config.get('min_reward', 'NOT SET')}")
        print(f"   - max_competition_bars: {scanner_config.get('max_competition_bars', 'NOT SET')}")
        print(f"   - interval: {scanner_config.get('interval', 'NOT SET')}s")
        print(f"   - min_shares: {scanner_config.get('min_shares', 'NOT SET')}")
        
        # Verify expected values
        expected_min_reward = 100
        actual_min_reward = scanner_config.get('min_reward')
        
        if actual_min_reward == expected_min_reward:
            print(f"\n✅ min_reward is correct: {actual_min_reward}")
        else:
            print(f"\n❌ ERROR: min_reward is {actual_min_reward}, expected {expected_min_reward}")
            return False
        
        # Test MarketScannerV2 initialization
        print("\n" + "=" * 80)
        print("Testing MarketScannerV2 initialization...")
        print("=" * 80)
        
        from market_scanner_v2 import MarketScannerV2
        
        # Test with direct config (how main.py passes it)
        scanner = MarketScannerV2(scanner_config)
        
        print(f"\n✅ MarketScannerV2 initialized")
        print(f"   - scanner.min_reward: {scanner.min_reward}")
        print(f"   - scanner.max_competition: {scanner.max_competition}")
        
        if scanner.min_reward == expected_min_reward:
            print(f"\n✅ Scanner is using correct min_reward: {scanner.min_reward}")
        else:
            print(f"\n❌ ERROR: Scanner min_reward is {scanner.min_reward}, expected {expected_min_reward}")
            return False
        
        print("\n" + "=" * 80)
        print("✅ ALL TESTS PASSED!")
        print("=" * 80)
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    success = test_config_loading()
    exit(0 if success else 1)

