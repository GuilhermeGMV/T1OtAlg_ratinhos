print("Digite o numero do caso de teste(10,20,30,40,50,60,70): ")
caso = input()
with open("caso" + caso + ".txt", "r") as arquivo:
    lines = arquivo.readlines()

n = int(lines[0].strip())
lab = [list(map(int, line.strip().split())) for line in lines[1:]]

dp = [[float('-inf')] * n for _ in range(n)]

dp[n-1][0] = lab[n-1][0]


for i in reversed(range(n)):
    for j in range(n):
        atual = dp[i][j]

        # n
        if i > 0:
            dp[i-1][j] = max(dp[i-1][j], atual - 20 + lab[i-1][j])

        # e
        if j < n - 1:
            dp[i][j+1] = max(dp[i][j+1], atual - 20 + lab[i][j+1])

        # ne
        if i > 0 and j < n - 1:
            dp[i-1][j+1] = max(dp[i-1][j+1], atual - 10 + lab[i-1][j+1])

print(dp[0][n-1])
