class Hundar:
    def __init__(self, grupp, sektion, namn):
        self.__grupp = grupp                        
        self.__sektion = sektion                    
        self.__namn = namn

# privata variablerna genom ”name mangling” med dubbla understreck (__)        
# set och get metod för varje klass
    
    def set_grupp(self, grupp):                     
        self.__grupp = grupp
    
    def get_grupp(self):
        return self.__grupp
    
    def set_sektion(self, sektion):
        self.__sektion = sektion
    
    def get_sektion(self):
        return self.__sektion
    
    def set_namn(self, namn):
        self.__namn = namn
    
    def get_namn(self):
        return self.__namn
    
    def __str__(self):
        return f"Det finns {self.get_grupp()} grupper av hundar som delas i {self.get_sektion()} sektioner\n{self.get_namn()} tillhör grupp {self.get_grupp()} och sektion {self.get_sektion()} av hundraser"


# skapar en variabel i klass Hundar
# 10 grupper av hundar, "olika" för typen av sektioner, "Kompis" för namnet på hunden.
print("Uppgift 2 a") 
hund_svar = Hundar(10, "olika", "Kompis")
print(hund_svar)
print()


# Uppgift 2b:
# -----------

# sub-klass som ärver från klass Hundar
# super() ärver från huvudklass
class minHund(Hundar):
    def __init__(self, grupp, sektion, namn, ålder, färg):
        super().__init__(grupp, sektion, namn)
        self.__ålder = ålder
        self.__färg = färg
    
    def set_ålder(self, ålder):
        self.__ålder = ålder
    
    def get_ålder(self):
        return self.__ålder
    
    def set_färg(self, färg):
        self.__färg = färg
    
    def get_färg(self):
        return self.__färg
    
    def låt(self):
        return "voff, voff, voff!"

    def __str__(self):
        return f"{self.get_namn()} är {self.get_färg()} och är {self.get_ålder()} år gammal och säger {self.låt()}\n{super().__str__()}"


# Huvudprogram
print()
print("Uppgift 2 b") 
print()
hund1 = minHund(2, 1, "Boxer", 4, "brun")
print(hund1)
print()

hund1.set_ålder(5)
hund1.set_färg("röd")
print(hund1)
