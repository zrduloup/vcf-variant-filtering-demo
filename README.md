# VCF Variant Filtering (Demo)

This repository is a **sample** showcasing how I approach **variant filtering and lightweight annotation** for genomics data.
It is **intended as a demo** of work I’ve done — **all data are synthetic** and **no PII or proprietary data** are included.

## What this demonstrates
- Parsing VCF (line-oriented) without heavy native dependencies
- Filtering by **Minor Allele Frequency (MAF)** (default `< 0.01`)
- (Optional) Enriching with a **mock ClinVar** lookup (Pathogenic / Likely_pathogenic)
- Exporting filtered variants as VCF
- A small notebook walking through counts and filtering results

> ⚠️ **Note:** This is a *demonstration repo*. Real pipelines I’ve built integrate with production-grade tools
> (e.g., bcftools, cyvcf2, htslib, cloud batch, dashboards), but those are omitted here for portability and to avoid any sensitive data.

## Quickstart

```bash
git clone https://github.com/YOURNAME/vcf-variant-filtering.git
cd vcf-variant-filtering
python -m venv .venv && source .venv/bin/activate  # optional
pip install -r requirements.txt
python scripts/filter_variants.py --input data/example.vcf.gz --output results/filtered_output.vcf --clinvar-json data/mock_clinvar.json --maf-threshold 0.01
```

## Repo layout
```
vcf-variant-filtering/
├── README.md
├── requirements.txt
├── data/
│   ├── example.vcf.gz
│   └── mock_clinvar.json
├── scripts/
│   ├── filter_variants.py
│   ├── annotate_clinvar.py
│   └── utils.py
├── notebooks/
│   └── exploratory.ipynb
└── results/
    └── filtered_output.vcf
```

## Skills illustrated
- Python scripting for data pipelines
- Practical genomics data handling (VCF)
- Quality/annotation thinking (e.g., ClinVar tags)
- Reproducible analysis with a small notebook
