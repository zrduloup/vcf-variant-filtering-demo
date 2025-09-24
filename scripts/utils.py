import gzip

def open_maybe_gzip(path, mode="rt"):
    """
    Open text or gzipped text file transparently.
    """
    if path.endswith(".gz"):
        return gzip.open(path, mode)
    return open(path, mode)

def parse_info(info_str):
    """
    Parse INFO field into a dict. Example: "MAF=0.003;CLNSIG=Pathogenic"
    """
    d = {}
    if info_str == "." or not info_str:
        return d
    for item in info_str.split(";"):
        if "=" in item:
            k, v = item.split("=", 1)
            d[k] = v
        else:
            d[item] = True
    return d

def rebuild_info(info_dict):
    parts = []
    for k, v in info_dict.items():
        if v is True:
            parts.append(k)
        else:
            parts.append(f"{k}={v}")
    return ";".join(parts) if parts else "."
