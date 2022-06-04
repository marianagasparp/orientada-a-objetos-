from abc import ABC, abstractmethod


class Vendedor(ABC):
    def __init__(self, codigo:int, nome:str):
        
        self.__codigo = codigo
        self.__nome = nome
        self.__vendas = []

    def getcodigo(self):
        return self.__codigo
        
    def getnome(self):
        return self.__nome

    def getVendas(self):
        return self.__vendas

    def addVenda(self, codigo, mes, ano, valor):
        venda = Venda(codigo, mes, ano, valor)
        self.__vendas.append(venda)
    
    @abstractmethod
    def getDados(self):
        pass

    @abstractmethod
    def calculaRenda(mes, ano):
        pass


class Venda():
    def __init__(self, codigo:int, mes:int, ano:int, valor:float):
        self.__codigo = codigo
        self.__mes = mes
        self.__ano = ano
        self.__valor = valor

    def getCodImovel(self):
        return self.__codigo

    def getMesVenda(self):
        return self.__mes

    def getAnoVenda(self):
        return self.__ano
    
    def getValorVenda(self):
        return self.__valor

class Contratado(Vendedor):
    def __init__(self, codigo ,nome, salario:float, NroCartTrabalho:str):
        super().__init__(codigo, nome)
        self.__salario = salario
        self.__NroCartTrabalho = NroCartTrabalho
        self.__comissao = float(0.01)
        int(codigo)
       
    def getNroCartTrabalho(self):
        return self.__NroCartTrabalho

    def getSalarioFixo(self):
        return self.__salario
    
    def getDados(self):
        return "Nome " + self.getnome() + "- Nro Carteira:"+ str(self.getNroCartTrabalho())

    def calculaRenda(self, mes, ano):
        vendas = self.getVendas()
        comissaoMes = 0
         
        for venda in vendas:
            if (venda.getMesVenda() == mes and venda.getAnoVenda() == ano):
                comissaoMes += (venda.getValorVenda() * self.__comissao )
        return comissaoMes + self.__salario

class Comissionado(Vendedor):
    def __init__(self, codigo:int, nome:str, NroCPF:int, comissao:float):
        super().__init__(codigo, nome)
        self.__NroCPF = NroCPF
        self.__comissao = comissao 
        
    def getNroCPF(self):
        return self.__NroCPF
    
    def getComissao(self):
        return self.__comissao


    def getDados(self):
        return "Nome " + self.getnome() + "- CPF:"+ str(self.getNroCPF())

    
    def calculaRenda(self, mes:int, ano:int):
        vendas = self.getVendas()
        comissaoMes = 0

        for venda in vendas:
            if (venda.getMesVenda() == mes and venda.getAnoVenda() == ano):
                comissaoMes += (venda.getValorVenda() * self.__comissao/100 )
        return comissaoMes



if __name__ == "__main__":
    funcContratado = Contratado(1001, 'João da Silva', 2000, 1234)
    funcContratado.addVenda(100, 3, 2022, 200000)
    funcContratado.addVenda(101, 3, 2022, 300000)
    funcContratado.addVenda(102, 4, 2022, 600000)
    funcComissionado = Comissionado(1002, 'José Santos', 4321, 5)
    funcComissionado.addVenda(200, 3, 2022, 200000)
    funcComissionado.addVenda(201, 3, 2022, 400000)
    funcComissionado.addVenda(202, 4, 2022, 500000)
    listaFunc = {funcContratado, funcComissionado}
    for func in listaFunc:
        print (func.getDados())
        print ("Renda no mês 3 de 2022: ")
        print (func.calculaRenda(3, 2022))

    