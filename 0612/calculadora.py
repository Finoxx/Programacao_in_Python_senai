import tkinter as tk

def soma():
    numero_1 = float(input_1.get())
    numero_2 = float(input_2.get())
    soma = numero_1 + numero_2
    resultado.config(text=soma)

def sub():
    numero_1 = float(input_1.get())
    numero_2 = float(input_2.get())
    sub = numero_1 - numero_2
    resultado.config(text=sub)

def vezes():
    numero_1 = float(input_1.get())
    numero_2 = float(input_2.get())
    mult = numero_1 * numero_2
    resultado.config(text=mult)

def div():
    numero_1 = float(input_1.get())
    numero_2 = float(input_2.get())
    mult = numero_1 / numero_2
    resultado.config(text=mult)

janela = tk.Tk()

janela.configure(bg = '#DCD7D7')



tk.Label(janela, text='CALCULADORA', bg = '#DCD7D7',font=('Montserrat', 12) ).grid(row=0, column=0, pady=20)





fr1 = tk.Frame(janela, bg = '#DCD7D7')

fr1.grid(columnspan=2)



numero_1 = tk.Label(fr1, text = 'Numero', font=('Montserrat', 12), bg = '#DCD7D7')

numero_1.grid(row=1,column=1)



numero_1 = tk.Label(fr1, text = 'Numero', font=('Montserrat', 12), bg = '#DCD7D7')

numero_1.grid(row=1,column=3)



input_1 = tk.Entry(fr1,font=('Montserrat', 12), width=16 )

input_1.grid(row=2, column=1, pady=20, padx=5)



input_2 = tk.Entry(fr1,font=('Montserrat', 12), width=16 )

input_2.grid(row=2, column=3, pady=20, padx=5)



fr2 = tk.Frame(janela, bg = '#DCD7D7')

fr2.grid(columnspan=2, )



btn_soma = tk.Button(fr2, text='+', font=('Montserrat', 12), bg = '#FF0909', width=12, command=soma) 

btn_soma.grid(row=4, column=1, pady=20)



btn_sub = tk.Button(fr2, text='-', font=('Montserrat', 12), bg = '#FF0909', width=12, command= sub)

btn_sub.grid(row=4, column=3, pady=20)



btn_mult = tk.Button(fr2, text='x', font=('Montserrat', 12), bg = '#FF0909', width=12, command=vezes)

btn_mult.grid(row=5, column=1, pady=20)



btn_div = tk.Button(fr2, text='/', font=('Montserrat', 12), bg = '#FF0909', width=12, command= div)

btn_div.grid(row=5, column=3, pady=20)





resultado = tk.Label(fr2, text = '=', fg = '#000000',font=('Montserrat', 12), bg = '#ffffff')

resultado.grid(row=6,column=2)



janela.mainloop()