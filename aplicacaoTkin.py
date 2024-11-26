import tkinter as tk
from tkinter import ttk
import crud as crud




class PrincipalBD:
  
  def __init__(self, win):
    self.objBD = crud.AppBD()
    self.lbCodigo = tk.Label(win, text="Codigo do Produto")
    self.lblNome = tk.Label(win, text="Nome do Produto")
    self.lblPreco = tk.Label(win, text="Preço")
    
    self.txtCodigo = tk.Entry(bd=3)
    self.txtNome = tk.Entry()
    self.txtPreco = tk.Entry()
    
    self.btnCadastrar = tk.Button(win, text="Cadastrar", command=self.fCadastrarProduto)
    self.btnAtualizar = tk.Button(win, text="Atualizar", command=self.fAtualizarProduto)
    self.btnExcluir = tk.Button(win, text="Excluir", command=self.fExcluirProduto)
    self.btnLimpar = tk.Button(win, text="Limpar", command=self.fLimparTela)
    
    self.dadosColunas = ("Código", "Nome", "Preço")
    self.treeProdutos = ttk.Treeview(win, columns=self.dadosColunas, selectmode='browse')
    
    self.verscribar = ttk.Scrollbar(win, orient='vertical', command=self.treeProdutos.yview)
    
    self.verscribar.pack(side='right', fill="x")
    self.treeProdutos.configure(yscrollcommand=self.verscribar.set)
    
    self.treeProdutos.heading("Código", text="Código")
    self.treeProdutos.heading("Nome", text="Nome")
    self.treeProdutos.heading("Preço", text="Preço")
    
    self.treeProdutos.column("Código", minwidth=0, width=50)
    self.treeProdutos.column("Nome", minwidth=0, width=150)
    self.treeProdutos.column("Preço", minwidth=0, width=150)
    
    self.treeProdutos.pack(padx=10, pady=10)
    
    self.treeProdutos.bind("<<TreeviewSelect>>", self.apresentarRegistrosSelecionados)
    
    
    self.lbCodigo.place(x=100, y=50)
    self.txtCodigo.place(x=250, y=50)
    
    self.lblNome.place(x=100, y=100)
    self.txtNome.place(x=250, y=100)
    
    self.lblPreco.place(x=100, y=150)
    self.txtPreco.place(x=250, y=150)
    
    self.btnCadastrar.place(x=100, y=200)
    self.btnAtualizar.place(x=200, y=200)
    self.btnExcluir.place(x=300, y=200)
    self.btnLimpar.place(x=400, y=200)
    
    self.treeProdutos.place(x=100, y=300)
    self.verscribar.place(x=805, y=300, height=255)
    self.carregarDadosIniciais()
    
  
  
  def apresentarRegistrosSelecionados(self, event):
    self.fLimparTela()
    for selection in self.treeProdutos.selection():
      item = self.treeProdutos.item(selection)
      codigo,nome,preco = item["values"][0:3]
      self.txtCodigo.insert(0, codigo)
      self.txtNome.insert(0, nome)
      self.txtPreco.insert(0, preco)  
  
  
  def carregarDadosIniciais(self):
    try:
      self.id = 0
      self.iid = 0
      registros = self.objBD.selecionarDados()
      print("*************** dados disponiveis no BD **************")
      for item in registros:
        codigo=item[0]
        nome=item[1]
        preco=item[2]
        print("Codigo = ", codigo)
        print("Nome = ", nome)
        print("Preço = ", preco, "/n")
        
        self.treeProdutos.insert('','end',
                                 iid=self.iid,
                                 values=(codigo,nome,preco
                                         ))
        self.iid = self.iid + 1
        self.id = self.id + 1
      print('Dados da base')
    except:
      print('Ainda nao existem dados para carregar')
  
      
  def fLerCampos(self):
    try:
      print("********** dados disponiveis ************")
      codigo = int(self.txtCodigo.get())
      print('codigo', codigo)
      nome = self.txtNome.get()
      print('nome', nome)
      preco = float(self.txtPreco.get())
      print('preco', preco)
      print('leitura dos dados com sucesso')
    except:
      print("Nao foi possivel ler os dados.")  
    return codigo, nome, preco
  
  
  def fCadastrarProduto(self):
    try:
      print("********** dados disponiveis ************")
      codigo, nome, preco = self.fLerCampos()
      self.objBD.inserirDados(codigo, nome, preco)
      self.treeProdutos.insert('','end',
                               iid=self.iid,
                               values=(codigo, nome, preco)
                               )
      self.iid = self.iid + 1
      self.id = self.id + 1
      self.fLimparTela()
      print('Produto Cadastrado com Sucesso')
    except:
      print('Nao foi possivel fazer o cadastro')
  
      
  def fAtualizarProduto(self):
    try:
      print("********* dados disponiveis *********")
      codigo, nome, preco = self.fLerCampos()
      self.objBD.atualizarDados(codigo, nome, preco)
      self.treeProdutos.delete(*self.treeProdutos.get_children())
      self.carregarDadosIniciais()
      self.fLimparTela()
      print("Produto Atualizado com Sucesso")
    except:
      print("Nao foi possivel fazer a atualização")
  
  
  def fExcluirProduto(self):
    try:
      print("******** dados disponiveis *******")
      codigo, nome, preco = self.fLerCampos()
      self.objBD.excluirDados(codigo)
      
      self.treeProdutos.delete(*self.treeProdutos.get_children())
      self.carregarDadosIniciais()
      self.fLimparTela()
      print("Produto Excluido com sucesso")
    except:
      print("Nao foi possivel excluir o produto")
  
      
  def fLimparTela(self):
    try:
      print("********* dados disponiveis *********")
      self.txtCodigo.delete(0, tk.END)
      self.txtNome.delete(0, tk.END)
      self.txtPreco.delete(0, tk.END)
      print('campos limpos')
    except:
      print('nao foi possivel limpar os campos')


  
janela = tk.Tk()
principal = PrincipalBD(janela)
janela.title('Bem vindo a aplicação de loja')
janela.geometry("860x600+10+10")
janela.mainloop()