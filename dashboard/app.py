from pathlib import Path
import pandas as pd
import streamlit as st

from metrics import headline_metrics, prepare

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "incidents.csv"

st.set_page_config(page_title="Major Incident Dashboard", layout="wide")
st.title("Major Incident Management Dashboard")
st.caption("Synthetic portfolio dataset")

df = pd.read_csv(DATA)
prepared = prepare(df)
metrics = headline_metrics(df)

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Major incidents", int(metrics["major_incidents"]))
c2.metric("MTTA", f'{metrics["mtta_minutes"]} min')
c3.metric("MTTR", f'{metrics["mttr_minutes"] / 60:.1f} h')
c4.metric("Comms on time", f'{metrics["comms_on_time_pct"]}%')
c5.metric("Repeat incidents", f'{metrics["repeat_incident_pct"]}%')

st.subheader("Incidents by month")
st.bar_chart(prepared.groupby("month").size())

st.subheader("Severity")
st.bar_chart(prepared.groupby("severity").size())

st.subheader("Resolver trend")
st.bar_chart(prepared.groupby("resolver").size())

st.subheader("Incident detail")
st.dataframe(
    prepared[
        ["incident_id", "severity", "service", "mtta_minutes", "mttr_minutes",
         "communications_on_time", "repeat_incident", "resolver"]
    ],
    use_container_width=True,
)
