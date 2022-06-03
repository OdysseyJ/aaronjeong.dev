from abc import *



class Beverage(metaclass=ABCMeta):
    description = "제목 없음"

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self):
        raise NotImplementedError()


# Beverage 클래스가 들어갈 자리에 들어갈 수 있어야 하므로 Beverage를 상속
class CondimentDecorator(Beverage):
    beverage: Beverage

    @abstractmethod
    def get_description(self):
        raise NotImplementedError()

    @abstractmethod
    def cost(self):
        raise NotImplementedError()

class Espresso(Beverage):
    def __init__(self):
        self.description = "에스프레소"

    def cost(self):
        return 1.99

class HouseBlend(Beverage):
    def __init__(self):
        self.description = "하우스 블렌드 커피"

    def cost(self):
        return 0.89

class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", 모카"

    def cost(self):
        return self.beverage.cost() + 0.2

class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", 휘핑"

    def cost(self):
        return self.beverage.cost() + 0.1


beverage1: Beverage = Espresso()
beverage1 = Mocha(beverage1)
beverage1 = Mocha(beverage1)
beverage1 = Whip(beverage1)
print(beverage1.cost())