
#  desarrolle un algoritmo que muestre el siguiente patron: 

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

n = int(input("introduce el numero de filas"))
for i in range(1, n+1) :
    for j in range(1, i+1) :
        print(i, end = " ")
    print("")

for i in range(6):
    print(str(i)     *1)