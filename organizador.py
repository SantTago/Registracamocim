import os

def renomear_imagens(pasta):
    # Obtém a lista de arquivos na pasta
    arquivos = sorted(os.listdir(pasta))
    
    # Filtra apenas os arquivos de imagem
    imagens = [f for f in arquivos if f.lower().endswith(('jpg', 'jpeg', 'png', 'gif', 'bmp'))]
    
    # Renomeia as imagens
    for i, imagem in enumerate(imagens, start=1):
        extensao = os.path.splitext(imagem)[1]  # Obtém a extensão do arquivo
        novo_nome = f"imagem{i}{extensao}"  # Define o novo nome
        caminho_antigo = os.path.join(pasta, imagem)
        caminho_novo = os.path.join(pasta, novo_nome)
        
        os.rename(caminho_antigo, caminho_novo)
        print(f"{imagem} -> {novo_nome}")

# Exemplo de uso
pasta_imagens = "@centromedico"  # Substitua pelo caminho real
renomear_imagens(pasta_imagens)
