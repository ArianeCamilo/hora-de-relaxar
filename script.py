import time
import webbrowser

url = "index.html"
tempo_do_projeto_min = float(input("Qual é a duração do seu projeto (em minutos)? "))

tempo_do_projeto = tempo_do_projeto_min * 60

while tempo_do_projeto > 0:
    time.sleep(1800)
    webbrowser.open_new_tab(url)
    tempo_do_projeto -= 1800
