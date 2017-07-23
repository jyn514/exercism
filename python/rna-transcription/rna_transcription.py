def to_rna(strand):
    """Return a string of DNA as the RNA equivalent"""
    for base in strand:
        if base not in "GCTA":
            return ""
    try:                    # python2
        from string import maketrans
        return strand.translate(maketrans("GCTA", "CGAU"))
    except ImportError:     # python3
        return strand.translate(str.maketrans("GCTA", "CGAU"))
