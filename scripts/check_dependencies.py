"""
Check all required dependencies
"""

import sys

# Core modules to check
REQUIRED_MODULES = {
    'aiohttp': 'aiohttp',
    'websockets': 'websockets',
    'playwright': 'playwright.async_api',
    'yaml': 'yaml',
    'torch': 'torch',
    'numpy': 'numpy',
    'pandas': 'pandas',
    'sklearn': 'sklearn',
    'psutil': 'psutil',
    'dotenv': 'dotenv',
    'web3': 'web3',
    'py_clob_client': 'py_clob_client.client',
}

print("="*80)
print("🔍 CHECKING DEPENDENCIES")
print("="*80)

missing = []
installed = []

for name, import_path in REQUIRED_MODULES.items():
    try:
        module = __import__(import_path.split('.')[0])
        version = getattr(module, '__version__', 'unknown')
        installed.append((name, version))
        print(f"✅ {name:20s} - version {version}")
    except ImportError as e:
        missing.append(name)
        print(f"❌ {name:20s} - NOT INSTALLED")

print("\n" + "="*80)
if missing:
    print(f"❌ MISSING {len(missing)} MODULES:")
    for m in missing:
        print(f"   - {m}")
    print("\n💡 Install with: pip install " + " ".join(missing))
    sys.exit(1)
else:
    print(f"✅ ALL {len(installed)} CORE MODULES INSTALLED!")
    print("\n🚀 Bot is ready to run!")
    sys.exit(0)

