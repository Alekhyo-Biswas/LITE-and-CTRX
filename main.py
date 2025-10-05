import sys  #this allows entering ant .ltx file
from lite_parser import parse_line
from lite_vm import LiteVM

def run_ltx_file(filename):
    vm = LiteVM()  # new VM instance

    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return

    for line_num, line in enumerate(lines, start=1):
        parsed = parse_line(line)
        if parsed:
            cmd, args = parsed
            try:
                vm.execute(cmd, args)
            except Exception as e:
                print(f"Error on line {line_num}: {line.strip()}")
                print(e)
                break

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        print("Usage: python main.py <file.ltx>")
        sys.exit(1)

    run_ltx_file(filename)
