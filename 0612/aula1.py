import tkinter as tk




def mostar_():
    texto  =   input_.get()
    mostrar_texto.config(text=texto)   




janela =  tk.Tk()
janela.geometry('1440x1024')
janela.configure(bg =  '#480987')


texto = tk.Label(janela, text='SEU TEXTO AQUI', fg = 'white', font = ('Montserrat', 32), bg ='#480987' )
texto.pack(pady=75)


input_ = tk.Entry(janela,font = ('Montserrat', 32) )
input_.pack(pady=40)


btn =  tk.Button(janela, text='CLIQUE', bg = 'black', fg = 'white' , font = ('Montserrat', 25), command=mostar_)
btn.pack(pady=40)


mostrar_texto =  tk.Label(janela, text = 'aqui vai mostrar um texto', bg ='#480987', fg = 'white', font = ('Montserrat', 25))
mostrar_texto.pack(pady=30)



janela.mainloop()