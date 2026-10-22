from enum import property


class Car:
    def __init__(self, model):
        self.__model = model

    # def get_model(self):
    #     return self.__model
    #
    # def set_model(self, model):
    #     if model < 2000:
    #         self.__model = 2000
    #     elif model > 2018:
    #         self.__model = 2018
    #     else:
    #         self.__model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if model < 2000:
            self.__model = 2000
        elif model > 2018:
            self.__model = 2018
        else:
            self.__model = model


car = Car(1998)
print(car.model)
car.model = 1998
print(car.model)
