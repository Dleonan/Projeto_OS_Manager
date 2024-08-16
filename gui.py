from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, messagebox
from db_utils import validar_login


# Caminho das assets
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\leonam\Desktop\TKD\Tela_De_Login\build\assets\frame0")

path = Path(r"C:\Users\leonam\Desktop\TKD\Tela_De_Login\build\assets\fundo1.png")
print(path.exists())  # Deve imprimir True se o arquivo existir

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def center_window(window):
    # Obtém as dimensões da tela do usuário
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # Define as dimensões da janela
    window_width = 1280
    window_height = 720
    # Calcula a posição x e y para centralizar a janela
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    # Define a geometria da janela para incluir a posição e o tamanho
    window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    # responsavel por validar o login e imprimir uma mensagem ao usuario em caso de erro ou sucesso!
    
def realizar_login():
    login_usuario = entry.get()
    senha_usuario = entry2.get()

    if validar_login(login_usuario, senha_usuario):
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")


window = Tk()
center_window(window)  # Centraliza a janela na tela
window.resizable(False, False)  # Permite redimensionamento na largura, mas não na altura

# Carregar a imagem de fundo
fundo_image = PhotoImage(file=relative_to_assets(r"C:\Users\leonam\Desktop\TKD\Tela_De_Login\build\assets\fundo1.png"))


# Criação do Canvas e aplicação da imagem de fundo
canvas = Canvas(window, width=1280, height=720)
canvas.pack(fill="both", expand=True)

# Colocar a imagem no canvas
canvas.create_image(0, 0, image=fundo_image, anchor="nw")

# Adicionando a campo texto
capo_texte_image = PhotoImage(file=relative_to_assets(r"C:\Users\leonam\Desktop\TKD\Tela_De_Login\build\assets\TextBox_Bg.png"))
canvas.create_image(
    640,  # X: posição horizontal da imagem
    350,  # Y: posição vertical da imagem
    image=capo_texte_image
)

# Adicionando a campo texto
capo_texte2_image = PhotoImage(file=relative_to_assets(r"C:\Users\leonam\Desktop\TKD\Tela_De_Login\build\assets\TextBox_Bg.png"))
canvas.create_image(
    640,  # X: posição horizontal da imagem
    450,  # Y: posição vertical da imagem
    image=capo_texte2_image
)
# Aqui eu adicionei a funcionalidade ao campo do canvas que antes era somente uma imagem 

# Adicionar um campo de texto funcional sobre a imagem
entry = Entry(canvas, bd=0, bg="#ffffff", highlightthickness=0)
entry.place(x=530, y=330, width=200, height=50)

# Adicionar outro campo de texto funcional
entry2 = Entry(canvas, show= "*", bd=0, bg="#ffffff", highlightthickness=0)
entry2.place(x=534, y=430, width=200, height=50)

# Adicionar a descrição para o primeiro campo de texto
label1 = Label(canvas, text="Login:", bg="#ffffff", fg="black", font=("Arial", 14))
label1.place(x=470, y=340)  # Ajuste a posição conforme necessário

# Adicionar a descrição para o segundo campo de texto
label2 = Label(canvas, text="Senha:", bg="#ffffff", fg="black", font=("Arial", 14))
label2.place(x=470, y=440)  # Ajuste a posição conforme necessário


# Adicionando a logo
logo_image = PhotoImage(file=relative_to_assets(r"C:\Users\leonam\Desktop\TKD\Tela_De_Login\build\assets\aboch.png"))
canvas.create_image(
    640,  # X: posição horizontal da imagem
    150,  # Y: posição vertical da imagem
    image=logo_image
)
# Adicionando o botão
button = Button(canvas, text="Entre", bg="#4CAF50", fg="white", font=("Arial", 14), command=realizar_login)
button.place(x=550, y=520, width=200, height=50)  # Ajuste a posição e o tamanho conforme necessário


footer_text = "© 2024 Leonan Matheus leyedecker, @ABOCH. https://github.com/Dleonan"
footer_label = Label(canvas, text=footer_text, bg="#2148C0", fg="white", font=("Arial", 10))
footer_label.pack(side="bottom", fill="x", pady=10)

window.mainloop()
