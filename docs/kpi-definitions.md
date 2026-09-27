# KPI Definitions

## Major incident count

Number of records classified as major incidents in the selected period.

## Mean Time to Acknowledge (MTTA)

```text
acknowledged_at - opened_at
```

Measures how quickly the major-incident process is engaged.

## Mean Time to Restore (MTTR)

```text
restored_at - opened_at
```

Measures elapsed time until service restoration. It is deliberately separated from final closure.

## Communications on time

Percentage of incidents where communications met the defined operational cadence.

## Repeat incident rate

Percentage of major incidents marked as a recurrence of a previously known failure pattern.

## Interpretation

Metrics should not be used in isolation. A lower MTTR can still hide poor communications, repeat failures or weak problem management. Operational review should combine speed, customer impact, recurrence and quality.
