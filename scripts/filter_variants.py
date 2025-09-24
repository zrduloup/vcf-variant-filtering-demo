#!/usr/bin/env python3
import argparse, json, sys
from utils import open_maybe_gzip, parse_info, rebuild_info

def load_clinvar(path):
    if not path:
        return {}
    with open(path, "r") as f:
        return json.load(f)

def key_for(chrom, pos, ref, alt):
    return f"{chrom}:{pos}:{ref}:{alt}"

def variant_passes(maf_str, maf_threshold):
    try:
        if maf_str is None:
            return False
        return float(maf_str) < maf_threshold
    except ValueError:
        return False

def is_pathogenic(clnsig):
    if not clnsig:
        return False
    return clnsig.lower() in {"pathogenic", "likely_pathogenic", "likely-pathogenic"}

def main():
    ap = argparse.ArgumentParser(description="Filter VCF by MAF and pathogenicity (demo).")
    ap.add_argument("--input", required=True, help="Input VCF (.vcf or .vcf.gz)")
    ap.add_argument("--output", required=True, help="Output VCF (plain .vcf)")
    ap.add_argument("--maf-threshold", type=float, default=0.01, help="MAF threshold (default: 0.01)")
    ap.add_argument("--clinvar-json", default=None, help="Optional ClinVar JSON lookup (demo)")
    args = ap.parse_args()

    clinvar = load_clinvar(args.clinvar_json)

    with open_maybe_gzip(args.input, "rt") as fin, open(args.output, "w") as fout:
        for line in fin:
            if line.startswith("#"):
                fout.write(line)
                continue
            cols = line.rstrip("\n").split("\t")
            if len(cols) < 8:
                continue
            chrom, pos, _id, ref, alt, qual, filt, info = cols[:8]
            info_dict = parse_info(info)

            # Annotate from mock ClinVar (demo)
            k = key_for(chrom, pos, ref, alt)
            if k in clinvar:
                info_dict["CLNSIG"] = clinvar[k]["clnsig"]

            maf = info_dict.get("MAF")
            clnsig = info_dict.get("CLNSIG")

            if variant_passes(maf, args.maf_threshold) and (is_pathogenic(clnsig)):
                # pass: write record (rebuild INFO in case we added CLNSIG)
                cols[7] = rebuild_info(info_dict)
                fout.write("\t".join(cols) + "\n")

if __name__ == "__main__":
    main()
