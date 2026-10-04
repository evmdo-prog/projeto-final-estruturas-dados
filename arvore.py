"""Árvore binária de busca (ABB) com o nome da pessoa como chave."""
import unicodedata


def chave_do_nome(nome):
    """Chave de comparação: ignora maiúsculas/minúsculas e acentos,
    para que a ordem alfabética fique correta (ex.: 'Álvaro' antes de 'Beto')."""
    sem_acento = unicodedata.normalize("NFD", nome)
    sem_acento = "".join(c for c in sem_acento if unicodedata.category(c) != "Mn")
    return sem_acento.casefold()


class NoArvore:
    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.chave = chave_do_nome(pessoa.nome)
        self.esquerda = None
        self.direita = None


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None
        self.tamanho = 0

    @classmethod
    def a_partir_da_lista(cls, lista):
        """Gera a árvore a partir da lista encadeada (percorrendo-a do início ao fim)."""
        arvore = cls()
        for pessoa in lista:
            arvore.inserir(pessoa)
        return arvore

    def inserir(self, pessoa):
        """Insere a pessoa. Retorna False (sem inserir) se já existir o mesmo nome."""
        novo = NoArvore(pessoa)
        if self.raiz is None:
            self.raiz = novo
            self.tamanho += 1
            return True
        atual = self.raiz
        while True:
            if novo.chave == atual.chave:
                return False
            if novo.chave < atual.chave:
                if atual.esquerda is None:
                    atual.esquerda = novo
                    break
                atual = atual.esquerda
            else:
                if atual.direita is None:
                    atual.direita = novo
                    break
                atual = atual.direita
        self.tamanho += 1
        return True

    def buscar(self, nome):
        """Busca iterativa. Retorna a Pessoa ou None."""
        chave = chave_do_nome(nome)
        atual = self.raiz
        while atual is not None:
            if chave == atual.chave:
                return atual.pessoa
            atual = atual.esquerda if chave < atual.chave else atual.direita
        return None

    def remover(self, nome):
        """Remove a pessoa com esse nome. Retorna True se removeu."""
        antes = self.tamanho
        self.raiz = self._remover(self.raiz, chave_do_nome(nome))
        return self.tamanho < antes

    def _remover(self, no, chave):
        if no is None:
            return None
        if chave < no.chave:
            no.esquerda = self._remover(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self._remover(no.direita, chave)
        else:
            self.tamanho -= 1
            if no.esquerda is None:
                return no.direita
            if no.direita is None:
                return no.esquerda
            # dois filhos: o sucessor (menor da subárvore direita) ocupa o lugar do nó
            sucessor = no.direita
            while sucessor.esquerda is not None:
                sucessor = sucessor.esquerda
            no.pessoa, no.chave = sucessor.pessoa, sucessor.chave
            self.tamanho += 1  # compensa: a chamada abaixo remove o sucessor e decrementa
            no.direita = self._remover(no.direita, sucessor.chave)
        return no

    def primeira(self):
        """Pessoa com o primeiro nome em ordem alfabética (nó mais à esquerda)."""
        if self.raiz is None:
            return None
        atual = self.raiz
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.pessoa

    def ultima(self):
        """Pessoa com o último nome em ordem alfabética (nó mais à direita)."""
        if self.raiz is None:
            return None
        atual = self.raiz
        while atual.direita is not None:
            atual = atual.direita
        return atual.pessoa

    def em_ordem(self):
        """Gera as pessoas em ordem alfabética (percurso em ordem, iterativo)."""
        pilha, atual = [], self.raiz
        while pilha or atual is not None:
            while atual is not None:
                pilha.append(atual)
                atual = atual.esquerda
            atual = pilha.pop()
            yield atual.pessoa
            atual = atual.direita

    def __len__(self):
        return self.tamanho
