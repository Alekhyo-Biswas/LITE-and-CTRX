import shlex

def parse_command(line: str):
    """
    Split a single line into (command, args) using shlex.
    Returns ("", []) if the line is empty or only a comment.
    """
    # strip off comment lines first
    line = line.strip()
    if not line or line.startswith("//") or line.startswith("#"):
        return "", []  # skip comments / blank lines

    try:
        parts = shlex.split(line, posix=True)
    except ValueError as e:
        print(f"Parse error: {e} in line: {line}")
        return "", []

    if not parts:
        return "", []

    cmd = parts[0]
    args = parts[1:]
    return cmd, args


def parse_sequences(text: str):
    """
    Break a whole .ltx file into command sequences.
    Each sequence starts with an <event> line.
    Sequences are separated by at least one blank line.
    Returns a list of lists of (cmd, args).
    """
    sequences = []
    current_seq = []

    for rawline in text.splitlines():
        line = rawline.strip()

        # if it's a blank line, that ends a sequence
        if not line:
            if current_seq:
                sequences.append(current_seq)
                current_seq = []
            continue

        cmd, args = parse_command(rawline)
        if not cmd:
            continue  # skip comments / empty

        current_seq.append((cmd, args))

    if current_seq:
        sequences.append(current_seq)

    return sequences
