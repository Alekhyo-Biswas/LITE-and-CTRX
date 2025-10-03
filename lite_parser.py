def parse_line(line):
    # Remove comments and whitespace
    line = line.split('#')[0].strip()
    if not line:
        return None
    return line
