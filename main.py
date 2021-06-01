from caracteristicas import Caracteristicas # import das classes e bibliotecas
from acoes import Acoes
# **********************************************
crianca = Caracteristicas() # Instanciar um objeto
crianca.personagem()
crianca = Acoes()
crianca.levantar()
status = []
horas = 6
minutos = 0
#**********************************************
while True: # validação das escolhas
        while crianca.horas < 18: 
                crianca.vizual()                
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
                     
        if crianca.horas >= 18:
                print("""
        ---------------------------------------------------------------------------
            -----<<<<<< SEU DIA CHEGOU AO FIM, HORA DE DORMIR. BOA NOITE!! >>>>>>-----
        ---------------------------------------------------------------------------
            """) 
                break
               
        
                
                
          

               


