# POLIMORFISMO

class Programa:
    def __init__(self, nome, ano):
        self._nome=nome.title()
        self.ano=ano
        self._likes=0
        
    @property
    def likes(self):
        return self._likes
    
    def dar_likes(self):
        self._likes+=1
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome=nome
        
    def imprime(self):
        print(f'{self._nome} - {self.ano}  - {self._likes}')

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao=duracao
        
    def imprime(self):
        print(f'Nome: {self._nome} - Ano: {self.ano} - Duração: {self.duracao} - Likes: {self._likes}')

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas=temporadas
        
    def imprime(self):
        print(f'Nome: {self._nome} - Ano: {self.ano} - Temp: {self.temporadas} - Likes: {self._likes}')

filme1=Filme('star wars', 1977, 132)
filme1.dar_likes()
serie1=Serie('greys anatomy', 2005, 20)
serie1.dar_likes()

# 1 criando um list para armazenar os objetos
filmes_e_series=[filme1, serie1]

# escrever um if que verifica dentro do nosso for se cada interação possui determinado atributo
#for programa in filmes_e_series:
#    detalhes=programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
#    print(f'{programa.nome} - {programa.temporadas} - {programa.likes} likes')

for programa in filmes_e_series:
    programa.imprime()
    