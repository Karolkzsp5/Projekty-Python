import numpy as np

A = np.array([[1, 2], [4, 5], [7, 8]])
B = np.diag([2, 2, 2])
C = np.array([[2, 1, 0], [0, 0, 2]])
D = np.array([[3, 2, 1], [0, 5, 6], [8, -1, 2]])

def can_operate(a, b, op):
    if op in ['+', '-']:
        return a.shape == b.shape
    elif op == '@':
        return a.shape[1] == b.shape[0]
    return True

print("Macierz A:\n", A)
print("\nMacierz B:\n", B)
print("\nMacierz C:\n", C)
print("\nMacierz D:\n", D)

print("\nB + D:\n", B + D if can_operate(B, D, '+') else "Nie można dodać - różne wymiary")
print("\n3A:\n", 3*A)
print("\n-2C:\n", -2*C)
print("\nBA:\n", B @ A if can_operate(B, A, '@') else "Nie można pomnożyć - niezgodne wymiary")
print("\nDB:\n", D @ B)
print("\n2A + B:", "Nie można dodać - różne wymiary (A: 3x2, B: 3x3)")
print("\nCD:\n", C @ D if can_operate(C, D, '@') else "Nie można pomnożyć")
print("\nDC:\n", D @ C if can_operate(D, C, '@') else "Nie można pomnożyć")
print("\nCD - DC:", "Nie można wykonać - różne wymiary wyników" if C.shape != D.shape else C @ D - D @ C)
print("\n2B - D:\n", 2*B - D)
print("\nDD:\n", D @ D)
print("\nBB + DD:\n", B @ B + D @ D)
print("\n4A:\n", 4*A)
print("\nAB:", "Nie można pomnożyć - niezgodne wymiary (A: 3x2, B: 3x3)")
print("\nB^2:\n", B @ B)
print("\nA^2:", "Nie można - macierz niekwadratowa")
print("\nC/C:\n", C/C)