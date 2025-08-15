import time
import os.path

def geralog(nome_arquivo):
    if os.path.isfile('log.txt') is False:
        print('Criando arquivo')
    else:
        print('Atualizando Log')

    capitulo = int(input('Digite o capítulo que você está: \n'))
    pagina = int(input('Digite a página que você está: \n'))

    arquivo = open(nome_arquivo, 'a')
    now = time.localtime()
    now_formatado = time.strftime('%d/%m/%y as %H:%M:%S', now)

    arquivo.write(f'Voce parou na pagina {pagina} do capitulo {capitulo} no dia {now_formatado}\n')
    arquivo.close()

geralog('log.txt')