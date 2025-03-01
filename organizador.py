import os
import re

def renomear_imagens(pasta):
    # Obtém a lista de arquivos na pasta
    arquivos = sorted(os.listdir(pasta))
    
    # Filtra apenas os arquivos de imagem
    imagens = [f for f in arquivos if f.lower().endswith(('jpg', 'jpeg', 'png', 'gif', 'bmp'))]

    # Expressão regular para encontrar arquivos já renomeados como "imagemX.extensão"
    padrao = re.compile(r"imagem(\d+)\.(jpg|jpeg|png|gif|bmp)", re.IGNORECASE)

    # Encontra o maior número já existente
    maior_numero = 0
    for imagem in imagens:
        match = padrao.match(imagem)
        if match:
            num = int(match.group(1))
            if num > maior_numero:
                maior_numero = num

    # Renomeia as imagens começando do maior número encontrado +1
    novo_numero = maior_numero + 1
    for imagem in imagens:
        caminho_antigo = os.path.join(pasta, imagem)
        extensao = os.path.splitext(imagem)[1].lower()  # Obtém a extensão do arquivo
        novo_nome = f"imagem{novo_numero}{extensao}"
        caminho_novo = os.path.join(pasta, novo_nome)

        # Evita renomear se o nome já estiver correto
        if caminho_antigo != caminho_novo:
            os.rename(caminho_antigo, caminho_novo)
            print(f"{imagem} -> {novo_nome}")

        novo_numero += 1  # Incrementa o número para a próxima imagem

# Exemplo de uso
pasta_imagens = "imagens/@Zehostilio96"  # Substitua pelo caminho real
renomear_imagens(pasta_imagens)
