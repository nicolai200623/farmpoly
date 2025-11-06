"""
Test script to verify bug fixes for:
1. Invalid signature in profit_taking_manager.py
2. Pending orders always empty in main.py
"""

import sys
import os
import re

def test_profit_taking_fix():
    """Test that profit_taking_manager.py creates fresh signing client"""
    print("\n" + "="*80)
    print("TEST 1: Profit Taking - Fresh Signing Client")
    print("="*80)
    
    with open('profit_taking_manager.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check 1: Should create fresh signing client
    if 'signing_client = ClobClient(' in content:
        print("✅ PASS: Creates fresh signing client")
    else:
        print("❌ FAIL: Does not create fresh signing client")
        return False
    
    # Check 2: Should set API credentials on signing_client
    if 'signing_client.set_api_creds(signing_client.create_or_derive_api_creds())' in content:
        print("✅ PASS: Sets API credentials on signing_client")
    else:
        print("❌ FAIL: Does not set API credentials properly")
        return False
    
    # Check 3: Should use signing_client to create and post order
    if 'signed_order = signing_client.create_order(order_args)' in content:
        print("✅ PASS: Uses signing_client to create order")
    else:
        print("❌ FAIL: Does not use signing_client to create order")
        return False
    
    if 'resp = signing_client.post_order(signed_order' in content:
        print("✅ PASS: Uses signing_client to post order")
    else:
        print("❌ FAIL: Does not use signing_client to post order")
        return False
    
    # Check 4: Should NOT use self.client for signing/posting
    # Find the _close_position method
    close_position_start = content.find('async def _close_position(')
    if close_position_start == -1:
        print("❌ FAIL: Cannot find _close_position method")
        return False
    
    # Find the next method after _close_position
    next_method = content.find('\n    async def ', close_position_start + 1)
    if next_method == -1:
        next_method = content.find('\n    def ', close_position_start + 1)
    if next_method == -1:
        next_method = len(content)
    
    close_position_method = content[close_position_start:next_method]
    
    # Check that self.client is NOT used for create_order or post_order
    if 'self.client.create_order(' in close_position_method:
        print("❌ FAIL: Still uses self.client.create_order() - should use signing_client")
        return False
    else:
        print("✅ PASS: Does not use self.client.create_order()")
    
    if 'self.client.post_order(' in close_position_method:
        print("❌ FAIL: Still uses self.client.post_order() - should use signing_client")
        return False
    else:
        print("✅ PASS: Does not use self.client.post_order()")
    
    print("\n✅ TEST 1 PASSED: Profit taking fix verified!")
    return True


def test_pending_orders_fix():
    """Test that main.py checks if order is valid before adding to pending"""
    print("\n" + "="*80)
    print("TEST 2: Pending Orders - Check Before Add")
    print("="*80)
    
    with open('main.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the _process_market_opportunity method
    method_start = content.find('async def _process_market_opportunity(')
    if method_start == -1:
        print("❌ FAIL: Cannot find _process_market_opportunity method")
        return False
    
    # Find the next method
    next_method = content.find('\n    async def ', method_start + 1)
    if next_method == -1:
        next_method = len(content)
    
    method_content = content[method_start:next_method]
    
    # Check 1: Should have "if order:" check before add_pending_order
    if 'if order:' in method_content and 'add_pending_order(order)' in method_content:
        print("✅ PASS: Has 'if order:' check before add_pending_order")
    else:
        print("❌ FAIL: Missing 'if order:' check before add_pending_order")
        return False
    
    # Check 2: Should have success log inside if block
    if_block_pattern = r'if order:.*?add_pending_order\(order\).*?Added market.*to pending orders'
    if re.search(if_block_pattern, method_content, re.DOTALL):
        print("✅ PASS: Success log is inside 'if order:' block")
    else:
        print("❌ FAIL: Success log may not be inside 'if order:' block")
        return False
    
    # Check 3: Should have else block with warning
    if 'else:' in method_content and 'Skipped market' in method_content:
        print("✅ PASS: Has else block with skip warning")
    else:
        print("❌ FAIL: Missing else block with skip warning")
        return False
    
    # Check 4: Should NOT have unconditional add_pending_order
    # Look for add_pending_order that's not inside if order: block
    lines = method_content.split('\n')
    for i, line in enumerate(lines):
        if 'add_pending_order(order)' in line:
            # Check if previous lines have "if order:"
            prev_lines = '\n'.join(lines[max(0, i-5):i])
            if 'if order:' not in prev_lines:
                print("❌ FAIL: Found unconditional add_pending_order call")
                return False
    
    print("✅ PASS: No unconditional add_pending_order calls")
    
    print("\n✅ TEST 2 PASSED: Pending orders fix verified!")
    return True


def test_logging_improvements():
    """Test that all logging improvements are in place"""
    print("\n" + "="*80)
    print("TEST 3: Logging Improvements")
    print("="*80)
    
    with open('main.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    required_logs = [
        ('📦 Starting order management loop', 'Order management loop'),
        ('📋 Processing', 'Processing pending orders'),
        ('📤 Placing order for market', 'Placing order'),
    ]
    
    all_found = True
    for log_text, description in required_logs:
        if log_text in content:
            print(f"✅ PASS: Found '{description}' log")
        else:
            print(f"❌ FAIL: Missing '{description}' log")
            all_found = False
    
    if all_found:
        print("\n✅ TEST 3 PASSED: All logging improvements verified!")
        return True
    else:
        print("\n❌ TEST 3 FAILED: Some logging improvements missing")
        return False


def main():
    """Run all tests"""
    print("\n" + "="*80)
    print("🧪 RUNNING BUG FIX VERIFICATION TESTS")
    print("="*80)
    
    results = []
    
    # Test 1: Profit taking fix
    try:
        results.append(("Profit Taking Fix", test_profit_taking_fix()))
    except Exception as e:
        print(f"\n❌ TEST 1 CRASHED: {e}")
        results.append(("Profit Taking Fix", False))
    
    # Test 2: Pending orders fix
    try:
        results.append(("Pending Orders Fix", test_pending_orders_fix()))
    except Exception as e:
        print(f"\n❌ TEST 2 CRASHED: {e}")
        results.append(("Pending Orders Fix", False))
    
    # Test 3: Logging improvements
    try:
        results.append(("Logging Improvements", test_logging_improvements()))
    except Exception as e:
        print(f"\n❌ TEST 3 CRASHED: {e}")
        results.append(("Logging Improvements", False))
    
    # Summary
    print("\n" + "="*80)
    print("📊 TEST SUMMARY")
    print("="*80)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{status}: {name}")
    
    print(f"\n📊 Tests Passed: {passed}/{total}")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED! Bug fixes verified successfully!")
        return 0
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Please review the fixes.")
        return 1


if __name__ == '__main__':
    sys.exit(main())

