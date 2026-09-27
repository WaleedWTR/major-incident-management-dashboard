# Major Incident Management Dashboard

![Dashboard tests](https://github.com/WaleedWTR/major-incident-management-dashboard/actions/workflows/tests.yml/badge.svg)

A sanitised service-operations portfolio project that turns major-incident records into measurable operational insight.

> **Provenance:** This repository is a public reconstruction informed by real major-incident management and operational dashboard experience. The dataset is entirely synthetic and contains no employer or production information.

## What this project demonstrates

- major-incident KPI design
- MTTA / MTTR measurement
- incident trend analysis
- business-impact tracking
- timeline and communications governance
- Python-based dashboarding
- synthetic operational datasets
- automated metric testing

## Dashboard metrics

- major incidents by month
- severity distribution
- mean time to acknowledge (MTTA)
- mean time to restore (MTTR)
- communications timeliness
- repeat incident rate
- supplier / resolver trends
- service impact

## Run locally

```bash
python -m pip install -r requirements.txt
streamlit run dashboard/app.py
```

## Test

```bash
python -m pytest -q
```

## Repository structure

```text
.
├── dashboard/
│   ├── app.py
│   └── metrics.py
├── data/
│   └── incidents.csv
├── docs/
│   ├── kpi-definitions.md
│   └── major-incident-lifecycle.md
├── tests/
│   └── test_metrics.py
└── requirements.txt
```

## Skills demonstrated

**Major Incident Management · ITSM · Service Operations · Python · Pandas · Streamlit · KPI Design · Operational Reporting**

## Evidence standard

The repo demonstrates the mechanics of the solution and the operating model without reproducing confidential screenshots, ticket data or internal processes.
