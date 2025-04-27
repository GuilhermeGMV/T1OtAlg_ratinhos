def melhor_caminho(lab, n, c, l=0, memo=None):
    if memo is None:
        memo = {}

    chave = (c, l)

    if chave in memo:
        return memo[chave]


    if c == 0 and l == n - 1:
        memo[chave] = (lab[c][l], [])
        return memo[chave]

    melhores = []

    # NE
    if c > 0 and l < n - 1:
        pontuacao, caminho = melhor_caminho(lab, n, c - 1, l + 1, memo)
        melhores.append((pontuacao - 10, ['NE'] + caminho))

    # N
    if c > 0:
        pontuacao, caminho = melhor_caminho(lab, n, c - 1, l, memo)
        melhores.append((pontuacao - 20, ['N'] + caminho))

    # E
    if l < n - 1:
        pontuacao, caminho = melhor_caminho(lab, n, c, l + 1, memo)
        melhores.append((pontuacao - 20, ['E'] + caminho))

    melhor_pontuacao, melhor_caminho_percorrido = max(melhores, key=lambda x: x[0])
    melhor_pontuacao += lab[c][l]
    memo[chave] = (melhor_pontuacao, melhor_caminho_percorrido)
    return memo[chave]

print("Digite o número do caso de teste (10, 20, 30, 40, 50, 60, 70): ")
caso = input()

with open("caso" + caso + ".txt", "r") as arquivo:
    lines = arquivo.readlines()

n = int(lines[0].strip())
lab = [list(map(int, line.strip().split())) for line in lines[1:]]

melhor_pontuacao, caminho = melhor_caminho(lab, n, n - 1)

print("Melhor pontuação:", melhor_pontuacao)
print("Caminho percorrido:", caminho)
