import random
rule =[[0,1,2],[1,0,2],[2,1,0]]
choice = ["keo","bua","bao"]
isWin=["hoa","thua","thang"]
num = random.randint(0,2)
player = int(input("0: keo 1: bua 2: bao "))
print(choice[player]+" vs "+ choice[num])
print(isWin[rule[player][num]])
