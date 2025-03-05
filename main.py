from tkinter import *

# Cores
cor1 = "#1e1f1e"  # Preto
cor2 = "#feffff"  # Branco
cor3 = "#38576b"  # Azul escuro
cor4 = "#ECEFF1"  # Cinza claro
cor5 = "#FFAB40"  # Laranja

# Criando janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)

# Criando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela,  width=235, height=268, bg=cor1)
frame_corpo.grid(row=1, column=0)

todos_valores = ""


valor_text = StringVar()

def entrar_valor(event): 

    global todos_valores

    todos_valores = todos_valores + str(event)


    valor_text.set(todos_valores)

def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    valor_text.set(str(resultado))

def limparTela():
    global todos_valores
    todos_valores=""
    valor_text.set("")



app_label = Label(frame_tela, textvariable=valor_text, width=16, height=2,padx=7,relief=FLAT,anchor="e",justify=RIGHT, font=('Ivy 18'),bg=cor3, fg=cor2)
app_label.place(x=0,y=0)


# Adicionando botões
b_1 = Button(frame_corpo,command=limparTela, text='C', width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.grid(row=0, column=0, columnspan=2)

b_2 = Button(frame_corpo, command=lambda:entrar_valor('%'), text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.grid(row=0, column=2)

b_3 = Button(frame_corpo,  command=lambda:entrar_valor('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.grid(row=0, column=3)

b_4 = Button(frame_corpo, command=lambda:entrar_valor('7'), text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.grid(row=1, column=0)

b_5 = Button(frame_corpo, command=lambda:entrar_valor('8'), text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.grid(row=1, column=1)

b_6 = Button(frame_corpo,  command=lambda:entrar_valor('9'),text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.grid(row=1, column=2)

b_7 = Button(frame_corpo,  command=lambda:entrar_valor('*'),text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.grid(row=1, column=3)

b_8 = Button(frame_corpo, command=lambda:entrar_valor('4'), text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.grid(row=2, column=0)

b_9 = Button(frame_corpo, command=lambda:entrar_valor('5'), text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.grid(row=2, column=1)

b_10 = Button(frame_corpo, command=lambda:entrar_valor('6'), text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.grid(row=2, column=2)

b_11 = Button(frame_corpo, command=lambda:entrar_valor('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.grid(row=2, column=3)

b_12 = Button(frame_corpo, command=lambda:entrar_valor('1'), text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.grid(row=3, column=0)

b_13 = Button(frame_corpo, command=lambda:entrar_valor('2'), text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.grid(row=3, column=1)

b_14 = Button(frame_corpo,  command=lambda:entrar_valor('3'),text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.grid(row=3, column=2)

b_15 = Button(frame_corpo,  command=lambda:entrar_valor('+'),text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.grid(row=3, column=3)

b_16 = Button(frame_corpo,  command=lambda:entrar_valor('0'),text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.grid(row=4, column=0, columnspan=2)

b_17 = Button(frame_corpo, command=lambda:entrar_valor('.'), text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.grid(row=4, column=2)

b_18 = Button(frame_corpo,  command=calcular,text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.grid(row=4, column=3)





# Loop principal
janela.mainloop()


