"""Interface com o usuário. Não acessa lista, árvore ou grafo diretamente."""
import atribuicoes_secretario as secretario
import atribuicoes_diretor as diretor
import atribuicoes_assistente as assistente


def ler_inteiro(mensagem):
    """Repete a leitura até o usuário digitar um número inteiro."""
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def menu_secretario():
    print("-------------- Olá, Secretário(a)! --------------")
    while True:
        print()
        print("Você deseja:")
        print("(1) Cadastrar nova pessoa na lista de espera.")
        print("(2) Consultar pessoa cadastrada.")
        print("(3) Ver quantidade de pessoas cadastradas.")
        print("(4) Finalizar execução.")
        opcao = input("Digite sua opção: ").strip()

        if opcao == "1":
            nome = input("Digite o nome da pessoa: ").strip()
            idade = ler_inteiro("Digite a idade: ")
            telefone = input("Digite o telefone: ").strip()
            for linha in secretario.cadastrar_pessoa(nome, idade, telefone):
                print(linha)
        elif opcao == "2":
            nome = input("Digite o nome da pessoa: ").strip()
            dados = secretario.consultar_pessoa(nome)
            if dados is None:
                print("Pessoa não cadastrada. Tem certeza que o nome está certo?")
            else:
                print(dados)
        elif opcao == "3":
            print(f"São {secretario.quantidade_pessoas()} pessoas na lista de espera.")
        elif opcao == "4":
            print("Fim das atividades sob responsabilidade do(a) Secretário(a).")
            break
        else:
            print("Opção inválida. Digite um número de 1 a 4.")


def menu_diretor():
    diretor.iniciar()  # gera a árvore binária de busca a partir da lista encadeada
    print("\n\n-------------- Olá, Diretor(a)! --------------")
    while True:
        print()
        print("Você deseja:")
        print("(1) Alterar nome, idade ou telefone de pessoa cadastrada.")
        print("(2) Descadastrar pessoa.")
        print("(3) Obter informações da primeira pessoa em ordem alfabética de nome.")
        print("(4) Obter informações da última pessoa em ordem alfabética de nome.")
        print("(5) Confirmar validade da lista de espera e finalizar execução.")
        opcao = input("Digite sua opção: ").strip()

        if opcao == "1":
            nome = input("Digite o nome da pessoa que você quer editar: ").strip()
            dados = diretor.consultar_pessoa(nome)
            if dados is None:
                print("Pessoa não cadastrada. Tem certeza que o nome está certo?")
                continue
            print(dados)
            while True:
                campo = input("O que você quer editar? Digite 1 para nome, "
                              "2 para idade ou 3 para telefone: ").strip()
                if campo in ("1", "2", "3"):
                    break
                print("Opção inválida. Digite 1, 2 ou 3.")
            if campo == "1":
                novo = input("Digite o novo nome: ").strip()
            elif campo == "2":
                novo = ler_inteiro("Digite a nova idade: ")
            else:
                novo = input("Digite o novo telefone: ").strip()
            sucesso, erro = diretor.alterar_dados(nome, int(campo), novo)
            print("Dados atualizados com sucesso." if sucesso else erro)
        elif opcao == "2":
            nome = input("Digite o nome da pessoa que você quer descadastrar: ").strip()
            dados = diretor.consultar_pessoa(nome)
            if dados is None:
                print("Pessoa não cadastrada ou lista de espera vazia. "
                      "Tem certeza que o nome da pessoa está certo?")
                continue
            print(dados)
            while True:
                resposta = input(f"Tem certeza que deseja descadastrar {nome}? "
                                 "Digite S ou N: ").strip().upper()
                if resposta in ("S", "N"):
                    break
                print("Opção inválida. Digite S ou N.")
            if resposta == "S":
                diretor.descadastrar(nome)
                print(f"{nome} descadastrado com sucesso.")
            else:
                print("Descadastro cancelado.")
        elif opcao == "3":
            dados = diretor.primeira_pessoa()
            print(dados if dados is not None else "Lista de espera vazia.")
        elif opcao == "4":
            dados = diretor.ultima_pessoa()
            print(dados if dados is not None else "Lista de espera vazia.")
        elif opcao == "5":
            print("Fim das atividades sob responsabilidade do(a) Diretor(a).")
            break
        else:
            print("Opção inválida. Digite um número de 1 a 5.")


def menu_assistente():
    assistente.iniciar()  # monta o grafo a partir do cidades_vizinhas.csv
    print("\n\n-------------- Olá, Assistente! --------------")
    while True:
        print()
        print("Você deseja:")
        print("(1) Ver a menor distância entre a cidade da escola e a cidade de uma pessoa.")
        print("(2) Ver a menor distância da cidade da escola até a cidade da pessoa "
              "passando por uma cidade específica.")
        print("(3) Ver dados da(s) pessoa(s) que mora(m) na cidade mais perto da cidade "
              "da escola (incluindo distância).")
        print("(4) Finalizar execução.")
        opcao = input("Digite sua opção: ").strip()

        if opcao in ("1", "2"):
            nome = input("Digite o nome da pessoa cuja cidade te interessa: ").strip()
            if opcao == "1":
                resultado = assistente.menor_caminho_ate_pessoa(nome)
            else:
                resultado = assistente.menor_caminho_via_intermediaria(nome)
            if resultado is None:
                print("Pessoa não cadastrada ou lista de espera vazia. "
                      "Tem certeza que o nome da pessoa está certo?")
                continue
            dados, caminho, custo = resultado
            print(dados)
            if caminho is None:
                print("Não existe caminho entre as cidades.")
            else:
                print(f"Menor caminho = {caminho} com custo {custo}")
        elif opcao == "3":
            resultado = assistente.cidade_mais_proxima_com_moradores()
            if resultado is None:
                print("Lista de espera vazia.")
                continue
            cidade, distancia, moradores = resultado
            print("A cidade mais próxima à cidade da escola que tem moradores na lista "
                  f"de espera (ver abaixo) é {cidade}. Distância = {distancia}")
            for linha in moradores:
                print(linha)
        elif opcao == "4":
            print("Fim das atividades sob responsabilidade do(a) Assistente.")
            break
        else:
            print("Opção inválida. Digite um número de 1 a 4.")


def main():
    menu_secretario()
    menu_diretor()
    menu_assistente()


if __name__ == "__main__":
    main()
