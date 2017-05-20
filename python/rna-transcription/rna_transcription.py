def to_rna(strand):
    """Return a string of DNA as the RNA equivalent"""
    try:
        from string import maketrans
    except ImportError:
        pass
    for base in strand:
        if not base in "GCTA":
            return "" 
    return strand.translate(maketrans("GCTA", "CGAU"))
