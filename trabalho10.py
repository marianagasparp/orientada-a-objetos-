import tkinter as tk
from tkinter import messagebox, simpledialog


class ModelCliente():
    def __init__(self, nome, email, codigo):
        self.__nome = nome
        self.__email = email
        self.__codigo = codigo

    def getNome(self):
        return self.__nome

    def getEmail(self):
        return self.__email
    
    def getCodigo(self):
        return self.__codigo
    
    def imprimeDados(self):
        return 'Cliente: ' + self.getNome() + ', Email: ' + self.getEmail() + ', Codigo: '+ self.getCodigo()


class View():
    def __init__(self, master, controller):
        self.controller = controller
        self.janela = tk.Frame(master)
        self.janela.pack()
        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)
        self.frame3 = tk.Frame(self.janela)

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
      
        self.labelInfo1 = tk.Label(self.frame1,text="Nome: ")
        self.labelInfo2 = tk.Label(self.frame2,text="Email: ")
        self.labelInfo3 = tk.Label(self.frame3,text="Codigo: ")
        self.labelInfo1.pack(side="left")
        self.labelInfo2.pack(side="left") 
        self.labelInfo3.pack(side="left")  

        self.inputText1 = tk.Entry(self.frame1, width=20)
        self.inputText1.pack(side="left")
        self.inputText2 = tk.Entry(self.frame2, width=20)
        self.inputText2.pack(side="left") 
        self.inputText3 = tk.Entry(self.frame3, width=20)
        self.inputText3.pack(side="left")             
      
        self.buttonSubmit = tk.Button(self.janela,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controller.enterHandler)
      
        self.buttonClear = tk.Button(self.janela,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controller.clearHandler)  

        self.buttonCli = tk.Button(self.janela,text="Consultar Cliente")      
        self.buttonCli.pack(side="left")
        self.buttonCli.bind("<Button>", controller.cliHandler) 

        
    def mostraJanela(self, titulo, mensagem):
         messagebox.showinfo(titulo, mensagem)
    
      
class Controller():       
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x150')
        self.listaClientes = []

        # Cria a view passando referência da janela principal e
        # de si próprio (controlador)
        self.view = View(self.root, self) 

        self.root.title("Exemplo MVC")
        # Inicia o mainloop
        self.root.mainloop()


    def enterHandler(self, event):
        nomeCli = self.view.inputText1.get()
        emailCli = self.view.inputText2.get()
        codigoCli = self.view.inputText3.get()
        for cliente in self.listaClientes:
            if cliente.getCodigo() == codigoCli:
               self.view.mostraJanela('Erro', 'Ja existe cliente cadastrado nesse codigo')
               self.clearHandler(event)
               break 
        else:
            cliente = ModelCliente(nomeCli, emailCli, codigoCli)
            self.listaClientes.append(cliente)
            self.view.mostraJanela('Sucesso', 'Cliente cadastrado com sucesso')
            self.clearHandler(event)

    def clearHandler(self, event):
        self.view.inputText1.delete(0, len(self.view.inputText1.get()))
        self.view.inputText2.delete(0, len(self.view.inputText2.get()))
        self.view.inputText3.delete(0, len(self.view.inputText3.get()))

    def cliHandler (self, event):
        codigoCli = simpledialog.askstring('Codigo ', 'Codigo: ')
        cont = 0
        for cliente in self.listaClientes:
            if cliente.getCodigo() == codigoCli:
                self.view.mostraJanela('Cliente: ', cliente.imprimeDados())
                cont+= 1
        if cont == 0:
           self.view.mostraJanela('erro', 'Codigo nao Cadastrado')

    

    

if __name__ == '__main__':
    c = Controller()