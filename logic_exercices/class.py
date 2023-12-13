class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
   
    def setMarca (self, marca):
        self.marca = marca
 
    def setModelo (self, modelo):
        self.modelo = modelo
 
    def setAno (self, ano):
        self.ano = ano
 
    def getMarca (self):
        return self.marca
   
    def getModelo (self):
        return self.modelo
   
    def getAno (self):
        return self.ano