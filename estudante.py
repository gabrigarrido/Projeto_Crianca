class Estudante:
    def __init__(self):
        self.nome = ''
        self.idade = ''
        self.sexoB = ''
        self.olhos = ''
        self.pele = ''
        self.cabelo = ''
        self.tipoCabelos = ''



    def personagem(self): 
        print('Vamos montar seu personagem.')
        
        
        self.nome = str(input('Digite o nome para seu personagem: ').upper().strip())
        self.idade = int(input('Digite a idade para ele: '))
        self.sexoB = str(input('Escolha o sexo do seu personagem: [M/F]: ').upper().strip()[0])        
        self.olhos = str(input("""Escolha a cor dos olhos: 

                [0] Preto
                [1] Verde
                [2] Castanho
                [3] Azul        
        
        """).upper().strip()[0])
        # while True:
        #     if self.olhos != 0 or 1 or 2 or 3:
        #         print('Escolha invalida. Tente novamente.')
        #         self.olhos = str(input('Escolha a cor dos olhos: '))                
        #         break
        if self.olhos == 0:
            self.olhos = 'Olhos Pretos'
        elif self.olhos == 1:
            self.olhos = 'Olhos Verdes'
        elif self.olhos == 2:
            self.olhos = 'Castanhos'
        elif self.olhos == 3:
            self.olhos = 'Azuis'

        self.pele = str(input("""Escolha a cor da Pele: 

                [0] Preta
                [1] Branca
                [2] Amarela
                [3] Parda 
                [4] Indigêna
        
        """))
        if self.pele == 0:
            self.pele = 'Preta'
        elif self.pele == 1:
            self.pele = 'Branca'
        elif self.pele == 2:
            self.pele = 'Amarela'
        elif self.pele == 3:
            self.pele = 'Parda'
        elif self.pele == 4:
            self.pele = 'Parda'

        self.cabelo = str(input("""Escolha a cor dos Cabelos: 

                [0] Preto
                [1] Ruivo
                [2] Loiro
                       
        """))
        if self.cabelo == 0:
            self.cabelo = 'Preto'
        elif self.cabelo == 1:
            self.cabelo = 'Ruivo'
        elif self.cabelo == 2:
            self.cabelo = 'Loiro'


        self.tipoCabelos = str(input("""Escolha o tipo dos cabelos: 

                [0] Ondulados
                [1] Lisos
                [2] Cacheados
                [3] Crespos        
        
        """))
        if self.cabelo == 0:
            self.cabelo = 'Ondulados'
        elif self.cabelo == 1:
            self.cabelo = 'Lisos'
        elif self.cabelo == 2:
            self.cabelo = 'Cacheados'
        elif self.cabelo == 3:
            self.cabelo = 'Crespos'

        print(f"""Seu personagem ficou assim
        
        Seu nome é: {self.nome}.
        Com {self.idade} anos de idade.
        Sexo escolhido foi: {self.sexoB}.
        Com os olhos {self.olhos}.
        Pele cor {self.pele}.
        Cabelos {self.cabelo}.
        
        
        
        """)
       


        


        
       
            







    







        

