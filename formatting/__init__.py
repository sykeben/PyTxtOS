class coldat:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'  # OK (In Blue)
    OKGREEN = '\033[92m'  # OK (In Green)
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'  # Reset Colors
    RESET = ENDC  # Alias for Reset Colors
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def okblu(text):
    return coldat.OKBLUE + text + coldat.RESET


def okgrn(text):
    return coldat.OKGREEN + text + coldat.RESET


def head(text):
    return coldat.HEADER + text + coldat.RESET


def warn(text):
    return coldat.WARNING + text + coldat.RESET


def fail(text):
    return coldat.FAIL + text + coldat.RESET


def bold(text):
    return coldat.BOLD + text + coldat.RESET


def uline(text):
    return coldat.UNDERLINE + text + coldat.RESET