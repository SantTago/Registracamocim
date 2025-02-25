import pyautogui
import time

# Definir o intervalo entre cada rolagem (em segundos)
interval = 0.1 # Ajuste conforme necessário

try:
    while True:
        pyautogui.scroll(100)  # Rola para cima mais devagar
        time.sleep(interval)  # Aguarda antes da próxima rolagem
except KeyboardInterrupt:
    print("Interrompido pelo usuário.")