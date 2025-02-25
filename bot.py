import pyautogui
import time
import keyboard  # Biblioteca para detectar teclas pressionadas

print("O script começará em 3 segundos... Pressione 'Espaço' para parar.")
time.sleep(3)

# Loop infinito até pressionar 'Espaço'
while True:
    # Se a tecla 'espaço' for pressionada, o loop para
    if keyboard.is_pressed('space'):
        print("\nExecução interrompida pelo usuário! 🚀")
        break

    # Primeiro clique (Botão Direito)
    x1, y1 = 742, 306
    pyautogui.click(x=x1, y=y1, button='right')
    print(f"1º Clique (Direito) em X={x1}, Y={y1}")

    time.sleep(3)  # Pausa entre cliques

    # Segundo clique (Botão Esquerdo)
    x2, y2 = 782, 368
    pyautogui.click(x=x2, y=y2, button='left')
    print(f"2º Clique (Esquerdo) em X={x2}, Y={y2}")

    time.sleep(2)

     # Segundo clique (Botão Esquerdo)
    x2, y2 = 782, 368
    pyautogui.click(x=x2, y=y2, button='left')
    print(f"2º Clique (Esquerdo) em X={x2}, Y={y2}")

    time.sleep(5)

    

    # Terceiro clique (Botão Esquerdo)    
    x3, y3 = 521, 444
    pyautogui.click(x=x3, y=y3, button='left')
    print(f"3º Clique (Esquerdo) em X={x3}, Y={y3}")

    time.sleep(3)

    # Quarto clique (Botão Esquerdo)
    x4, y4 = 1330, 375
    pyautogui.click(x=x4, y=y4, button='left')
    print(f"4º Clique (Esquerdo) em X={x4}, Y={y4}")

    

    print("Todos os cliques realizados! Reiniciando... Pressione 'Espaço' para parar.")
    time.sleep(3)  # Pequena pausa antes de reiniciar c o loop

 