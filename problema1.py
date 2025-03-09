def main():
    m, n = map(int, input().split())
    H = list(map(int, input().split()))
    D = list(map(int, input().split()))

    ganancia_total = 0
    comida_usada = -1

    for i in range(m):
        if H[i] == n:
            comida_usada = i
            break

    for i in range(m):
        if i != comida_usada:
            ganancia_total += D[i]

    print(ganancia_total)

if __name__ == '__main__':
    main()
