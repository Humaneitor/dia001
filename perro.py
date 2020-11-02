class Perro():
    def __init__(self, n, e, p):
        self.nombre = n
        self.edad = e
        self.peso = p
    
    def ladrar(self):
        if self.peso >= 8:
            print("Guau, Guau", self.nombre)
        else:
            print("guau, guau", self.nombre)
            
    def __str__(self):
        return "Perro{}, e: {} años, p: {} kilos".format(self.nombre, self.edad, self.peso)
    
            