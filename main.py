import sys
from lite_parser import parse_line
from lite_vm import execute_line

def run_ltx_file(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return

    for line_num, line in enumerate(lines, start=1):
        parsed = parse_line(line)
        if parsed:
            try:
                execute_line(parsed)
            except Exception as e:
                print(f"Error on line {line_num}: {parsed}")
                print(e)
                break

if __name__ == "__main__":
    # Check if filename was passed as a command-line argument
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        # Default example file
        filename = 'examples/hello.ltx'

    run_ltx_file(filename)
