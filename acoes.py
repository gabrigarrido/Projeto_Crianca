class Acoes:
    def __init__(self):              
        self.status = []
        self.horas = 6
        self.minutos = 0

    def vizual(self):
        print("""      
                [0] Tomar Banho
                [1] Tomar Café 
                [2] Brincar
                [3] Comer
                [4] Escola
                [5] Estudar
                [6] Soneca 
        """) 
    
    def levantar(self):
        print('<<<<>>>> Seu dia inicia quando você estiver pronto!<<<<>>>>')
        print()
        resposta = str(input('Você irá levantar? [S/N] ').upper())
        while True:
            if resposta == 'S':
                print('Seu dia começou! Escolha suas ações: ')
                break
            else:
                print('Você está perdendo um lindo dia!')
                resposta = str(input('Você irá levantar agora? [S/N] ').upper())

    def tomarBanho(self):
        self.minutos = 0
        self.minutos += 30 
        self.horas += 1                       
        if 'Está limpo' not in self.status:                               
            self.status.append('Está limpo')                           
            print(self.status)  
            print(f'Relogio : {self.horas}:{self.minutos} AM') 
            return self.status

    def cafe(self):
        self.minutos = 0
        self.horas +=1                  
        if 'Está sem fome' not in self.status:                               
            if self.horas < 10:                            
                self.status.append('Está sem fome')
                print(self.status)  
                print(f'Relogio : {self.horas}:{self.minutos}0 AM')
                return self.status 
            else:
                print('Não é mais horario para tomar café.')
                return self.status       

    def brincadeira(self):
        self.minutos = 0        
        self.horas += 2                      
        if 'Já brincou' not in self.status:                               
            self.status.append('Já brincou')                           
            print(self.status)  
            print(f'Relogio : {self.horas}:{self.minutos} AM') 
            return self.status
        
    def comida(self):
        self.minutos = 0        
        self.horas += 1                      
        if 'Já comeu' not in self.status:                               
            self.status.append('Já comeu')                           
            print(self.status)  
            print(f'Relogio : {self.horas}:{self.minutos} AM') 
            return self.status

    def irEscola(self):
        self.minutos = 0        
        self.horas += 4
        print('Você irá para a sala ou irá matar aula no patio?')
        print("""
                [8] Sala
                [9] Matar Aula
        """)  
        opcao = int(input(''))
        if opcao == 8 :
            if 'Teve boa aula' not in self.status:                               
                self.status.append('Teve boa aula')                           
                print(self.status)  
                print(f'Relogio : {self.horas}:{self.minutos} AM') 
                return self.status        
        elif opcao == 9:
            if 'Matou aula e perdeu pontos' not in self.status:                               
                    self.status.append('Matou aula e perdeu pontos')                           
                    print(self.status)  
                    print(f'Relogio : {self.horas}:{self.minutos} AM') 
                    return self.status
        else: 
            print('Escolha invalida! Tente Novamente')
            while True:
                print('Escolha invalida! Tente Novamente')
                print("""
                [8] Sala
                [9] Matar Aula
    
            """)

    def estudar(self):
        self.minutos = 0        
        self.horas += 2                      
        if 'Estudou bem' not in self.status:                               
            self.status.append('Estudou bem')                           
            print(self.status)  
            print(f'Relogio : {self.horas}:{self.minutos} AM') 
            return self.status

    def tirarCochilo(self):
        self.minutos = 0        
        self.horas += 1                      
        if 'Está sem sono' not in self.status:                               
            self.status.append('Está sem sono')                           
            print(self.status)  
            print(f'Relogio : {self.horas}:{self.minutos} AM') 
            return self.status

   




        


            

    