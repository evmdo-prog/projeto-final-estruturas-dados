"""Interface entre o main.py e a lista encadeada (operações do(a) secretário(a))."""
import csv
import os
import random

from lista_encadeada import ListaEncadeada, Pessoa

ARQUIVO_CIDADES = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "cidades_vizinhas.csv")

_lista = ListaEncadeada()
_cidades = None


def _carregar_cidades():
    """Lê as cidades das duas primeiras colunas do CSV (sem repetição)."""
    global _cidades
    if _cidades is None:
        vistas = []
        conjunto = set()
        with open(ARQUIVO_CIDADES, encoding="utf-8", newline="") as f:
            for linha in csv.reader(f, delimiter=";"):
                if len(linha) < 2:
                    continue
                for cidade in (linha[0].strip(), linha[1].strip()):
                    if cidade and cidade not in conjunto:
                        conjunto.add(cidade)
                        vistas.append(cidade)
        _cidades = vistas
    return _cidades


def cadastrar_pessoa(nome, idade, telefone):
    """Cadastra a pessoa com cidade aleatória. Retorna a lista (textos) após a inclusão."""
    cidade = random.choice(_carregar_cidades())
    _lista.inserir_no_fim(Pessoa(nome, idade, telefone, cidade))
    return listar_pessoas()


def listar_pessoas():
    return [str(p) for p in _lista]


def consultar_pessoa(nome):
    """Retorna o texto com os dados da pessoa, ou None se não estiver cadastrada."""
    pessoa = _lista.buscar_por_nome(nome)
    return str(pessoa) if pessoa is not None else None


def quantidade_pessoas():
    return len(_lista)


def obter_lista():
    """Usada nas próximas etapas (diretor) para gerar a árvore a partir da lista."""
    return _lista
