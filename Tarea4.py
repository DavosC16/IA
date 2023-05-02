from queue import Queue

def ruta_mas_corta(inicio, destino, grafo):
    visitados = set()
    cola = Queue()
    cola.put((inicio, 0))

    while not cola.empty():
        nodo, distancia = cola.get()

        if nodo == destino:
            return distancia

        if nodo in visitados:
            continue

        visitados.add(nodo)

        for vecino, peso in grafo[nodo].items():
            cola.put((vecino, distancia + peso))

    return None