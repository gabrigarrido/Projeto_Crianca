class Caracteristicas:
    def __init__(self):
        self.nome = ''
        self.idade = ''
        self.sexoB = ''
        self.olhos = ''
        self.pele = ''
        self.cabelo = ''
        self.tipoCabelos = ''



    def personagem(self):
        print("""
        ---------------------------------------------------------------------------
            -----<<<<<<<<BEM VINDO AO JOGO DE VIDA VIRTUAL DA BLUE>>>>>>>>-----
        ---------------------------------------------------------------------------
            """) 
        print()
        print('<><><><><> VAMOS MONTAR SEU PERSONAGEM <><><><><>')
        print()
        
        
        self.nome = str(input('>>> Digite o nome para ele(a): ').upper().strip())
        self.idade = int(input('>>> Digite a idade para ele(a): '))
        while True:
            if self.idade < 6 or self.idade > 12:
                print('*** Idade invalida ***')
                self.idade = int(input('>>> Digite a idade para ele(a): '))
            else:
                break       
        self.sexoB = str(input('>>> Escolha o sexo do seu personagem: [M/F]: ').upper().strip()[0])
        while self.sexoB not in 'MF':            
            print('*** Sexo Invalido ***')
            self.sexoB = str(input('>>> Escolha o sexo do seu personagem: [M/F]: ').upper().strip()[0])
                        
        tipoOlhos = int(input("""Escolha a cor dos olhos: 

                [0] Preto
                [1] Verde
                [2] Castanho
                [3] Azul        
        
        """))
        if tipoOlhos == 0:
            self.olhos = 'Pretos'
        elif tipoOlhos == 1:
            self.olhos = 'Verdes'
        elif tipoOlhos == 2:
            self.olhos = 'Castanhos'
        elif tipoOlhos == 3:
            self.olhos = 'Azuis'
        else:
            while True:
                if tipoOlhos < 0 or tipoOlhos > 3:
                    print('*** Escolha Invalida ***')
                    tipoOlhos = int(input('>>> Escolha a cor dos olhos:: '))
                else:
                    break 
        pele = int(input("""Escolha a cor da Pele: 

                [0] Preta
                [1] Branca
                [2] Amarela
                [3] Parda 
                [4] Indigêna
        
        """))
        if pele == 0:
            self.pele = 'Preta'
        elif pele == 1:
            self.pele = 'Branca'
        elif pele == 2:
            self.pele = 'Amarela'
        elif pele == 3:
            self.pele = 'Parda'
        elif pele == 4:
            self.pele = 'Indigêna'
        else:
            while True:
                if pele < 0 or pele > 4:
                    print('*** Escolha Invalida ***')
                    pele = int(input('>>> Escolha a cor da Pele: '))
                else:
                    break 
        cabelo = int(input("""Escolha a cor dos Cabelos: 

                [0] Preto
                [1] Ruivo
                [2] Loiro
                       
        """))
        if cabelo == 0:
            self.cabelo = 'Preto'
        elif cabelo == 1:
            self.cabelo = 'Ruivo'
        elif cabelo == 2:
            self.cabelo = 'Loiro'
        else:
            while True:
                if cabelo < 0 or cabelo > 2:
                    print('*** Escolha Invalida ***')
                    cabelo = int(input('>>> Escolha a cor dos Cabelos: '))
                else:
                    break 

        tipoCabelos = int(input("""Escolha o tipo dos cabelos: 

                [0] Ondulados
                [1] Lisos
                [2] Cacheados
                [3] Crespos        
        
        """))
        if tipoCabelos == 0:
            self.tipoCabelos = 'Ondulados'
        elif tipoCabelos == 1:
            self.tipoCabelos = 'Lisos'
        elif tipoCabelos == 2:
            self.tipoCabelos = 'Cacheados'
        elif tipoCabelos == 3:
            self.tipoCabelos = 'Crespos'
        else:
            while True:
                if tipoCabelos < 0 or tipoCabelos > 3:
                    print('*** Escolha Invalida ***')
                    tipoCabelos = int(input('>>> Escolha o tipo dos cabelos: '))
                else:
                    break 
        
        print("""
        ---------------------------------------------------------------------------
            -----<<<<<< ESSE É SEU PERSONAGEM COM AS CARACTERISTICAS QUE ESCOLHEU >>>>>>-----
        ---------------------------------------------------------------------------
            """) 
        print(f"""
        
                     ><>< Seu nome é: {self.nome}.
                     ><>< Com {self.idade} anos de Idade.
                     ><>< Sexo escolhido foi: {self.sexoB}.
                     ><>< Com os olhos {self.olhos}.
                     ><>< Pele cor {self.pele}.
                     ><>< Cabelos {self.cabelo}.
                     ><>< Tipo dos Cabelos {self.tipoCabelos}.
                            
        
        
        """)
       


        


        
       
            







    







        

