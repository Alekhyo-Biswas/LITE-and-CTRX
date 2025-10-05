import shlex

def parse_line(line):
    """
    Returns: (cmd, args)
    Handles quoted strings as single arguments.
    """
    line = line.strip()
    if not line or line.startswith("#"):  # skip empty or comment
        return None

    # Use shlex to split, keeping quoted strings intact
    parts = shlex.split(line)
    cmd = parts[0]
    args = parts[1:]
    return cmd, args
