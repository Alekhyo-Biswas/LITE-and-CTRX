from lite_parser import parse_line
from lite_vm import execute_line

def run_ltx_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    for line in lines:
        parsed = parse_line(line)
        if parsed:
            execute_line(parsed)

if __name__ == "__main__":
    run_ltx_file('examples/hello.ltx')

