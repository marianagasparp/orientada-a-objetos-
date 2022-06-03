from typing import List


class Disciplina:
    def __init__(self, codigo, nome, cargaHoraria):
        self.__codigo = codigo
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria

    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.__nome

    def getCargaHoraria(self):
        return self.__cargaHoraria
        

class Curso:
    def __init__(self,nome, grade):
        self.__nome = nome
        self.__grade= grade

    def getNome(self):
        return self.__nome

    def getGrade(self):
        return self.__grade
  
    def getDisciplinas(self):
        return self.__grade.getDisciplinas()
    
class Historico:
    def __init__(self):
        self.__historico = []
    
    def getHistorico (self):
        return self.__historico

    def addDisciplina(self, disciplina):
        self.__historico.append(disciplina)

class Aluno():
    def __init__(self, nroMatric, nome, curso):
        self.__nroMatric = nroMatric
        self.__nome = nome
        self.__curso = curso
        self.__historico = Historico()

    def getnroMatric(self):
        return self.__nroMatric

    def getNome(self):
        return self.__nome

    def getCurso(self):
        return self.__curso.getNome()
    
    def getHistorico(self):
        return self.__historico.getHistorico()

    def addDisciplina(self, disciplina):
        self.__historico.addDisciplina(disciplina)
    
    def getCargaHorariaObrigatoria(self):
        cargaHorariaObrigatoria = 0
        for disciplina in self.__historico.getHistorico():
            if disciplina in self.__curso.getDisciplinas():
                cargaHorariaObrigatoria += disciplina.getCargaHoraria()
        return cargaHorariaObrigatoria
    
    def getCargaHorariaEletiva(self):
        cargaHorariaEletiva = 0
        for disciplina in self.__historico.getHistorico():
            if not (disciplina in self.__curso.getDisciplinas()):
                cargaHorariaEletiva += disciplina.getCargaHoraria()
        return cargaHorariaEletiva 
    

class Grade:
    def __init__(self, ano):
        self.__ano = ano
        self.__disciplinas = []

    def getAno(self):
        return self.__ano

    def getDisciplinas(self):
        return self.__disciplinas

    def addDisciplina(self, disciplina):
        self.__disciplinas.append(disciplina)



if __name__ == "__main__":    
    listaCursos = []
    listaAlunos = []

    grade = Grade(2011)
    disciplina = Disciplina('COM220','POO', 68)
    disciplina2 = Disciplina('COM112','AEDII', 80)
    disciplina3 = Disciplina('COM210','ENG. SOFTWARE', 90)
    grade.addDisciplina(disciplina)
    grade.addDisciplina(disciplina2)
    grade.addDisciplina(disciplina3) 
    curso = Curso('Sistemas de Informacao', grade)
    listaCursos.append(curso)

    grade2 = Grade(2015)
    disciplina4 = Disciplina('COM110','Int. a Programacao', 48)
    disciplina5 = Disciplina('MATI001','CALCULO I', 70 )
    disciplina6 = Disciplina('MAT013','Probabilidade e Estatistica', 90)
    grade2.addDisciplina(disciplina4)
    grade2.addDisciplina(disciplina5)
    grade2.addDisciplina(disciplina6) 
    curso2 = Curso('Matematica', grade2)
    listaCursos.append(curso2)

    aluno = Aluno(123,'Joao', curso)
    listaAlunos.append(aluno)
    aluno2 = Aluno(145, 'Maria', curso2)
    listaAlunos.append(aluno2)

    aluno.addDisciplina(disciplina)
    aluno.addDisciplina(disciplina2)
    aluno.addDisciplina(disciplina4)

    aluno2.addDisciplina(disciplina3)
    aluno2.addDisciplina(disciplina5)
    aluno2.addDisciplina(disciplina6)

    for aluno in listaAlunos:
        print(f'O aluno {aluno.getNome()} do curso {aluno.getCurso()} possui {aluno.getCargaHorariaObrigatoria()} horas obrigatorias e {aluno.getCargaHorariaEletiva()} horas eletivas')
        print( )


 