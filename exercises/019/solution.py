import operator
import sys
if len(sys.argv) <= 2:
    print("usage: python3 solution.py OP1 OP2")
else:
    print(operator.add(int(sys.argv[1]), int(sys.argv[2])))
