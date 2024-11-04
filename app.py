import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from models.cliente import inserir_cliente, obter_clientes, atualizar_cliente, deletar_cliente

class RoundedFrame(tk.Frame):
    def __init__(self, master, radius=15, **kwargs):
        super().__init__(master, **kwargs)
        self.radius = radius
        self.canvas = tk.Canvas(self, bg='white', highlightthickness=0)
        self.canvas.place(relwidth=1, relheight=1)
        self.create_oval(0, 0, 0, 0)

    def create_oval(self, x1, y1, x2, y2):
        self.canvas.create_oval(x1, y1, x2, y2, outline='#cccccc', fill='#ffffff', width=1)

    def draw_rounded_rect(self, x1, y1, x2, y2):
        self.create_oval(x1, y1, x1 + self.radius * 2, y1 + self.radius * 2)  # Top left
        self.create_oval(x2 - self.radius * 2, y1, x2, y1 + self.radius * 2)  # Top right
        self.create_oval(x1, y2 - self.radius * 2, x1 + self.radius * 2, y2)  # Bottom left
        self.create_oval(x2 - self.radius * 2, y2 - self.radius * 2, x2, y2)  # Bottom right
        self.canvas.create_rectangle(x1 + self.radius, y1, x2 - self.radius, y2, outline='#cccccc', fill='#ffffff', width=1)  # Middle horizontal
        self.canvas.create_rectangle(x1, y1 + self.radius, x2, y2 - self.radius, outline='#cccccc', fill='#ffffff', width=1)  # Middle vertical

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Gerenciamento de Clientes")
        self.master.geometry("350x400")
        self.master.configure(bg='#f0f0f0')

        # Frame com bordas arredondadas
        frame = RoundedFrame(master, radius=15, bg='#ffffff')
        frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        frame.draw_rounded_rect(0, 0, 350, 400)

        # Labels e Entradas
        tk.Label(frame, text="Deletar ID do Cliente:", bg='#ffffff').pack(pady=5)
        self.id_entry = tk.Entry(frame, width=25)
        self.id_entry.pack(pady=5, padx=10)

        tk.Label(frame, text="Nome:", bg='#ffffff').pack(pady=5)
        self.nome_entry = tk.Entry(frame, width=25)
        self.nome_entry.pack(pady=5, padx=10)

        tk.Label(frame, text="CPF:", bg='#ffffff').pack(pady=5)
        self.cpf_entry = tk.Entry(frame, width=25)
        self.cpf_entry.pack(pady=5, padx=10)

        tk.Label(frame, text="RG:", bg='#ffffff').pack(pady=5)
        self.rg_entry = tk.Entry(frame, width=25)
        self.rg_entry.pack(pady=5, padx=10)

        # Botões
        button_frame = tk.Frame(frame, bg='#ffffff')
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Inserir Cliente", command=self.inserir_cliente, bg='#4CAF50', fg='white', width=15).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Atualizar Cliente", command=self.atualizar_cliente, bg='#2196F3', fg='white', width=15).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Deletar Cliente", command=self.deletar_cliente, bg='#F44336', fg='white', width=15).grid(row=1, column=0, padx=5)
        tk.Button(button_frame, text="Listar Clientes", command=self.listar_clientes, bg='#FFC107', fg='black', width=15).grid(row=1, column=1, padx=5)

    def inserir_cliente(self):
        nome = self.nome_entry.get()
        cpf = self.cpf_entry.get()
        rg = self.rg_entry.get()
        if nome and cpf and rg:
            inserir_cliente(nome, cpf, rg)
            messagebox.showinfo("Sucesso", "Cliente inserido com sucesso!")
            self.limpar_campos()
        else:
            messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")

    def atualizar_cliente(self):
        id_cliente = self.id_entry.get()
        novo_nome = self.nome_entry.get()
        novo_cpf = self.cpf_entry.get()
        novo_rg = self.rg_entry.get()
        if id_cliente and novo_nome and novo_cpf and novo_rg:
            try:
                atualizar_cliente(int(id_cliente), novo_nome, novo_cpf, novo_rg)
                messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
                self.limpar_campos()
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível atualizar o cliente: {e}")
        else:
            messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")

    def deletar_cliente(self):
        id_cliente = self.id_entry.get()
        if id_cliente:
            try:
                deletar_cliente(int(id_cliente))
                messagebox.showinfo("Sucesso", "Cliente deletado com sucesso!")
                self.limpar_campos()
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível deletar o cliente: {e}")
        else:
            messagebox.showwarning("Atenção", "Por favor, informe o ID do cliente.")

    def listar_clientes(self):
        clientes = obter_clientes()
        lista_clientes = '\n'.join([f'ID {cliente[0]}: {cliente[1]} - CPF: {cliente[2]}' for cliente in clientes])
        messagebox.showinfo("Clientes", lista_clientes if lista_clientes else "Nenhum cliente cadastrado.")

    def limpar_campos(self):
        self.id_entry.delete(0, tk.END)
        self.nome_entry.delete(0, tk.END)
        self.cpf_entry.delete(0, tk.END)
        self.rg_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
