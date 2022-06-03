from abc import *


class FlyBehavior(metaclass=ABCMeta):
    def fly(self):
        pass


class FlyWithWing(FlyBehavior):
    def fly(self):
        print("날개로 날기")


class FlyWithRocket(FlyBehavior):
    def fly(self):
        print("로켓으로 날기")


class QuackBehavior(metaclass=ABCMeta):
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print("그냥꽥꽥")


class SlowQuack(QuackBehavior):
    def quack(self):
        print("꽤액")


class Duck(metaclass=ABCMeta):
    fly_behavior: FlyBehavior
    quack_behavior: QuackBehavior

    def perform_quack(self):
        return self.quack_behavior.quack()

    def perform_fly(self):
        return self.fly_behavior.fly()

    def swim(self):
        print("헤엄치기")

    def quack(self):
        print("꽥꽥")

    def set_fly_behavior(self, fly_behavior: FlyBehavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior: QuackBehavior):
        self.quack_behavior = quack_behavior

    @abstractmethod
    def display(self):
        raise NotImplementedError()


class YellowDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWing()
        self.quack_behavior = Quack()

    def display(self):
        print("노란오리")


class RubberDuck(Duck):
    def quack(self):
        print("삑삑")

    def display(self):
        print("고무오리")


yellow_duck = YellowDuck()
yellow_duck.perform_fly()
yellow_duck.set_fly_behavior(fly_behavior=FlyWithRocket())
yellow_duck.perform_fly()
