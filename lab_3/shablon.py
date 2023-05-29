from abc import ABC, abstractmethod

class Algorithm(ABC):
    def template_method(self):
        self.make_food()
        self.first_step()
        self.second_step()
        self.third_step()
        self.done_food()
        self.printer()

    def make_food(self):
        print("Выбрать цветы")

    @abstractmethod
    def first_step(self):
        pass

    @abstractmethod
    def second_step(self):
        pass
    @abstractmethod
    def third_step(self):
        pass

    def done_food(self):
        print("Букет готов!")

    def printer(self):
        n=50
        print("*" * n) 

class part:
    def doublebulk(self):
        print("Собрать цветы")
    def onebulk(self):
        print("Вставить цветы в оазис")
    def meat(self):
        print("Подрезать стебли")
    def vegetables(self):
        print("Убрать шипы")
    def sasuage(self):
        print("Убрать листья")
    def ketchunes(self):
        print("Обернуть упаковочной бумагой")
    def kolbasa(self):
        print("Перевязать ленточкой")
class burger(Algorithm):
    def first_step(self):
        make = part()
        make.doublebulk()
    def second_step(self):
        make = part()
        make.vegetables()
    def third_step(self):
        make = part()
        make.meat()
    def done_food(self):
        print("Букет готов!")
class hotdog(Algorithm):
    def first_step(self):
        make = part()
        make.doublebulk()
    def second_step(self):
        make = part()
        make.ketchunes()
    def third_step(self):
        make = part()
        make.sasuage()
    def done_food(self):
        print("Композиция готова!")

print("Делаем Букет")
burg = burger()
burg.template_method()

print("Составляем композицию")
hot = hotdog()
hot.template_method()

