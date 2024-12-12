class phone:
    def __init__(self,price,battery,type,charger):
        self.price=price
        self.battery=battery
        self.type=type
        self.charger=charger

    def display_information(self):
        print(f"Price: {self.price},\nBattery: {self.battery}, \nType: {self.type}, \nCharger: {self.charger}")

Oppo = phone ("200000" , "100%" , "Oppo" , "Normal charger")
Oppo.display_information()