from __future__ import annotations
import pandas as pd

DATETIME_COLUMNS = ["opened_at", "acknowledged_at", "restored_at", "closed_at"]

def prepare(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    for column in DATETIME_COLUMNS:
        result[column] = pd.to_datetime(result[column], utc=True)
    result["mtta_minutes"] = (
        result["acknowledged_at"] - result["opened_at"]
    ).dt.total_seconds() / 60
    result["mttr_minutes"] = (
        result["restored_at"] - result["opened_at"]
    ).dt.total_seconds() / 60
    result["month"] = result["opened_at"].dt.to_period("M").astype(str)
    return result

def headline_metrics(df: pd.DataFrame) -> dict[str, float]:
    prepared = prepare(df)
    return {
        "major_incidents": float(len(prepared)),
        "mtta_minutes": round(prepared["mtta_minutes"].mean(), 1),
        "mttr_minutes": round(prepared["mttr_minutes"].mean(), 1),
        "comms_on_time_pct": round(prepared["communications_on_time"].mean() * 100, 1),
        "repeat_incident_pct": round(prepared["repeat_incident"].mean() * 100, 1),
    }
