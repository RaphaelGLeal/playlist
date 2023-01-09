import pygame
import emoji

from time import sleep


print("1 - Projota \n2 - Ana Vitoria \n3 - Marcelo D2 \n4 - Zeno e Henrique")
print('-'*30)
escolha = int(input('\nDigite o Numero da musica: '))
musica = ''

if escolha == 1:
   musica = 'projota.mp3'
elif escolha == 2:
    musica = 'anavitoria.mp3'
elif escolha == 3:
    musica = 'marcelod2.mp3'
elif escolha == 4:
    musica = 'zeneto.mp3'
else:
    print(emoji.emojize('Opção errada! :warning: \n Digite uma opção Valida entre 1 e 4'))
    #print(emoji.emojize('Opção errada! :warning: \n Digite uma opção Valida entre 1 e 4',use_aliases=True))

print('-'*30)
print('\nSua escolha foi {}'.format(musica))
#print('-'*20)

pygame.mixer.init()
pygame.mixer.music.load(musica)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    print('-'*30)
    pause = int(input('1 para pausar\n2 para play \n3 para finalizar \nOpção Desejda: '))
    if pause == 1:
        pygame.mixer.music.pause()
    elif pause == 2:
        pygame.mixer.music.unpause()
    elif pause == 3:
        print('Musica Finalizada em 3seg.')
        sleep(5)
        pygame.mixer.music.quit()    
input()
pygame.event.wait()

sleep(5)
