import yaml

with open('config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

scanner = config.get('market_scanner', {})
print(f"max_competition_bars: {scanner.get('max_competition_bars', 'NOT FOUND')}")
print(f"min_reward: {scanner.get('min_reward', 'NOT FOUND')}")

