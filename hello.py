rule =[[0,2,1],[1,0,2],[2,1,0]]
check=["hoa","thang","thua"]
p1 = int(input("p1:= "))
p2 = int(input("p2:= "))
checkResult = rule[p1][p2]
print(check[checkResult])