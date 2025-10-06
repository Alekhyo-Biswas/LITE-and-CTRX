def register(vm):
    """
    Adds a helper function to the VM to evaluate conditions.
    Conditions support:
      - Comparisons: ==, !=, <, >, <=, >=
      - Logical: and, or
      - Variables: inst, temp, code vars
      - Literals: numbers, strings, booleans
    """
    import re

    def parse_value(token):
        token = token.strip()
        # boolean
        if token.lower() == "true":
            return True
        elif token.lower() == "false":
            return False
        # string literal
        if token.startswith('"') and token.endswith('"'):
            return token[1:-1]
        # number
        try:
            if "." in token:
                return float(token)
            return int(token)
        except:
            pass
        # variable lookup
        if token in vm.inst_vars:
            return vm.inst_vars[token]
        if token in vm.temp_vars:
            return vm.temp_vars[token]
        if token in vm.vars:
            return vm.vars[token]
        return token  # fallback: string

    def check_condition(cond_string):
        """
        Evaluates a condition string safely.
        Supports: ==, !=, <, >, <=, >=, and, or
        """
        # split by logical operators first
        or_parts = [part.strip() for part in cond_string.split(" or ")]
        for part in or_parts:
            and_parts = [p.strip() for p in part.split(" and ")]
            if all(eval_simple_comparison(p) for p in and_parts):
                return True
        return False

    def eval_simple_comparison(expr):
        # match <left> <op> <right>
        m = re.match(r'(.+?)\s*(==|!=|<=|>=|<|>)\s*(.+)', expr)
        if not m:
            # if no comparison, treat as a single boolean variable or literal
            val = parse_value(expr)
            return bool(val)
        left, op, right = m.groups()
        left_val = parse_value(left)
        right_val = parse_value(right)

        if op == "==": return left_val == right_val
        if op == "!=": return left_val != right_val
        if op == "<":  return left_val < right_val
        if op == ">":  return left_val > right_val
        if op == "<=": return left_val <= right_val
        if op == ">=": return left_val >= right_val
        return False

    vm.check_condition = check_condition
