
#  desarrolle un algoritmo que muestre el siguiente patron: 

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

n = int(input("introduce los numeros: "))
for a in range (1, n+1, 2):
    for b in range(a, 0, -2):
        print(b, end=" ")
        print(" ")
             