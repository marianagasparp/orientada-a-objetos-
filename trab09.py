from abc import ABC, abstractmethod


class idadeInvalida(Exception):
    pass
class cursoInvalido(Exception):
    pass
class titulacaoInvalida(Exception):
    pass
class cursoInvalido(Exception):
    pass
class cpfInvalido(Exception):
    pass

class Pessoa(ABC):
    def __init__(self, nome, endereco, idade:int, cpf:int):
        self.__nome = nome 
        self.__endereco = endereco
        self.__idade = idade 
        self.__cpf = cpf 

    def getNome(self):
        return self.__nome

    def getEndereco(self):
        return self.__endereco
    
    def getIdade(self):
        return self.__idade
    
    def getCPF(self):
        return self.__cpf
    
    @abstractmethod
    def printDescricao():
        pass 


class Professor (Pessoa):
    def __init__(self, nome, endereco, idade:int, cpf: int, titulacao):
        super().__init__(nome, endereco, idade, cpf)
        self.__titulacao = titulacao

    def getTitulacao (self):
        return self.__titulacao
    
    def printDescricao(self):
        return print(f'Nome:{self.getNome()}, Endereco: {self.getEndereco()}, Idade:{self.getIdade()}, CPF: {self.getCPF()}, Titulacao:{self.getTitulacao()} ')
        

class Aluno (Pessoa):
    def __init__(self, nome, endereco, idade:int, cpf: int, curso):
        super().__init__(nome, endereco, idade, cpf)
        self.__curso = curso

    def getCurso(self):
        return self.__curso
    
    def printDescricao(self):
        return print(f'Nome:{self.getNome()}, Endereco: {self.getEndereco()}, Idade:{self.getIdade()}, CPF: {self.getCPF()}, Curso:{self.getCurso()} ')

if __name__ == "__main__":
    Pessoas = []
    Cadastrados = {}

    prof1 = Professor('Mauro', 'Av Cachoeira 31', 44, 1234321, 'Doutor' )
    Pessoas.append(prof1)

    prof2 = Professor('Leonardo', 'Av Rio Grande 12', 30, 123321, 'Mestre' )
    Pessoas.append(prof2)

    prof3 = Professor('Marcella', 'Rua Pelotas 234', 28, 134321, 'Doutor' )
    Pessoas.append(prof3)

    aluno1 = Aluno ('Luana','Rua Jose Alves 44', 19, 34567, 'SIN')
    Pessoas.append(aluno1)

    aluno2 = Aluno ('Laura','Rua Rio de Janeiro, 301', 17, 345767, 'CCO')
    Pessoas.append(aluno2)

    aluno3 = Aluno ('Maria','Av Jose Alves 42', 20, 345347, 'MAT')
    Pessoas.append(aluno3)

    aluno4 = Aluno ('Joana','Rua Caetano, 33', 19, 1234321, 'SIN')
    Pessoas.append(aluno4)

    for pessoa in Pessoas:
        try:
            if (pessoa.getCPF() in Cadastrados):
                raise cpfInvalido()

            if (type(pessoa)==Professor):
                if ( pessoa.getIdade()<30):
                 raise idadeInvalida()

                if ( pessoa.getTitulacao() != 'Doutor'):
                    raise titulacaoInvalida()
            else:
                if (pessoa.getIdade()<18):
                    raise idadeInvalida()

                if (pessoa.getCurso() != ('SIN' or 'CCO')):
                    raise cursoInvalido()

        except (idadeInvalida):
            print(f'Ídade invalida: {pessoa.getIdade()}')  
        except (titulacaoInvalida):
            print(f'Titulacao invalida: {pessoa.getTitulacao()}')  
        except (cursoInvalido):
            print(f'Curso invalido: {pessoa.getCurso()}')  
        except (cpfInvalido):
            print(f'Ja existe um cadastro nesse CPF: {pessoa.getCPF()}')  
        else: 
            print('Usuario cadastrado com sucesso!')
            Cadastrados[pessoa.getCPF()] = pessoa
            pessoa.printDescricao()
        finally:
            print()

            




