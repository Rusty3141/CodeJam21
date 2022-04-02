def reversort(L):
    total = 0
    for i in range(0, len(L) - 1):
        j = L.index(min(L[i:]))
        a = L[:max(0, i)]
        b = L[i:j+1][::-1]
        c = L[j+1:]
        total += j - i + 1
        L = a + b + c
    return total


def main():
    numCases = int(input())
    N, L = [], []
    for case in range(numCases):
        N.append(int(input()))
        L.append([int(x)
                 for x in input().strip().replace("\n", "").split(" ")])

    for i, x in enumerate(L):
        print(f"Case #{i+1}: {reversort(x)}")


if __name__ == "__main__":
    main()
