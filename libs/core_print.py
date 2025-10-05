def execute(vm, args):
    if not args:
        print("(nothing)")
        return

    token = args[0]

    # If token starts and ends with double quotes → string literal
    if token.startswith('"') and token.endswith('"'):
        # strip the quotes and print the content
        value = token[1:-1]
        print(value)
    else:
        # assume it's a variable name in vm.variables
        if token in vm.variables:
            print(vm.variables[token])
        else:
            print(f"(undefined var: {token})")
