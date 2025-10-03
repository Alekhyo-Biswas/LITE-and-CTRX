inst_vars = {}
temp_vars = {}
code_vars = {}

def get_var(name):
    if name in inst_vars:
        return inst_vars[name]
    elif name in temp_vars:
        return temp_vars[name]
    elif name in code_vars:
        return code_vars[name]
    else:
        raise NameError(f"Variable '{name}' not declared")

def set_var(name, value, var_type='inst'):
    if var_type == 'inst':
        inst_vars[name] = value
    elif var_type == 'temp':
        temp_vars[name] = value
    elif var_type == 'code':
        code_vars[name] = value
    else:
        raise ValueError(f"Unknown variable type '{var_type}'")

def delete_var(name):
    if name in temp_vars:
        del temp_vars[name]
    else:
        raise NameError(f"Temp variable '{name}' cannot be deleted or does not exist")

def eval_expression(expr):
    # Replace variable names with values
    for var in {**inst_vars, **temp_vars, **code_vars}:
        expr = expr.replace(var, str(get_var(var)))
    return eval(expr)

def execute_line(line):
    line = line.strip()
    
    # Variable declarations
    if line.startswith('inst '):
        var, expr = line[5:].split('=', 1)
        var = var.strip()
        value = eval_expression(expr.strip())
        set_var(var, value, 'inst')

    elif line.startswith('temp '):
        var, expr = line[5:].split('=', 1)
        var = var.strip()
        value = eval_expression(expr.strip())
        set_var(var, value, 'temp')

    elif line.startswith('code '):
        var, expr = line[5:].split('=', 1)
        var = var.strip()
        value = eval_expression(expr.strip())
        set_var(var, value, 'code')

    # Delete temp variable
    elif line.startswith('delete '):
        var = line[7:].strip()
        delete_var(var)

    # Print statement
    elif line.startswith('print '):
        expr = line[6:].strip()
        print(eval_expression(expr))

    # Shorthand operators
    else:
        if '+=' in line:
            var, expr = line.split('+=')
            var = var.strip()
            set_var(var, get_var(var) + eval_expression(expr.strip()), 'inst')
        elif '-=' in line:
            var, expr = line.split('-=')
            var = var.strip()
            set_var(var, get_var(var) - eval_expression(expr.strip()), 'inst')
        elif line.endswith('++'):
            var = line[:-2].strip()
            set_var(var, get_var(var) + 1, 'inst')
        elif line.endswith('--'):
            var = line[:-2].strip()
            set_var(var, get_var(var) - 1, 'inst')
        else:
            raise SyntaxError(f"Unknown command: {line}")
