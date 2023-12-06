class Calculadora:
    
    def __init__(self, array_numero, operador):
        self.array_numero = array_numero
        self.operador = operador
   
    def setArray (self, array_numero):
        self.array_numero = array_numero
 
    def setOperador (self, operador):
        self.operador = operador
 
    def getMedia (self):
        #faz a soma do array e divide pela quantidade de numeros