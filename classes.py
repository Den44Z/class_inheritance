


class Animal():
    def __init__(self,name,hitpoint,lifespan):
        self.name = name
        self.hitpoint = hitpoint
        self.lifespan = lifespan

    def get_damage(self):
        self.hitpoint = self.hitpoint - 1

caterpilar = Animal('Caterina',2,1)

caterpilar.get_damage()
print(caterpilar.hitpoint)


class Cat(Animal):
    def __init__(self, name, hitpoint, lifespan,lifecount):
        super().__init__(name, hitpoint, lifespan)
        self.lifecount = lifecount

    def get_damage(self):
        super().get_damage()
    def do_damage(self,animal):
        animal.hitpoint = animal.hitpoint- 1

billy_the_Cat = Cat('billy',9,140,9)

billy_the_Cat.do_damage(caterpilar)

if caterpilar.hitpoint <= 0 :
    print((caterpilar.hitpoint),'oh no Caterina died :( ')
else:
    print(f"{caterpilar.name} is still alive with {caterpilar.hitpoint} hitpoints.")