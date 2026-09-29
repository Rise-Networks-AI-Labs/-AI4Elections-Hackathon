import pandas as pd

PARTY_COLS = ["votes_A", "votes_B", "votes_C", "votes_D", "votes_E"]

def integrity_flags(df: pd.DataFrame) -> pd.DataFrame:
    """Rule-based consistency checks on results data. Flags are for HUMAN REVIEW only;
    they are not evidence of wrongdoing. Returns df with boolean flag columns added."""
    out = df.copy()
    valid = out[PARTY_COLS].sum(axis=1)
    out["flag_accredited_gt_registered"] = out["accredited_voters"] > out["registered_voters"]
    out["flag_sum_mismatch"] = (valid + out["rejected_votes"]) != out["accredited_voters"]
    out["flag_round_numbers"] = (out[PARTY_COLS] % 100 == 0).all(axis=1)
    out["flag_duplicate_of_previous"] = (out[PARTY_COLS] == out[PARTY_COLS].shift()).all(axis=1)
    return out
