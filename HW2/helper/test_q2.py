import json
import os
import numpy as np

BASE_PATH = '.'
INPUTS_PATH = os.path.join(BASE_PATH, 'inputs')
OUTPUT_PATH = os.path.join(BASE_PATH, 'outputs')


def get_all_tests(prefix):
    test_files = [f for f in os.listdir(INPUTS_PATH) if os.path.isfile(os.path.join(INPUTS_PATH, f))]
    return list(filter(lambda f: f.startswith(prefix), test_files))


def scan_test_input(test):
    with open(os.path.join(INPUTS_PATH, test), 'r') as f:
        test_lines = f.readlines()
    base = int(test_lines[0].strip())
    result = test_lines[-1].strip().lower()
    operands = test_lines[1:-1]
    operands = [op.strip().lower() for op in operands]

    return base, operands, result


def _clean_result(result):
    return ' '.join(map(str, result)) if ' ' not in result else result


def is_result_valid(sol: dict[str, int], operands: list[str], result: str, base: int = 10):
    if len(sol.keys()) != len(set(sol.values())):
        return False
    for op in operands:
        if op[0] not in sol or sol[op[0]] == 0:
            return False
    if result[0] not in sol or sol[result[0]] == 0:
        return False
    expr = ' + '.join(['INT("' + op + '", ' + str(base) + ')' for op in operands])
    expr += ' == INT("' + result + '", ' + str(base) + ')'
    for var in sol:
        expr = expr.replace(var, np.base_repr(sol[var], base))
    expr = expr.lower()
    return eval(expr)

