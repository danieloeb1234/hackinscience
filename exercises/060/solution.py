import operator
A = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
     "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for i in range(26):
    for j in range(26):
        print(operator.add(A[i], A[j]))
