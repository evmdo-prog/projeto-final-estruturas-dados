"""Interface entre o main.py e a árvore binária de busca (operações do(a) diretor(a))."""
import atribuicoes_secretario as secretario
from arvore import ArvoreBinariaBusca, chave_do_nome

_arvore = ArvoreBinariaBusca()


def iniciar():
    """Gera a ABB a partir da lista encadeada do(a) secretário(a)."""
    global _arvore
    _arvore = ArvoreBinariaBusca.a_partir_da_lista(secretario.obter_lista())


def consultar_pessoa(nome):
    """Texto com os dados da pessoa, ou None se não estiver cadastrada."""
    pessoa = _arvore.buscar(nome)
    return str(pessoa) if pessoa is not None else None


def alterar_dados(nome, campo, novo_valor):
    """Altera nome (campo 1), idade (2) ou telefone (3). A cidade nunca é alterada.
    Retorna (sucesso, mensagem_de_erro)."""
    pessoa = _arvore.buscar(nome)
    if pessoa is None:
        return False, "Pessoa não cadastrada."
    if campo == 1:
        existente = _arvore.buscar(novo_valor)
        if existente is not None and existente is not pessoa:
            return False, "Já existe uma pessoa cadastrada com esse nome."
        # o nome é a chave da árvore: remove o nó e reinsere com o nome novo
        _arvore.remover(pessoa.nome)
        pessoa.nome = novo_valor
        _arvore.inserir(pessoa)
    elif campo == 2:
        pessoa.idade = novo_valor
    elif campo == 3:
        pessoa.telefone = novo_valor
    else:
        return False, "Campo inválido."
    return True, ""


def descadastrar(nome):
    """Remove a pessoa da lista de espera (árvore). Retorna True se removeu."""
    return _arvore.remover(nome)


def primeira_pessoa():
    pessoa = _arvore.primeira()
    return str(pessoa) if pessoa is not None else None


def ultima_pessoa():
    pessoa = _arvore.ultima()
    return str(pessoa) if pessoa is not None else None


def obter_arvore():
    """Usada na Etapa 3 (assistente), para que ele enxergue a lista já validada."""
    return _arvore
