import pyautogui
import time

print("Posicione o mouse onde deseja capturar a coordenada. Capturando em 3 segundos...")
time.sleep(10)  # Espera 3 segundos

# Captura a posição do mouse
x, y = pyautogui.position()

# Exibe a coordenada capturada
print(f"Coordenadas capturadas: X={x}, Y={y}")
