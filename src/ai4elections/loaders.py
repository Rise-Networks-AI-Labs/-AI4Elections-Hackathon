from pathlib import Path
import json
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "synthetic"

def load_csv(name: str) -> pd.DataFrame:
    """Load a CSV from data/synthetic by filename."""
    return pd.read_csv(DATA_DIR / name)

def load_jsonl(name: str) -> pd.DataFrame:
    with open(DATA_DIR / name, encoding="utf-8") as f:
        return pd.DataFrame([json.loads(line) for line in f])
