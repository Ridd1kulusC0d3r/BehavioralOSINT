# Behavioral OSINT: evaluation protocol (research preview)

**Status:** protocol proposal, not a validated accuracy claim. All examples in CI are synthetic. This project does not establish a person's identity, intent, psychological characteristics, or whereabouts.

## Research question

Can a tool identify **observable changes in aggregate public activity** more reliably than transparent baseline methods, without treating gaps in collection as changes in behavior?

This is a hypothesis to test, not proof of a person's characteristics.

## Allowed evaluation inputs

- Synthetic event sequences with declared generation parameters and known missingness.
- Voluntary, consented self-audit data with collection scope and retention periods.
- Aggregate, non-identifying records that satisfy the applicable rights and licenses.

Do not upload real-person dossiers, precise daily routines, personal contact information, or sensitive characteristics into a public benchmark. Never publish inferred home/work locations or individual activity schedules.

## Ground truth and negative control

Define the expected labels **before** observing predictions. Separate:
- Actual synthetic shifts in event volume or timing.
- **Negative control**: stable synthetic timelines, randomized timestamps, empty sequences, and degraded coverage.
- Confounders: platform outages, API sampling limits, automated posts, shared accounts, time-zone changes, weekends, and seasonal effects.

A missing event with insufficient coverage must remain `unknown`, not a confidently classified behavioral change.

## Reproducibility contract

For every experiment preserve:
1. Dataset provenance, license, consent or synthetic generator parameters.
2. Unit of analysis, inclusion and exclusion criteria.
3. Pre-registered hypothesis and deterministic baseline.
4. Train/test separation when statistical or ML methods are involved.
5. Execution environment, tool version, seed, date, and checksums.
6. Raw counts for true/false positives and true/false negatives.
7. Limitations, error analysis and competing explanations.

## Metrics and acceptance criteria

Report precision, recall, false-positive rate, false-negative rate, base rates, abstention/unknown rate, and confidence intervals where applicable. Always compare against a trivial baseline. Explicitly distinguish link existence, metadata similarity, and verified correspondence.

**Acceptance for any efficacy claim:** disclose a synthetic or consented validation dataset, a negative control, comparable baseline, method of scoring and failure cases. With no independently audited ground truth, mark a claim **unmeasured**, never validated.

A correlation is **not proof** of identity, intention, causality, personality, or a real person's whereabouts.

## Safety and governance

- Public availability of a record is not equivalent to consent for aggregation or profiling.
- Use privacy-preserving summaries when possible; minimize collection and define deletion dates.
- Do not operationalize inference about protected or intimate traits.
- Human review is required for consequential interpretations.
- Prefer personal self-audits, aggregate campaign studies and synthetic casework over targeting individuals.

## What CI validates

CI checks Python syntax, repository hygiene and deterministic math using invented vectors. It **does not validate any behavioral inference, scientific claim, external service, or live data collection**.
