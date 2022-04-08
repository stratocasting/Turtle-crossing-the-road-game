from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
road_list = [-186,-164, -142, -120,  -102, -80, -22, 0, 22, 40]
road_list2= [300, 332, 360, 392]
class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        dice = random.randint(0, 7)
        if dice == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(x=random.choice(road_list2), y=random.choice(road_list))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)



