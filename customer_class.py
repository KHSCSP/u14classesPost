class Customer:
    def __init__(self, nameP, numP, moneyP):
        self.name = nameP
        self.num = numP
        self.money = moneyP
    
    def add_money(self, amt):
        self.money += amt

    def __str__(self):
        return this.name + " has " + str(this.money)
    
    