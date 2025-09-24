# VCF Variant Filtering (Demo)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Data](https://img.shields.io/badge/Data-Synthetic%20(No%20PII)-red.svg)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOURNAME/vcf-variant-filtering-demo/blob/main/notebooks/exploratory.ipynb)

> **Demo project showcasing how I filter and annotate variants from VCF files using Python.**  
> All data are **synthetic** — this repo illustrates workflow and skills without exposing any proprietary or PHI/PII data.

---

## What this demonstrates
- Parsing VCF (line-oriented) without heavy native dependencies  
- Filtering by **Minor Allele Frequency (MAF)** (default `< 0.01`)  
- (Optional) Enriching with a **mock ClinVar** lookup (Pathogenic / Likely_pathogenic)  
- Exporting filtered variants as VCF  
- A small notebook walking through counts and filtering results  

> ⚠️ **Note:** This is a *demonstration repo*. Real pipelines I’ve built integrate with production-grade tools  
> (e.g., `bcftools`, `cyvcf2`, `htslib`, cloud batch systems, dashboards), but those are omitted here for portability and to avoid sensitive data.

---

## Quickstart

```bash
git clone https://github.com/YOURNAME/vcf-variant-filtering-demo.git
cd vcf-variant-filtering-demo
python -m venv .venv && source .venv/bin/activate  # optional
pip install -r requirements.txt

python scripts/filter_variants.py \
  --input data/example.vcf.gz \
  --output results/filtered_output.vcf \
  --clinvar-json data/mock_clinvar.json \
  --maf-threshold 0.01

---

## Repo layout
vcf-variant-filtering-demo/
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

---

🔗 More projects and work samples at [zrlo.dev] (https://zrlo.dev)
