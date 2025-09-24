#!/usr/bin/env python3
import argparse, json
from utils import open_maybe_gzip, parse_info, rebuild_info

def key_for(chrom, pos, ref, alt):
    return f"{chrom}:{pos}:{ref}:{alt}"

def main():
    ap = argparse.ArgumentParser(description="Apply mock ClinVar annotations (demo).")
    ap.add_argument("--input", required=True, help="Input VCF (.vcf or .vcf.gz)")
    ap.add_argument("--output", required=True, help="Output VCF with CLNSIG in INFO (plain .vcf)")
    ap.add_argument("--clinvar-json", required=True, help="Mock ClinVar JSON")
    args = ap.parse_args()

    with open(args.clinvar_json, "r") as f:
        clinvar = json.load(f)

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
            k = key_for(chrom, pos, ref, alt)
            if k in clinvar:
                info_dict["CLNSIG"] = clinvar[k]["clnsig"]
            cols[7] = rebuild_info(info_dict)
            fout.write("\t".join(cols) + "\n")

if __name__ == "__main__":
    main()
