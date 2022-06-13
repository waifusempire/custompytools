"Simple flush function"


def flush():
    import sys
    try:
        sys.stdin.flush()
    except:
        sys.stdout.flush()