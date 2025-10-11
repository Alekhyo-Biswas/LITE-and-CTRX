from lite_vm import LiteVM
from lite_parser import parse_sequences
import sys

def run_ltx_file(filename):
    # Create a new VM instance
    vm = LiteVM()

    # Register the 'use' command manually
    def cmd_use(args):
        if not args:
            print("Usage: use <library>")
            return
        libname = args[0]
        vm.load_library(libname)
    vm.register_command("use", cmd_use)

    # Read file content
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse into sequences
    sequences = parse_sequences(content)

    first_sequence = True
    for seq in sequences:
        if not seq:
            continue

        first_cmd, first_args = seq[0]

        # Run first sequence immediately if it doesn't start with an event
        if first_sequence and first_cmd not in ('on', 'when', 'every', 'listen_for'):
            for cmd, args in seq:
                vm.execute(cmd, args)
            vm.clear_inst()  # clear instant vars after sequence
        else:
            # Later event-handling (for debugging for now)
            print("Stored event sequence (not yet executed):")
            for cmd, args in seq:
                print(cmd, args)

        first_sequence = False


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <file.ltx>")
        return
    filename = sys.argv[1]
    run_ltx_file(filename)


if __name__ == "__main__":
    main()
