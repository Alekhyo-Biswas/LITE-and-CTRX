from lite_vm import LiteVM
from lite_parser import parse_sequences
import sys

def run_ltx_file(filename):
    # create a new VM instance
    vm = LiteVM()

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # break into sequences
    sequences = parse_sequences(content)

    first_sequence = True
    for seq in sequences:
        if not seq:
            continue

        # run first sequence immediately if first command is not an event
        first_cmd, first_args = seq[0]
        if first_sequence and first_cmd not in ('on', 'when', 'every', 'listen_for'):
            for cmd, args in seq:
                vm.execute(cmd, args)
            vm.clear_inst()  # clear instant vars after sequence
        else:
            # store other sequences for later (events)
            # for now just print for debugging
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
