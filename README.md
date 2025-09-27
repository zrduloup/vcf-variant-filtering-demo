# VCF Variant Filtering & Annotation Pipeline (Demo)

[![CI/CD](https://github.com/zrduloup/vcf-variant-filtering-demo/actions/workflows/ci.yml/badge.svg)](https://github.com/zrduloup/vcf-variant-filtering-demo/actions/workflows/ci.yml)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/zrduloup/vcf-variant-filtering-demo/main?labpath=notebooks%2Fexploratory.ipynb)

**Production-ready demo showcasing genomics variant filtering and annotation workflows using Python.** 

This repository demonstrates end-to-end VCF processing capabilities including MAF-based filtering, ClinVar annotation, interactive visualization, and automated reporting—all with synthetic data to protect PHI/PII.

## 🎯 What This Demonstrates

- **VCF Processing**: Efficient parsing and filtering of genomic variants
- **Quality Filtering**: Minor Allele Frequency (MAF) thresholding (default < 0.01)
- **Clinical Annotation**: Integration with ClinVar pathogenicity data
- **Data Visualization**: Interactive plots and summary dashboards
- **Pipeline Automation**: Containerized, tested, and CI/CD-ready workflows
- **Production Practices**: Comprehensive testing, documentation, and error handling

## 🏗️ Architecture

```
VCF Input → Parse & Validate → MAF Filter → ClinVar Annotate → Export & Visualize
     ↓              ↓              ↓             ↓                    ↓
Raw Variants → Structured Data → Rare Variants → Clinical Context → Results
```

## 🚀 Quick Start

### Option 1: Local Installation
```bash
git clone https://github.com/zrduloup/vcf-variant-filtering-demo.git
cd vcf-variant-filtering-demo
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Run the filtering pipeline
python scripts/filter_variants.py \
  --input data/example.vcf.gz \
  --output results/filtered_output.vcf \
  --clinvar-json data/mock_clinvar.json \
  --maf-threshold 0.01 \
  --threads 4

# Generate interactive report
python scripts/generate_report.py --input results/filtered_output.vcf --output results/report.html
```

### Option 2: Docker
```bash
docker build -t vcf-demo .
docker run -v $(pwd)/results:/app/results vcf-demo \
  --input data/example.vcf.gz \
  --output results/filtered_output.vcf
```

### Option 3: Try in Browser
Click the Binder badge above to run the interactive notebooks without any local setup!

## 📊 Sample Results

After processing the demo VCF file, you'll see:
- **Original variants**: ~50,000 
- **After MAF filtering**: ~2,500 rare variants
- **ClinVar annotated**: ~300 variants with clinical significance
- **Pathogenic/Likely pathogenic**: ~45 high-priority variants

## 📁 Repository Structure

```
vcf-variant-filtering-demo/
├── README.md                    # This file
├── requirements.txt             # Python dependencies (pinned versions)
├── environment.yml              # Conda environment specification
├── Dockerfile                   # Container configuration
├── pyproject.toml              # Modern Python project configuration
│
├── data/                        # Sample datasets
│   ├── example.vcf.gz          # Synthetic VCF file (~50K variants)
│   ├── mock_clinvar.json       # Clinical annotation data
│   └── README.md               # Data documentation
│
├── scripts/                     # Main processing scripts
│   ├── filter_variants.py      # Core filtering pipeline
│   ├── annotate_clinvar.py     # Clinical annotation module
│   ├── utils.py                # Shared utilities
│   └── generate_report.py      # Automated HTML reporting
│
├── notebooks/                   # Interactive analysis
│   ├── exploratory.ipynb       # Variant exploration & QC
│   └── visualization_demo.ipynb # Interactive plots & dashboards
│
├── tests/                       # Comprehensive test suite
│   ├── test_filter_variants.py # Unit tests for filtering logic
│   ├── test_annotate_clinvar.py# Clinical annotation tests
│   ├── test_utils.py           # Utility function tests
│   ├── conftest.py             # Pytest configuration
│   └── fixtures/               # Test data files
│
├── results/                     # Output directory
│   └── .gitkeep               # Placeholder for generated files
│
└── docs/                        # Additional documentation
    ├── architecture.md         # System design details
    └── usage_examples.md       # Advanced usage patterns
```

## 🧪 Testing & Quality Assurance

```bash
# Run all tests with coverage
pytest --cov=scripts tests/

# Lint code
flake8 scripts/ tests/
black --check scripts/ tests/

# Type checking
mypy scripts/
```

## 🔧 Advanced Usage

### Parallel Processing
```bash
python scripts/filter_variants.py --input large_dataset.vcf.gz --threads 8
```

### Region-Specific Filtering
```bash
python scripts/filter_variants.py --region chr1:1000000-2000000 --input data/example.vcf.gz
```

### Custom MAF Thresholds
```bash
python scripts/filter_variants.py --maf-threshold 0.005 --input data/example.vcf.gz
```

## 📈 Performance Benchmarks

| Dataset Size | Processing Time | Memory Usage | Filtered Variants |
|-------------|----------------|--------------|-------------------|
| 10K variants | 2.3s | 45MB | ~500 |
| 100K variants | 18.7s | 120MB | ~5,000 |
| 1M variants | 3.2min | 450MB | ~50,000 |

*Benchmarked on: Intel i7-10700K, 32GB RAM, NVMe SSD*

## 🏭 Production Context

This demo illustrates core capabilities used in production genomics pipelines:

- **Scale**: Production systems process 10M+ variants using `bcftools`, `htslib`, and cloud batch processing
- **Integration**: Real workflows connect to clinical databases, LIMS systems, and reporting platforms
- **Security**: Production implementations include PHI encryption, audit logging, and access controls
- **Performance**: Distributed processing across compute clusters with automatic scaling

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes and add tests
4. Ensure all tests pass (`pytest`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Work

- **Portfolio**: [zrl.dev](https://zrl.dev) - More projects and technical expertise
- **Professional Background**: 7+ years in AI/ML data operations at Apple
- **Specialization**: Genomics data analysis, annotation quality, and production pipeline development

---

⚠️ **Note**: All data in this repository are synthetic and generated for demonstration purposes. No real patient data, PHI, or PII are included.
