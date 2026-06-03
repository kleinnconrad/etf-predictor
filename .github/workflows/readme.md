# GitHub Workflows

This directory contains automated pipelines orchestrated by GitHub Actions.

* `update_etf_seed.yml`: Executes the Xetra instrument validation pipeline. Triggered manually via the GitHub interface (`workflow_dispatch`), this workflow dynamically downloads the latest T7 tradable instruments dump, regenerates the base seed list, and screens all instruments for age and liquidity criteria. Validated updates are isolated in an automated Pull Request for review.
