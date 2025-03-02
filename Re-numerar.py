import os
import re

def renomear_imagens_decrescente(pasta):
    arquivos = sorted(os.listdir(pasta), reverse=True)
    imagens = [f for f in arquivos if f.lower().endswith(('jpg', 'jpeg', 'png', 'gif', 'bmp'))]
    
    # Passo 1: Renomeia para nomes temporários para evitar conflitos
    for i, imagem in enumerate(imagens):
        caminho_antigo = os.path.join(pasta, imagem)
        extensao = os.path.splitext(imagem)[1].lower()
        temp_nome = f"temp_{i}{extensao}"
        caminho_temp = os.path.join(pasta, temp_nome)
        os.rename(caminho_antigo, caminho_temp)
    
    # Passo 2: Renomeia as imagens na ordem desejada
    novo_numero = len(imagens)
    temp_arquivos = sorted(os.listdir(pasta))
    
    for temp_imagem in temp_arquivos:
        if temp_imagem.startswith("temp_"):
            caminho_temp = os.path.join(pasta, temp_imagem)
            extensao = os.path.splitext(temp_imagem)[1].lower()
            novo_nome = f"imagem{novo_numero}{extensao}"
            caminho_novo = os.path.join(pasta, novo_nome)
            os.rename(caminho_temp, caminho_novo)
            print(f"{temp_imagem} -> {novo_nome}")
            novo_numero -= 1

# Exemplo de uso
pasta_imagens = "imagens/@Jociklejacome"  # Substitua pelo caminho real
renomear_imagens_decrescente(pasta_imagens)
