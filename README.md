# Behavioral OSINT [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Curated list of tools, techniques, papers and datasets for **behavioral OSINT**: inferring patterns (when, how, where, with whom) from public digital traces, not just collecting data points.

Contributions welcome, see [CONTRIBUTING.md](CONTRIBUTING.md). Use only on public data, with authorization, and read the [Ethics](#ethics) section first.

## Contents

- [Username and Identity Correlation](#username-and-identity-correlation)
- [Stylometry and Authorship Attribution](#stylometry-and-authorship-attribution)
- [Temporal and Pattern-of-Life Analysis](#temporal-and-pattern-of-life-analysis)
- [Social Graph and Network Analysis](#social-graph-and-network-analysis)
- [Coordinated Behavior and Bot Detection](#coordinated-behavior-and-bot-detection)
- [Image, Geo and Metadata Behavior](#image-geo-and-metadata-behavior)
- [Frameworks and Collection Platforms](#frameworks-and-collection-platforms)
- [Innovations and Research Directions](#innovations-and-research-directions)
- [Learning Resources](#learning-resources)
- [Python Mini-Tools (this repo)](#python-mini-tools-this-repo)
- [Ethics](#ethics)

## Username and Identity Correlation

- [Sherlock](https://github.com/sherlock-project/sherlock) - Hunt usernames across hundreds of social networks.
- [Maigret](https://github.com/soxoj/maigret) - Collect a dossier by username, parsing profile pages and recursing on new IDs.
- [WhatsMyName](https://github.com/WebBreacher/WhatsMyName) - Community-maintained dataset of username-enumeration sites (data source for many tools).
- [Social Analyzer](https://github.com/qeeqbox/social-analyzer) - Profile finder across ~1000 sites with detection scoring.
- [Holehe](https://github.com/megadose/holehe) - Check which sites an email is registered on.
- [GHunt](https://github.com/mxrch/GHunt) - Investigate Google accounts from public identifiers.
- [Blackbird](https://github.com/p1ngul1n0/blackbird) - Username/email search across many sites; reportedly adds AI-based profile summaries (check the README).

## Stylometry and Authorship Attribution

- [JStylo / Anonymouth](https://github.com/psal/jstylo) - Authorship attribution framework (Drexel PSAL) and its anonymization companion.
- [Faststylometry](https://github.com/fastdatascience/faststylometry) - Simple Python Burrows' Delta implementation.
- [Stylo (R)](https://github.com/computationalstylistics/stylo) - Reference R package for computational stylistics.
- [NLTK](https://www.nltk.org/) - Build function-word and n-gram profiles in plain Python.

## Temporal and Pattern-of-Life Analysis

Sleep/wake cycles, posting rhythm, timezone and holiday inference from timestamps.

- [Osintgram](https://github.com/Datalux/Osintgram) - Instagram interaction analysis (archived upstream, fork-dependent).
- [Twint (archived)](https://github.com/twintproject/twint) - Historical reference for scraping timelines without API; see [Social Graph](#social-graph-and-network-analysis) for alternatives.
- [Wayback Machine CDX API](https://github.com/internetarchive/wayback) - Page change history as a behavioral timeline.
- [`tools/tz_guess.py`](tools/tz_guess.py) - Minimal timezone/activity-window estimator from timestamps (this repo).

## Social Graph and Network Analysis

- [Gephi](https://gephi.org/) - Graph visualization and community detection.
- [NetworkX](https://github.com/networkx/networkx) - Python graph analysis (centrality, communities).
- [Maltego](https://www.maltego.com/) - Link analysis platform (commercial, community edition available).
- [socioscan](https://github.com/h9zdev/socioscan) - Narratives, sentiment, influencers and account clusters from social posts (Bellingcat hackathon project).

## Coordinated Behavior and Bot Detection

- [Botometer](https://botometer.osome.iu.edu/) - Bot-likelihood scoring (Indiana University OSoMe).
- [OSoMe tools](https://osome.iu.edu/tools/) - Observatory on Social Media research tools.
- [Coordination detection (CooRnet)](https://github.com/fabiogiglietto/CooRnet) - Detect coordinated link sharing.

## Image, Geo and Metadata Behavior

- [ExifTool](https://exiftool.org/) - Read/write metadata in files.
- [SunCalc](https://www.suncalc.org/) - Sun position for chronolocation of photos.
- [Bellingcat Online Investigations Toolkit](https://github.com/bellingcat/toolkit) - Bellingcat's curated tool index.
- [Bellingcat Auto Archiver](https://github.com/bellingcat/auto-archiver) - Automatically archive social posts as evidence.

## Frameworks and Collection Platforms

- [SpiderFoot](https://github.com/smicallef/spiderfoot) - Automated OSINT collection and correlation.
- [Recon-ng](https://github.com/lanmaster53/recon-ng) - Modular web reconnaissance framework.
- [theHarvester](https://github.com/laramies/theHarvester) - Emails, subdomains, names from public sources.
- [AnubisX](https://github.com/AnubisXFramework/AnubisXFramework) - Research framework for behavioral digital attribution (stylometric fingerprints of operators). Self-reported results (see its [Zenodo record](https://zenodo.org/records/21446923)); no independent evaluation.
- [Xkeystroke](https://github.com/AIOSINT/Xkeystroke) - Web-interface OSINT aggregation/analysis tool by the AIOSINT org. Early-stage, review before use.
- [OPSEC-OSINT-Tools](https://github.com/airborne-commando/OPSEC-OSINT-Tools) - Guide collection; see `markdown/Digital-Profiling.md` for a digital profiling pipeline.
- [Awesome OSINT](https://github.com/jivoi/awesome-osint) - The general OSINT list this one complements.

## Innovations and Research Directions

Ideas worth building or tracking (PRs with working implementations welcome):

- **LLM-assisted stylometry** - Embedding-based author similarity instead of hand-built features; beware adversarial paraphrasing.
- **Cross-platform behavioral fingerprints** - Combine posting rhythm + vocabulary + emoji/punctuation habits into a single fingerprint, with confidence scores rather than binary matches.
- **Pattern-of-life from archives** - Wayback/Archive.today snapshots as a low-noise timeline of edits and deletions.
- **Deletion behavior** - Track what gets removed and when (e.g. via archives and caches) as a signal.
- **Evidence-grade pipelines** - Hashing + archiving every collected artifact for reproducibility.
- **Counter-OSINT / self-audit** - Measure your own behavioral leakage before an adversary does.

### Candidates under review

Mentioned but **not yet verified** (no repository found, or only an alpha announcement). PRs with a confirmed URL are welcome:

- **MOSAIC** - multi-platform behavioral analysis (GitHub, Reddit, YouTube...), local analysis via Ollama; only an alpha Reddit announcement found.
- **SocioSential** - no repository found; the closest verified match is [socioscan](https://github.com/h9zdev/socioscan).

## Learning Resources

- [Bellingcat Guides](https://www.bellingcat.com/resources/) - Practical investigation guides.
- [OSINT Framework](https://osintframework.com/) - Categorized tool tree.
- [Trace Labs](https://www.tracelabs.org/) - Ethical OSINT missing-persons CTFs.
- [IntelTechniques](https://inteltechniques.com/) - Michael Bazzell's resources.
- [Sofia Santos OSINT Resources](https://gralhix.com/) - Tutorials and challenges.

## Python Mini-Tools (this repo)

Stdlib-only, simple by design:

| Tool | What it does |
|------|--------------|
| [`tools/tz_guess.py`](tools/tz_guess.py) | Estimate timezone offset and active hours from a list of timestamps. |
| [`tools/style_compare.py`](tools/style_compare.py) | Compare two texts by function-word profile (cosine similarity). |
| [`tools/check_links.py`](tools/check_links.py) | Check that every link in the README resolves. |

## Ethics

- Collect only **public** data; respect platform terms and local law (LGPD, GDPR).
- Behavioral inference yields **probabilities, not proof**. Report confidence and false-positive risk.
- Never use these techniques for stalking, doxxing or harassment. Prefer defensive use: self-audit, missing-persons (Trace Labs), threat intel.

## License

[CC0 1.0](LICENSE)
