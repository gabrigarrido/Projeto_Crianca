from caracteristicas import Caracteristicas # import das classes e bibliotecas
from acoes import Acoes
import os
# **********************************************
crianca = Caracteristicas() # Não lembro como se chama quando coloca as classes aqui
crianca = Acoes()
crianca.levantar()
status = []
horas = 6
minutos = 0
#**********************************************
while True: # validação das escolhas
        while crianca.horas < 18:
                escolha = int(input(''))
                
                if escolha == 0:  
                        crianca.tomarBanho()                             
                elif escolha == 1: 
                        crianca.cafe()                             
                elif escolha == 2:
                       crianca.brincadeira()
                elif escolha == 3:
                       crianca.comida()
                elif escolha == 4:
                        crianca.irEscola()
                elif escolha == 5:
                        crianca.estudar()
                elif escolha == 6: 
                        crianca.tirarCochilo()
                elif escolha == 7:
                        print('|||||Fim do Jogo! Volte sempre.|||||')
                        break         
                else:
                        print('Escolha invalida. Tente novamente')
        else:
                        print('Fim do dia! Hora de dormir, Boa noite!')
                        break
               
        
                
                
          

               


