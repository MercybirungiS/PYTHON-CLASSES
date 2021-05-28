class Car():
    def __init__(self,car_Name,reg_no,car_model,car_color):
        self.car_Name=car_Name
        self.reg_No=reg_no
        self.car_model=car_model
        self.car_color=car_color
    def name(self):
        return "She bought an brand new {} car ".format(self.car_Name)
    def color(self):
        return "It is {} in color".format(self.car_color)
        