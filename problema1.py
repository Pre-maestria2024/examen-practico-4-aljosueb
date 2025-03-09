def main():
    m, n = map(int, input().split())
    H = list(map(int, input().split()))
    D = list(map(int, input().split()))

    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(m):
        for j in range(n, -1, -1):
            salud_nueva = min(j + H[i], n)
            dp[salud_nueva] = min(dp[salud_nueva], dp[j] + D[i])

    if dp[n] == float('inf'):
        print(0)
        return

    ganancia_total = sum(D)
    ganancia_final = ganancia_total - dp[n]

    print(ganancia_final)

if __name__ == '__main__':
    main()
