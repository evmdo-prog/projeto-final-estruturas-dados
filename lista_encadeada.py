"""Lista encadeada simples usada pelo(a) secretário(a)."""


class Pessoa:
    def __init__(self, nome, idade, telefone, cidade):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cidade = cidade

    def __str__(self):
        return (f"Nome: {self.nome} | Idade: {self.idade} | "
                f"Telefone: {self.telefone} | Cidade: {self.cidade}")


class No:
    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def inserir_no_fim(self, pessoa):
        """Insere no fim em O(1), mantendo a ordem de cadastro."""
        novo = No(pessoa)
        if self.inicio is None:
            self.inicio = novo
        else:
            self.fim.proximo = novo
        self.fim = novo
        self.tamanho += 1

    def buscar_por_nome(self, nome):
        """Retorna a Pessoa com esse nome, ou None se não existir."""
        atual = self.inicio
        while atual is not None:
            if atual.pessoa.nome == nome:
                return atual.pessoa
            atual = atual.proximo
        return None

    def __len__(self):
        return self.tamanho

    def __iter__(self):
        atual = self.inicio
        while atual is not None:
            yield atual.pessoa
            atual = atual.proximo
