# Skriv in din kod för Uppgift 2 här nedan
# ----------------------------------------

# Uppgift 2a:
# -----------

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
        return f"Det finns {self.get_grupp()} grupper av hundar som delas i {self.get_sektion()} sektioner"

    def __str__(self):
        return f"{self.get_namn()} tillhör grupp {self.get_grupp()} och sektion {self.get_sektion()} av hundraser"


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
        return f"{self.get_namn()} är {self.get_färg()} och är {self.get_ålder()} år gammal och säger {self.låt()}\n{super().__str__()}\nNamn: {self.get_namn()}\nÅlder: {self.get_ålder()}\nFärg: {self.get_färg()}"


# Huvudprogram
print()
print("Uppgift 2 b") 
print()
hund1 = minHund(2, 1, "Boxer", 4, "brun")
print(hund1)
print("__________________")

print("Vi ändrar hundfärg") 
print("__________________")
hund1.set_ålder(5)
hund1.set_färg("röd")
print(hund1)


# Uppgift 2c:
# -----------

def hund_lista():
    hund_list = []
    while True:
        antal_hundar = int(input("Hur många hundar har du? "))
        for _ in range(antal_hundar):
            grupp = input("Skriv in rasgruppen som din hund tillhör: ")
            sektion = input("Skriv in sektion som din hund tillhör: ")
            namn = input("Skriv in namn på din hund: ")
            ålder = int(input("Skriv in din hunds ålder: "))
            färg = input("Skriv in din hunds färg: ")
            
            hund = minHund(grupp, sektion, namn, ålder, färg)
            hund_list.append(hund)
            
            # För att avsluta loopen
            fortsätt = input("Vill du lägga till fler hundar? (ja/nej) ")
            if fortsätt.lower() != "ja":
                return hund_list

def visa_hund_data(hund_list):
    print("Rasgrupp   Sektion   Namn     Ålder     Färg")
    print("=" * 50)
    
    for hund in hund_list:
        print(f"{hund.get_grupp():<11}{hund.get_sektion():<10}{hund.get_namn():<12}{hund.get_ålder():<7}{hund.get_färg()}")

# Huvudprogram
print("Uppgift 2 c")
print()
alla_hundar = hund_lista()
visa_hund_data(alla_hundar)
print()



