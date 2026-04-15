class Smartphone:
    def __init__(self,model,battery,max_battery, power_on):
        self.model = model
        self.battery = battery
        self.max_battery = max_battery
        self.power_on = power_on

    def use_battery(self,amount):
        if self.battery <= 0 :
            print("전원이 꺼졌습니다")
        elif self.battery < amount :
            print("잔여배터리가 부족합니다")
        else:
            self.max_battery -= amount
            print(f"배터리 사용: {amount}")
    def charge(self, charger):
        if self.power_on == 0:
            print ("전원이 켜졌습니다")
            self.power_on = 1
        self.battery += charger.amount
        if self.battery > 100:
            self.battery = 100

        print(f"충전됨: {charger.amount} 현재: {self.battery}")
    
    def status(self):
        print(f"모델: {self.model} / 베터리: {self.battery}")

class Charger:
    def __init__(self,name,amount):
        self.name = name
        self.amount = amount
    

a = Smartphone("idk", 60, 100, True)
b = Charger("Charger 1", 30)

a.charge(b)
    

        