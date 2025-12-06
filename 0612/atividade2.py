import tkinter as tk

def primir():
    print(imput_nome.get(),imput_idade.get(),imput_mail.get(),imput_endereco.get(),imput_celular.get(),imput_CEP.get(),imput_cidade.get(),imput_cursos.get())


janela =  tk.Tk()
janela.geometry('1700x750')
janela.configure(bg =  '#F5F5F5')

fr1 = tk.Frame(janela, bg = '#F5F5F5')

fr1.grid(columnspan=2)


nome = tk.Label(fr1, text = 'Nome:', font=('Montserrat', 12), bg = '#DCD7D7')

nome.grid(row=1000,column=1000)

idade = tk.Label(fr1, text = 'idade:', font=('Montserrat', 12), bg = '#DCD7D7')

idade.grid(row=1250,column=1000)

mail = tk.Label(fr1, text = 'E-mail:', font=('Montserrat', 12), bg = '#DCD7D7')

mail.grid(row=1500,column=1000)

Endereco = tk.Label(fr1, text = 'Endereco:', font=('Montserrat', 12), bg = '#DCD7D7')

Endereco.grid(row=1750,column=1000)

Celular = tk.Label(fr1, text = 'Celular:', font=('Montserrat', 12), bg = '#DCD7D7')

Celular.grid(row=2000,column=1000)

CEP = tk.Label(fr1, text = 'CEP:', font=('Montserrat', 12), bg = '#DCD7D7')

CEP.grid(row=2250,column=1000)

Cidade = tk.Label(fr1, text = 'Cidade:', font=('Montserrat', 12), bg = '#DCD7D7')

Cidade.grid(row=2500,column=1000)

Cursos = tk.Label(fr1, text = 'Cursos:', font=('Montserrat', 12), bg = '#DCD7D7')

Cursos.grid(row=2750,column=1000)

imput_nome = tk.Entry(fr1,font=('Montserrat', 12), width=16 )

imput_nome.grid(row=1000, column=3000, pady=20, padx=5)

imput_idade = tk.Entry(fr1,font=('Montserrat', 12), width=16 )

imput_idade.grid(row=1250, column=3000, pady=20, padx=5)

imput_mail = tk.Entry(fr1,font=('Montserrat', 12), width=16 )

imput_mail.grid(row=1500, column=3000, pady=20, padx=5)

imput_endereco = tk.Entry(fr1,font=('Montserrat', 12), width=16 )

imput_endereco.grid(row=1750, column=3000, pady=20, padx=5)

imput_celular = tk.Entry(fr1,font=('Montserrat', 12), width=16 )

imput_celular.grid(row=2000, column=3000, pady=20, padx=5)

imput_CEP = tk.Entry(fr1,font=('Montserrat', 12), width=16 )

imput_CEP.grid(row=2250, column=3000, pady=20, padx=5)

imput_cidade = tk.Entry(fr1,font=('Montserrat', 12), width=16 )

imput_cidade.grid(row=2500, column=3000, pady=20, padx=5)

imput_cursos = tk.Entry(fr1,font=('Montserrat', 12), width=16 )

imput_cursos.grid(row=2750, column=3000, pady=20, padx=5)


btn_enviar = tk.Button(fr1, text='ENVIAR', font=('Montserrat', 12), bg = 'blue', width=12, command=primir) 
btn_enviar.grid(row=3000, column=1500, pady=20)
 
janela.mainloop()
