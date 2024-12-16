import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

def converter_para_jpg():
    caminho_arquivo = filedialog.askopenfilename(title="Selecione uma imagem")
    if caminho_arquivo:
        try:
            img = Image.open(caminho_arquivo)
            # Converter para RGB se a imagem for em outro modo de cor (ex: RGBA para PNGs com transparência)
            img = img.convert("RGB")  
            nome_arquivo, extensao = os.path.splitext(os.path.basename(caminho_arquivo))
            novo_nome_arquivo = nome_arquivo + ".jpg"
            diretorio_arquivo = os.path.dirname(caminho_arquivo)
            novo_caminho = os.path.join(diretorio_arquivo, novo_nome_arquivo)
            img.save(novo_caminho, "JPEG")
            messagebox.showinfo("Sucesso", f"Imagem convertida e salva como:\n{novo_caminho}")
            atualizar_imagem_exibida(novo_caminho) # Atualiza a exibição da imagem
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro durante a conversão: {e}")

def abrir_imagem():
    caminho_arquivo = filedialog.askopenfilename(title="Selecione uma imagem")
    if caminho_arquivo:
        atualizar_imagem_exibida(caminho_arquivo)
        
def atualizar_imagem_exibida(caminho_imagem):
    try:
        img = Image.open(caminho_imagem)
        img.thumbnail((300, 300)) # Redimensiona para exibir na interface
        imagem_tk = ImageTk.PhotoImage(img)
        label_imagem.config(image=imagem_tk)
        label_imagem.image = imagem_tk # Importante: manter uma referência!
    except Exception as e:
       print(f"Erro ao carregar imagem {e}")


# Configuração da janela principal
janela = tk.Tk()
janela.title("Conversor de Imagens para JPG")
janela.configure(bg="#e0f2f7") # Cor de fundo

# Estilos (cores)
cor_botao = "#4fc3f7" # Azul claro
cor_fundo_botao = "#bbdefb"

# Widgets
botao_converter = tk.Button(janela, text="Converter para JPG", command=converter_para_jpg, bg=cor_botao, activebackground=cor_fundo_botao, font=("Arial", 12), padx=10, pady=5)
botao_converter.pack(pady=10)

botao_abrir = tk.Button(janela, text="Abrir Imagem", command=abrir_imagem, bg=cor_botao, activebackground=cor_fundo_botao, font=("Arial", 12), padx=10, pady=5)
botao_abrir.pack(pady=(0, 10))

label_imagem = tk.Label(janela, bg="#FFFFFF") # Label para exibir a imagem
label_imagem.pack()

# Loop principal
janela.mainloop()