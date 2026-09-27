from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "dashboard"))

from metrics import headline_metrics, prepare  # noqa: E402

def load_data():
    return pd.read_csv(ROOT / "data" / "incidents.csv")

def test_prepare_adds_operational_metrics():
    prepared = prepare(load_data())
    assert "mtta_minutes" in prepared.columns
    assert "mttr_minutes" in prepared.columns
    assert prepared["mtta_minutes"].min() >= 0
    assert prepared["mttr_minutes"].min() >= 0

def test_headline_metrics_are_sensible():
    metrics = headline_metrics(load_data())
    assert metrics["major_incidents"] == 9
    assert 0 <= metrics["comms_on_time_pct"] <= 100
    assert 0 <= metrics["repeat_incident_pct"] <= 100
    assert metrics["mttr_minutes"] > metrics["mtta_minutes"]
