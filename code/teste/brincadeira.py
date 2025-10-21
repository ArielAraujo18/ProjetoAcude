import tkinter as tk
from tkinter import messagebox
import random
import webbrowser

root = tk.Tk()
root.title('Aceitas?')
root.geometry('600x600')
root.configure(background='#FF0000')

def botao_se_mexendo(e):
    distancia_x = abs(e.x - button_nao.winfo_x())
    distancia_y = abs(e.y - button_nao.winfo_y())
    if distancia_x < 300 and distancia_y < 100:
        x = random.randint(0, root.winfo_width() - button_nao.winfo_width())
        y = random.randint(0, root.winfo_height() - button_nao.winfo_height())
        button_nao.place(x=x, y=y)

def aceitou():
    messagebox.showinfo("<3", "Em breve casaremos <3")
    webbrowser.open("https://www.youtube.com/watch?v=ICS6uKC93w0")

def denied():
    messagebox.showinfo("")

margem = tk.Canvas(root, width=500, bg='#FF0000', height=100, bd=0, highlightthickness=0, relief='ridge')
margem.pack()

id_do_Texto = tk.Label(root, bg='#FFFFFF', text='Quer namorar comigo?', relief='ridge', bd=3, font=('Montserrat', 14, 'bold'))
id_do_Texto.pack(pady=20)

button_nao = tk.Button(root, text="Não", bg='#ffb3c1', relief='ridge', bd=3, command=denied, font=('Montserrat', 14, 'bold'))
button_nao.place(x=250, y=300)

button_sim = tk.Button(root, text='Sim', bg='#ffb3c1', relief='ridge', bd=3, command=aceitou, font=('Montserrat', 14, 'bold'))
button_sim.pack(pady=20)

root.bind('<Motion>', botao_se_mexendo)

root.mainloop()
