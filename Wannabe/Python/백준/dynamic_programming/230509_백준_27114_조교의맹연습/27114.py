import sys

si = sys.stdin.readline


def make_pool(l, r, b):
    cand = [(l * 4, 4), (r * 4, 4), (b * 2, 2), (l + r, 2), (l * 2 + b, 3), (r * 2 + b, 3)]
    return cand


if __name__ == "__main__":
    A, B, C, K = map(int, si().split())
    INF = int(1e10)
    dp = [INF] * 1000001
    dp[0] = 0

    pool = make_pool(A, B, C)

    for cost, step in pool:
        if cost < len(dp):
            dp[cost] = step

    for i in range(max(map(lambda x: x[0], pool)), K + 1):
        for cost, step in pool:
            if i >= cost:
                dp[i] = min(dp[i - cost] + step, dp[i])

    if dp[K] < INF:
        print(dp[K])
    else:
        print(-1)
