print("Digite o numero do caso de teste(10,20,30,40,50,60,70): ")
caso = input()
with open("caso" + caso + ".txt", "r") as arquivo:
    lines = arquivo.readlines()

n = int(lines[0].strip())
lab = [list(map(int, line.strip().split())) for line in lines[1:]]

m = [[float('-inf')] * n for _ in range(n)]

caminho = [[None] * n for _ in range(n)]

m[n-1][0] = lab[n-1][0]


for i in reversed(range(n)):
    for j in range(n):
        atual = m[i][j]

        # n
        if i > 0:
            novo_valor = atual - 20 + lab[i - 1][j]
            if novo_valor > m[i - 1][j]:
                m[i - 1][j] = novo_valor
                caminho[i - 1][j] = 'N'

        # e
        if j < n - 1:
            novo_valor = atual - 20 + lab[i][j + 1]
            if novo_valor > m[i][j + 1]:
                m[i][j + 1] = novo_valor
                caminho[i][j + 1] = 'E'

        # ne
        if i > 0 and j < n - 1:
            novo_valor = atual - 10 + lab[i - 1][j + 1]
            if novo_valor > m[i - 1][j + 1]:
                m[i - 1][j + 1] = novo_valor
                caminho[i - 1][j + 1] = 'NE'

print("Melhor pontuação:", m[0][n-1])

i, j = 0, n-1
caminho_percorrido = []

while not (i == n-1 and j == 0):
    mov = caminho[i][j]
    caminho_percorrido.append(mov)

    if mov == 'N':
        i += 1
    elif mov == 'E':
        j -= 1
    elif mov == 'NE':
        i += 1
        j -= 1
    else:
        break

caminho_percorrido.reverse()

print("Caminho percorrido:", caminho_percorrido)