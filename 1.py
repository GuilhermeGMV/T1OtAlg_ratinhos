def melhor_caminho(lab, n, c, l=0, p=0, m=float('-inf')):
    p = p + lab[c][l]

    # ne
    if c > 0 and l < n - 1:
        m = melhor_caminho(lab, n, c - 1, l + 1, p - 10, m)
    # n
    if c > 0:
        m = melhor_caminho(lab, n, c - 1, l, p - 20, m)
    # e
    if l < n - 1:
        m = melhor_caminho(lab, n, c, l + 1, p - 20, m)

    if c == 0 and l == n - 1:
        if m < p:
            return p
    return m


print("Digite o numero do caso de teste(10,20,30,40,50,60,70): ")
caso = input()
with open("caso" + caso + ".txt", "r") as arquivo:
    lines = arquivo.readlines()

n = int(lines[0].strip())

lab = [list(map(int, line.strip().split())) for line in lines[1:]]

print(melhor_caminho(lab, n, n - 1))