def parse_line(line):
    line = line.strip()
    if not line or line.startswith("#"):  # skip empty or comment
        return None

    parts = line.split()
    cmd = parts[0]
    args = parts[1:]
    return cmd, args
