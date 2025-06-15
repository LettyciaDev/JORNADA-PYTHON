#Passo1: entrar no sistema da empresa
    #link: https://dlp.hashtagtreinamentos.com/pythom/intensivao/login
#Passo2: fazer login
#Passo3: abrir o banco de dados da empresa
#Passo4: cadastrar um produtos
#Passo5: repetir o passo 4 até cadastrar todos os produtos

import pyautogui
from time import sleep

#pyautogui: automatiza o mouse, a tela e o teclado do computador
#Propriedades:
    # 1: pyautogui.press() : apertar uma tecla
    # 2: pyautogui.click() : clicar com o mouse
    # 3: pyautogui.write() : escreve um texto
    # 4: pyautogui.hotkey(): combinação de teclas (ctrl + c)
    # 5: pyautogui.scroll(): rolar a tela para cima e para baixo

pyautogui.PAUSE = 0.5

#Passo 1: entrar no sistema
#Abrir o navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

#entrar no link
pyautogui.write('https://dlp.hashtagtreinamentos.com/pythom/intensivao/login')
pyautogui.press('enter')

sleep(3)

pyautogui.click(x=3 ,y= 0)
