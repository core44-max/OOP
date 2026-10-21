class Camera:
    def camera_method(self):
        print('Это родительский метод из класса Camera')

class Radio:
    def radio_method(self):
        print('Это родительский метод из класса Radio')

class Cellphone(Camera, Radio):
    def cell_phone_method(self):
        print('Это дочерный метод из класса Cellphone')

obj = Cellphone()
obj.cell_phone_method()
obj.camera_method()
obj.radio_method()


