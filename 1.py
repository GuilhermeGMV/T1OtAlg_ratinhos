def melhor_caminho(lab, n, c, l=0, p=0):
    p += lab[c][l]

    if c == 0 and l == n - 1:
        return p, []

    melhores = []

    # NE
    if c > 0 and l < n - 1:
        pontuacao, caminho = melhor_caminho(lab, n, c - 1, l + 1, p - 10)
        melhores.append((pontuacao, ['NE'] + caminho))

    # N
    if c > 0:
        pontuacao, caminho = melhor_caminho(lab, n, c - 1, l, p - 20)
        melhores.append((pontuacao, ['N'] + caminho))

    # E
    if l < n - 1:
        pontuacao, caminho = melhor_caminho(lab, n, c, l + 1, p - 20)
        melhores.append((pontuacao, ['E'] + caminho))


    melhor_pontuacao, melhor_caminho_percorrido = max(melhores, key=lambda x: x[0])
    return melhor_pontuacao, melhor_caminho_percorrido

print("Digite o número do caso de teste (10, 20, 30, 40, 50, 60, 70): ")
caso = input()

with open("caso" + caso + ".txt", "r") as arquivo:
    lines = arquivo.readlines()

n = int(lines[0].strip())
lab = [list(map(int, line.strip().split())) for line in lines[1:]]

melhor_pontuacao, caminho = melhor_caminho(lab, n, n - 1)

print("Melhor pontuação:", melhor_pontuacao)
print("Caminho percorrido:", caminho)
