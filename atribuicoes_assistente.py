"""Interface entre o main.py e o grafo (operações do(a) assistente)."""
import atribuicoes_diretor as diretor
from atribuicoes_secretario import ARQUIVO_CIDADES
from grafo import Grafo

CIDADE_ESCOLA = "Guarujá"
CIDADE_INTERMEDIARIA = "Indaiatuba"

_grafo = None


def iniciar():
    """Monta o grafo a partir do cidades_vizinhas.csv."""
    global _grafo
    _grafo = Grafo.a_partir_do_csv(ARQUIVO_CIDADES)


def _pessoa(nome):
    return diretor.obter_arvore().buscar(nome)


def menor_caminho_ate_pessoa(nome):
    """Opção 1. Retorna None se a pessoa não existe; senão (dados, caminho, custo)."""
    pessoa = _pessoa(nome)
    if pessoa is None:
        return None
    caminho, custo = _grafo.menor_caminho(CIDADE_ESCOLA, pessoa.cidade)
    return str(pessoa), caminho, custo


def menor_caminho_via_intermediaria(nome):
    """Opção 2: escola -> Indaiatuba -> cidade da pessoa."""
    pessoa = _pessoa(nome)
    if pessoa is None:
        return None
    ida, custo_ida = _grafo.menor_caminho(CIDADE_ESCOLA, CIDADE_INTERMEDIARIA)
    volta, custo_volta = _grafo.menor_caminho(CIDADE_INTERMEDIARIA, pessoa.cidade)
    if ida is None or volta is None:
        return str(pessoa), None, None
    # junta os dois trechos sem repetir Indaiatuba no meio
    return str(pessoa), ida + volta[1:], custo_ida + custo_volta


def cidade_mais_proxima_com_moradores():
    """Opção 3. Retorna None se a lista está vazia; senão (cidade, distância, [moradores])."""
    pessoas = list(diretor.obter_arvore().em_ordem())
    if not pessoas:
        return None
    distancias, _ = _grafo.dijkstra(CIDADE_ESCOLA)
    cidades = {p.cidade for p in pessoas}
    melhor = min(sorted(cidades), key=lambda c: distancias.get(c, float("inf")))
    moradores = [str(p) for p in pessoas if p.cidade == melhor]
    return melhor, distancias[melhor], moradores
