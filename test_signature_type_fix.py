"""
Test script to verify signature_type fix in profit_taking_manager.py
"""

import sys
import re

def test_signature_type_removed():
    """Test that signature_type=2 has been removed from profit_taking_manager.py"""
    print("\n" + "="*80)
    print("TEST: Signature Type Fix")
    print("="*80)
    
    with open('profit_taking_manager.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Check 1: Should NOT have signature_type=2 in actual code (not in comments)
    has_signature_type_2 = False
    for i, line in enumerate(lines, 1):
        # Skip comments
        if line.strip().startswith('#'):
            continue
        # Check if line has signature_type=2 (not in comment)
        code_part = line.split('#')[0]  # Get part before comment
        if 'signature_type=2' in code_part or 'signature_type = 2' in code_part:
            print(f"❌ FAIL: Line {i} has signature_type=2 in code")
            print(f"   Line: {line.strip()}")
            print("   This is WRONG for EOA wallets (private key from .env)")
            print("   signature_type=2 is for browser wallets only")
            has_signature_type_2 = True

    if not has_signature_type_2:
        print("✅ PASS: No signature_type=2 found in code")
    
    if has_signature_type_2:
        return False

    # Check 2: Should NOT have signature_type=1 in actual code
    content = ''.join(lines)
    has_signature_type_1 = False
    for i, line in enumerate(lines, 1):
        # Skip comments
        if line.strip().startswith('#'):
            continue
        code_part = line.split('#')[0]
        if 'signature_type=1' in code_part or 'signature_type = 1' in code_part:
            print(f"❌ FAIL: Line {i} has signature_type=1")
            print("   This is for email wallets, not EOA wallets")
            has_signature_type_1 = True

    if not has_signature_type_1:
        print("✅ PASS: No signature_type=1 found in code")
    else:
        return False
    
    # Check 3: Should have comment explaining signature_type
    if 'signature_type=0 is default for EOA wallets' in content:
        print("✅ PASS: Has explanatory comment about signature_type")
    else:
        print("⚠️  WARNING: Missing explanatory comment (not critical)")
    
    # Check 4: ClobClient should be initialized with only host, key, chain_id
    # Find all ClobClient initializations
    clob_client_pattern = r'ClobClient\s*\([^)]+\)'
    matches = re.findall(clob_client_pattern, content, re.DOTALL)
    
    print(f"\n📋 Found {len(matches)} ClobClient initialization(s)")
    
    for i, match in enumerate(matches, 1):
        print(f"\n   ClobClient #{i}:")
        # Check if it has signature_type parameter
        if 'signature_type' in match:
            print(f"   ❌ FAIL: Has signature_type parameter")
            print(f"   Code: {match[:100]}...")
            return False
        else:
            print(f"   ✅ PASS: No signature_type parameter")
            # Check if it has the required parameters
            if 'host' in match and 'key' in match and 'chain_id' in match:
                print(f"   ✅ PASS: Has required parameters (host, key, chain_id)")
            else:
                print(f"   ⚠️  WARNING: May be missing some parameters")
    
    print("\n✅ TEST PASSED: Signature type fix verified!")
    print("\n📝 Summary:")
    print("   - signature_type parameter removed (will use default=0 for EOA wallets)")
    print("   - This matches the working implementation in order_manager.py")
    print("   - EOA wallets (private key from .env) use signature_type=0")
    print("   - Browser wallets use signature_type=2")
    print("   - Email wallets use signature_type=1")
    return True


def main():
    """Run test"""
    print("\n" + "="*80)
    print("🧪 TESTING SIGNATURE TYPE FIX")
    print("="*80)
    
    try:
        result = test_signature_type_removed()
        
        if result:
            print("\n🎉 ALL TESTS PASSED!")
            print("\n📋 Next Steps:")
            print("   1. Deploy code to VPS: git pull origin master")
            print("   2. Restart bot: python main.py")
            print("   3. Check logs for successful SELL order placement")
            print("   4. Expected log: '✅ SELL order placed successfully!'")
            print("   5. No more 'invalid signature' errors!")
            return 0
        else:
            print("\n❌ TEST FAILED!")
            print("   Please review the code and fix the issues.")
            return 1
            
    except Exception as e:
        print(f"\n❌ TEST CRASHED: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())

