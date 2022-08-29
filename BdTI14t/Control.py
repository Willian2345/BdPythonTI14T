from Model import Model

class Control:
    def __init__(self):
        self.opcao = -1
        self.modelo = Model()

    def getOpcao(self):
        return self.opcao

    def setOpcao(self,opcao):
      self.opcao = opcao

    def menu(self):
        print("Escolha uma das opções abaixo:  \n" +
              "0. Sair \n"                          +
              "1. Cadastrar \n"                     +
              "2. Consultar \n"                     +
              "3. Atualizar \n"                     +
              "4. Excluir")
        self.setOpcao(int(input()))

    def operacoes(self):
      while self.getOpcao() != 0:
            self.menu()
            if self.getOpcao == 0:
                print("Obrigado!")
            elif self.getOpcao() == 1:
                self.cadastrar()
            elif self.getOpcao() == 2:
              print(self.modelo.selecionar())
            else:
                print("Opção escolhida inválida! Tente Novamente!")




    def cadastrar(self):
        print("informe seu nome: ")
        nome = input()
        print("informe seu telefone: ")
        telefone = input()
        print("informe seu endereço: ")
        endereco = input()
        print("informe sua data de nascimento: ")
        dataDeNascimento = input()
        print(self.modelo.inserir(nome, telefone, endereco, self.transformarData(dataDeNascimento)))

    def transformarData(self, texto):
        separado = texto.split('/')
        dia = separado[0]
        mes = separado[1]
        ano = separado[2]
        return "{}-{}-{}".format (ano, mes, dia)




