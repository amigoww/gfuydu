class Human:
    def eat_spaghetti(self):
        print("Я могу есть спагетти")
class Robot:
    def drink_oil(self):
        print("Я могу потреблять машинное масло")

class Cyborg(Human, Robot):
    pass

cyborg = Cyborg()

print(cyborg.eat_spaghetti())
print(cyborg.drink_oil())