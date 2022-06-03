from abc import ABC, abstractmethod

class EmpDomestica(ABC):
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    def getNome(self):
        return self.__nome

    def gettelefone(self):
        return self.__telefone

    @abstractmethod
    def getSalario(self):
        pass

class Mensalista(EmpDomestica):
    def __init__(self, nome, telefone, salario):
        super().__init__(nome, telefone)
        self.__salario = salario

    def getSalario(self):
        return self.__salario

class Horista(EmpDomestica):
    def __init__(self, nome, telefone, salarioHora,horasTrabalhadas):
        super().__init__(nome, telefone)
        self.__salarioHora = salarioHora
        self.__horasTrabalhadas = horasTrabalhadas

    def getSalarioHora(self):
        return self.__salarioHora
    
    def gethorasTrabalhadas(self):
        return self.__horasTrabalhadas


    def getSalario(self):
        return self.__salarioHora * self.__horasTrabalhadas

class Diarista(EmpDomestica):
    def __init__(self, nome, telefone, salarioDia, diasTrabalhados):
        super().__init__(nome, telefone)
        self.__salarioDia = salarioDia
        self.__diasTrabalhados = diasTrabalhados

    def getSalarioDia(self):
        return self.__salarioHora
    
    def getdiasTrabalhados(self):
        return self.__diasTrabalhados

    def getSalario(self):
        return self.__salarioDia * self.__diasTrabalhados
        




if __name__ == "__main__":
    emp1 = Horista('Maria', 12345, 160 , 10)
    emp2 = Mensalista('Betania', 54321, 1000)
    emp3 = Diarista('Ana', 56789, 55, 20)
    emps = [emp1, emp2, emp3]
    menor=emp1
    for emp in emps:
        print ('Nome: {} - Salário: {}'.format(emp.getNome(), emp.getSalario()))
        if emp.getSalario() < menor.getSalario():
            menor = emp 
    print()
    print ('Menor salario: {} - {}'.format(menor.getNome(), menor.getSalario()))

    
    


