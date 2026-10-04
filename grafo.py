"""Grafo ponderado e não-direcionado (lista de adjacência) com Dijkstra."""
import csv
import heapq


class Grafo:
    def __init__(self):
        self.adjacencia = {}  # cidade -> {vizinha: distância}

    def adicionar_aresta(self, a, b, distancia):
        # não-direcionado: a aresta vale nos dois sentidos.
        # Usar dicionário evita arestas duplicadas (o CSV repete alguns pares).
        self.adjacencia.setdefault(a, {})
        self.adjacencia.setdefault(b, {})
        if b not in self.adjacencia[a] or distancia < self.adjacencia[a][b]:
            self.adjacencia[a][b] = distancia
            self.adjacencia[b][a] = distancia

    @classmethod
    def a_partir_do_csv(cls, caminho_arquivo):
        grafo = cls()
        with open(caminho_arquivo, encoding="utf-8", newline="") as f:
            for linha in csv.reader(f, delimiter=";"):
                if len(linha) < 3:
                    continue
                grafo.adicionar_aresta(linha[0].strip(), linha[1].strip(), int(linha[2]))
        return grafo

    def dijkstra(self, origem):
        """Menores distâncias de 'origem' para todas as cidades.
        Retorna (distancias, anteriores) para reconstruir os caminhos."""
        distancias = {origem: 0}
        anteriores = {}
        fila = [(0, origem)]
        while fila:
            dist, cidade = heapq.heappop(fila)
            if dist > distancias.get(cidade, float("inf")):
                continue  # entrada antiga da fila
            for vizinha, peso in self.adjacencia[cidade].items():
                nova = dist + peso
                if nova < distancias.get(vizinha, float("inf")):
                    distancias[vizinha] = nova
                    anteriores[vizinha] = cidade
                    heapq.heappush(fila, (nova, vizinha))
        return distancias, anteriores

    def menor_caminho(self, origem, destino):
        """Retorna (lista_de_cidades, custo), ou (None, None) se não houver caminho."""
        if origem not in self.adjacencia or destino not in self.adjacencia:
            return None, None
        distancias, anteriores = self.dijkstra(origem)
        if destino not in distancias:
            return None, None
        caminho = [destino]
        while caminho[-1] != origem:
            caminho.append(anteriores[caminho[-1]])
        caminho.reverse()
        return caminho, distancias[destino]
