import pyautogui
import pyperclip

pyautogui.click 

pyautogui.keyDown ("botao")# Deixa precionado o botao

pyautogui.keyUp( 'botao') # Despreciona o botao

pyautogui.press( 'botao') # Da um click no botao

pyautogui.write('texto') # Escreve um texto, porem nao escreve caracters coringas(?,!)

pyautogui.hotkey('botao1', 'botao2', '....etc') # Comando de atalhos, permitindo precionar mais de um botao


# EXEMPLOS 

#pyautogui.keyDown( 'Alt')
#pyautogui.press( 'tab')
#pyautogui.keyUp( 'Alt')
#pyautogui.write('Ola, como vai')
#pyautogui.press( 'Tab' )
#pyautogui.click( 'Ctrl', 'c' )
#pyautogui.click( 'Ctrl', 'v')