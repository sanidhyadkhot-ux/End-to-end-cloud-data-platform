from pathlib import Path

def test_readme_exists():
    assert Path("README.md").exists()

def test_data_exists():
    assert Path("data/raw/asx_market_ticks.csv").exists()
