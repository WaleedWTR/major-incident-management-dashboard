#!/usr/bin/env python3
from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "dashboard"))

from metrics import headline_metrics  # noqa: E402

DATA = ROOT / "data" / "incidents.csv"

def main() -> None:
    metrics = headline_metrics(pd.read_csv(DATA))
    print("# Synthetic Major Incident Summary")
    print()
    print(f"- Major incidents: {int(metrics['major_incidents'])}")
    print(f"- Mean time to acknowledge: {metrics['mtta_minutes']} minutes")
    print(f"- Mean time to restore: {metrics['mttr_minutes']} minutes")
    print(f"- Communications on time: {metrics['comms_on_time_pct']}%")
    print(f"- Repeat incident rate: {metrics['repeat_incident_pct']}%")

if __name__ == "__main__":
    main()
