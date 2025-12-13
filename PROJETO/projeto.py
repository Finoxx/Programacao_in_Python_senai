import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class Sistema: # Corrigi o nome para 'Sistema' (opcional)
    def __init__(self, root): # MUDANÇA PRINCIPAL: De 'tela' para '__init__'
        self.janela = root
        self.janela.title('Sistema de gestão de cadastros')
        self.janela.geometry('850x600') # Aumentei um pouco a largura

        self.db_name = 'banco.db'

        # Agora chamamos a criação da tabela
        self.criar_tabela()

        # --- CADASTRO ---
        self.frame_cadastro = ttk.Labelframe(self.janela, text='Cadastro de Cliente')
        self.frame_cadastro.pack(fill='x', expand='yes', padx=10, pady=10)

        # Nome
        ttk.Label(self.frame_cadastro, text="Nome:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.ent_nome = ttk.Entry(self.frame_cadastro, width=30)
        self.ent_nome.grid(row=0, column=1, padx=5, pady=5)

        # E-mail
        ttk.Label(self.frame_cadastro, text='E-mail:').grid(row=0, column=2, padx=5, pady=5, sticky='w')
        self.ent_email = ttk.Entry(self.frame_cadastro, width=30)
        self.ent_email.grid(row=0, column=3, padx=5, pady=5)

        # Telefone
        ttk.Label(self.frame_cadastro, text='Telefone:').grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.ent_telefone = ttk.Entry(self.frame_cadastro, width=30)
        self.ent_telefone.grid(row=1, column=1, padx=5, pady=5)

        # Endereço (ESTE CAMPO ESTAVA FALTANDO NO SEU CÓDIGO)
        ttk.Label(self.frame_cadastro, text='Endereço:').grid(row=1, column=2, padx=5, pady=5, sticky='w')
        self.ent_endereco = ttk.Entry(self.frame_cadastro, width=30)
        self.ent_endereco.grid(row=1, column=3, padx=5, pady=5)

        # --- BOTÕES ---
        self.frame_botoes = ttk.Frame(self.janela)
        self.frame_botoes.pack(pady=10)

        ttk.Button(self.frame_botoes, text='Adicionar', command=self.adicionar_cliente).grid(row=0, column=0, padx=10)
        ttk.Button(self.frame_botoes, text="Editar Selecionado", command=self.editar_cliente).grid(row=0, column=1, padx=10)
        ttk.Button(self.frame_botoes, text="Excluir Selecionado", command=self.excluir_cliente).grid(row=0, column=2, padx=10)
        ttk.Button(self.frame_botoes, text="Limpar Campos", command=self.limpar_campos).grid(row=0, column=3, padx=10)

        # --- LISTAGEM ---
        self.tree = ttk.Treeview(self.janela, columns=("ID", "Nome", "Email", "Telefone", "Endereço"), show="headings")
        
        # Configurar colunas
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Email", text="E-mail")
        self.tree.heading("Telefone", text="Telefone")
        self.tree.heading("Endereço", text="Endereço")
        
        self.tree.column("ID", width=30)
        self.tree.column("Nome", width=150)
        self.tree.column("Email", width=150)
        self.tree.column("Telefone", width=100)
        self.tree.column("Endereço", width=200)
        
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Evento de clique na lista
        self.tree.bind("<<TreeviewSelect>>", self.selecionar_registro)
        
        # Carregar dados iniciais
        self.listar_clientes()

    # --- MÉTODOS DE BANCO E LÓGICA (Agora fora do __init__) ---

    def executar_query(self, query, parametros=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parametros)
            conn.commit() # Importante dar commit para salvar alterações
        return result
    
    def criar_tabela(self):
        query = '''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL, 
            telefone TEXT NOT NULL,
            endereco TEXT NOT NULL
        )
        '''
        self.executar_query(query)
    
    def adicionar_cliente(self):
        # Verifica se o nome foi preenchido
        if self.ent_nome.get() == "":
            messagebox.showwarning("Atenção", "O campo Nome é obrigatório.")
            return

        query = "INSERT INTO clientes VALUES (NULL, ?, ?, ?, ?)"
        parametros = (
            self.ent_nome.get(), 
            self.ent_email.get(), 
            self.ent_telefone.get(), 
            self.ent_endereco.get()
        )
        
        try:
            self.executar_query(query, parametros)
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
            self.limpar_campos()
            self.listar_clientes()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")

    def listar_clientes(self):
        """Consulta o banco e atualiza a lista na tela"""
        # Limpa a tabela visual atual
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
            
        # Busca dados do banco
        query = "SELECT * FROM clientes ORDER BY nome DESC"
        db_rows = self.executar_query(query)
        
        # Insere na Treeview
        for row in db_rows:
            self.tree.insert("", 0, values=row)

    def selecionar_registro(self, event):
        """Pega os dados da linha clicada e joga nos campos de texto"""
        try:
            item_selecionado = self.tree.selection()[0]
            valores = self.tree.item(item_selecionado, 'values')
            
            # Limpa e insere os valores nos campos
            self.limpar_campos()
            self.ent_nome.insert(0, valores[1])
            self.ent_email.insert(0, valores[2])
            self.ent_telefone.insert(0, valores[3])
            self.ent_endereco.insert(0, valores[4])
        except IndexError:
            pass # Clique em área vazia ou cabeçalho

    def editar_cliente(self):
        """Edita o cliente selecionado"""
        try:
            item_selecionado = self.tree.selection()[0]
            valores = self.tree.item(item_selecionado, 'values')
            id_cliente = valores[0] # O ID é a primeira coluna
            
            query = "UPDATE clientes SET nome=?, email=?, telefone=?, endereco=? WHERE id=?"
            parametros = (
                self.ent_nome.get(),
                self.ent_email.get(),
                self.ent_telefone.get(),
                self.ent_endereco.get(),
                id_cliente
            )
            
            self.executar_query(query, parametros)
            messagebox.showinfo("Sucesso", "Dados do cliente atualizados!")
            self.limpar_campos()
            self.listar_clientes()
            
        except IndexError:
            messagebox.showwarning("Atenção", "Selecione um cliente na lista para editar.")

    def excluir_cliente(self):
        """Exclui o cliente selecionado"""
        try:
            item_selecionado = self.tree.selection()[0]
            valores = self.tree.item(item_selecionado, 'values')
            id_cliente = valores[0]
            
            confirmar = messagebox.askyesno("Confirmar", "Tem certeza que deseja excluir este cliente?")
            if confirmar:
                query = "DELETE FROM clientes WHERE id=?"
                self.executar_query(query, (id_cliente,))
                messagebox.showinfo("Sucesso", "Cliente removido!")
                self.limpar_campos()
                self.listar_clientes()
                
        except IndexError:
            messagebox.showwarning("Atenção", "Selecione um cliente na lista para excluir.")

    def limpar_campos(self):
        self.ent_nome.delete(0, tk.END)
        self.ent_email.delete(0, tk.END)
        self.ent_telefone.delete(0, tk.END)
        self.ent_endereco.delete(0, tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    app = Sistema(root) # Agora chama a classe corrigida
    root.mainloop()