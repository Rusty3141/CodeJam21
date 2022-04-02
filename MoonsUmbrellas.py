def cost(xy, pattern):
    return xy['x']*pattern.replace('?', '').count('CJ') + xy['y']*pattern.replace('?', '').count('JC')


def main():
    numCases = int(input())
    xy, patterns = [], []
    for case in range(numCases):
        inp = input().split(" ")
        xy.append({'x': int(inp[0]), 'y': int(inp[1])})
        patterns.append(inp[-1])

    for i in range(numCases):
        print(f"Case #{i+1}: {cost(xy[i], patterns[i])}")


if __name__ == "__main__":
    main()
