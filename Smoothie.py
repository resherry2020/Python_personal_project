class Smoothie:
    ingregient_table = {
        "Strawberries":1.5,
        "Banana":0.5,
        "Mango":2.5,
        "Blueberries":1,
        "Raspberries":1,
        "Apple":1.75,
        "Pineapple":3.5
    }
    def __init__(self,ingre):
        self.ingregients = ingre
        self.cost = 0
        self.name = ''
        
    def get_cost(self):
        for x in self.ingregients:
            if x in self.ingregient_table.keys():
                self.cost += self.ingregient_table[x]
        return self.cost
    
    def get_price(self):
        return round(self.cost * 1.5,2)
    
    def get_name(self):
        if len(self.ingregients) > 1:
            for n in self.ingregients:
                if 'berries' in n:
                    n = n.replace('berries',"berry")
                    self.name += n + ' '
            self.name += "Fusion"    
        else:    
            self.name = self.ingregients[0] + ' ' + "Smoothie"
        return self.name
    
    
s1 = Smoothie(["Banana"])
print(s1.ingregients)
s1.get_cost()
s1.get_price()
s1.get_name()
            
            
s2 = Smoothie(["Raspberries", "Strawberries", "Blueberries"])
print(s2.ingregients)
s2.get_cost()
s2.get_price()
s2.get_name()            
    
    
        
    
    
        
    
        
