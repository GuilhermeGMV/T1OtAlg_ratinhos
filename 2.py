def melhor_caminho(lab, n, c, l=0, p=0, m=float('-inf'), memo=None):
    if memo is None:
        memo = {}

    chave = (c, l, p)

    if chave in memo:
        return memo[chave]

    p += lab[c][l]

    if c == 0 and l == n - 1:
        if p > m:
            memo[chave] = p
            return p
        else:
            memo[chave] = m
            return m

    caminhos = []

    # ne
    if c > 0 and l < n - 1:
        caminhos.append(melhor_caminho(lab, n, c - 1, l + 1, p - 10, m, memo))
    # n
    if c > 0:
        caminhos.append(melhor_caminho(lab, n, c - 1, l, p - 20, m, memo))
    # e
    if l < n - 1:
        caminhos.append(melhor_caminho(lab, n, c, l + 1, p - 20, m, memo))

    m = max(caminhos, default=m)
    memo[chave] = m
    return m


print("Digite o numero do caso de teste(10,20,30,40,50,60,70): ")
caso = input()
with open("caso"+caso+".txt", "r") as arquivo:
    lines = arquivo.readlines()

n = int(lines[0].strip())

lab = [list(map(int, line.strip().split())) for line in lines[1:]]


print(melhor_caminho(lab, n, n-1))