import sys
sys.path.append("D:\Escuelita")

import Tarea4 as t

#Gafo simples
#instancia 1
grafo1={
    "A": {"B": 1, "C": 2, "D": 3},
    "B": {"C": 4},
    "C": {"D": 5}
}
print("Instancia 1:")
print(t.ruta_mas_corta("A", "D", grafo1))


#instancia 2
grafo2={
    1: {2: 4, 3: 5},
    2: {3: 11, 4: 9, 5: 7},
    3: {5: 3},
    4: {5: 13, 6: 2},
    5: {6: 6}
}
print("Instancia 2:")
print(t.ruta_mas_corta(1, 6, grafo2))


#instancia 3
grafo3={
    1: {2: 4, 5: 10},
    2: {3: 8, 5: 11},
    3: {4: 7, 7: 4, 9:2},
    4: {7: 14, 8: 9},
    5: {6: 1, 9: 7},
    6: {7: 2},
    7: {8: 10}
}
print("Instancia 3:")
print(t.ruta_mas_corta(1,9, grafo3))


#instancia 4
grafo4={
    1: {2:3, 3:4, 4:5, 5:6},
    2: {3:4, 7:2, 6:5},
    3: {4:4, 7:1, 8:3, 9:3},
    4: {5:7, 9:1, 10:3, 11:1},
    5: {11:2},
    6: {7:2, 12:8},
    7: {8:4, 9:6, 12:4},
    8: {9:9, 12:4, 14:1},
    9: {10:4, 14:1, 15:4},
    10: {11:3, 15:9, 16:9},
    11: {16:10},
    12: {13:9, 17:4},
    13: {14:2, 17:3, 18:3},
    14: {15:3},
    15: {16:3},
    16: {18:5},
    17: {18:2},
    18: {20:7},
    19: {20:4}
}
print("Instancia 4:")
print(t.ruta_mas_corta(1, 20, grafo4))