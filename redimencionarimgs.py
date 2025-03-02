from PIL import Image
import os

def resize_images(input_folder, height=800):
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'webp')):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            
            # Calcular nova largura proporcional
            aspect_ratio = img.width / img.height
            new_width = int(height * aspect_ratio)
            
            img = img.resize((new_width, height), Image.LANCZOS)
            img.save(img_path, optimize=True, quality=85)
            print(f"Imagem redimensionada: {img_path}")

# Caminho da pasta de imagens
input_folder = "imagens/@raquelsiqueira"

# Chamar a função para redimensionar as imagens mantendo a proporção
resize_images(input_folder)