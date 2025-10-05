import shlex

def parse_file(filename):
    """
    Returns a list of command sequences.
    Each sequence is a list of (cmd, args) tuples.
    - Each sequence must start with an <event>
    - Blank lines end the sequence
    - Comments (#) are ignored
    """
    sequences = []
    current_seq = []
    sequence_started = False

    with open(filename, 'r') as f:
        for line in f:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue

            # Detect event line
            if stripped.startswith("<") and stripped.endswith(">"):
                if current_seq:
                    sequences.append(current_seq)
                current_seq = [("event", [stripped[1:-1]])]  # store event name
                sequence_started = True
                continue

            if sequence_started:
                parts = shlex.split(stripped)
                cmd = parts[0]
                args = parts[1:]
                current_seq.append((cmd, args))
            else:
                continue  # ignore lines before first event

    if current_seq:
        sequences.append(current_seq)

    return sequences

