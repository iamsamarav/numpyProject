import numpy as np

data8 = [1,2,3,4,5,6,7,8]
data8 = np.array(data8)
print(data8+10)

#matriz diagonal

data8 = np.diag(data8)
print(data8)

data9 = np.eye(4)
print(data9)

#repetição de valores

data10 = np.tile(np.array([[2,8],[2,12]]), 3)
print(data10)

data11 = np.tile(np.array([[2,2],[9,12]]), [3,2])
print(data11)

#Somando um valor a cada elemento da array

data12 = np.arange(0,30,3)+3
print(data12)

#Soma de arrays