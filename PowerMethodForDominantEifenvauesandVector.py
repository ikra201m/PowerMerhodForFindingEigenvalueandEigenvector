def power_method():
    A = [
        [-4.0, 14.0, 0.0],
        [-5.0, 13.0, 0.0],
        [-1.0, 0.0, 2.0],
    ]
    X = [1.0, 1.0, 1.0]

    lamda = 0.0
    pre_lamda = 0.0

    print(f"{'step':>4} {'eigenvalue':>10}   {'eigenvector'}")

    for i in range(1, 21):
        # Y = A * X
        Y = [sum(A[row][col] * X[col] for col in range(3)) for row in range(3)]

        #
        lamda = max(abs(val) for val in Y)

        # 
        X = [val / lamda for val in Y]

        print(f"{i:4d}{lamda:11.4f}   [{X[0]:7.4f}, {X[1]:7.4f}, {X[2]:7.4f}]")

        if abs(pre_lamda - lamda) < 1e-6:
            break

        pre_lamda = lamda


if __name__ == "__main__":
    power_method()