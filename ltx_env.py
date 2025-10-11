from lite_vm import LiteVM
from lite_parser import LiteParser

def main():
    vm = LiteVM()
    parser = LiteParser(vm)

    print("LTX Environment (type 'exit' or 'quit' to leave)")
    print("Type blank line to execute a command sequence\n")

    buffer = []
    while True:
        try:
            line = input("LTX > ").strip()
            if line.lower() in ("exit", "quit"):
                print("Exiting LTX.")
                break

            # detect command sequence boundary
            if line == "":
                if buffer:
                    parser.parse("\n".join(buffer))
                    buffer.clear()
                continue

            buffer.append(line)

        except KeyboardInterrupt:
            print("\nExiting LTX.")
            break
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
