def Overloading_inheritance(a,b,c):
    class Vehicle:
        def __init__(self,capacity=50):
            self.capacity=capacity

    class Bus(Vehicle):
        def __init__(self,name,max_speed,mileage,capacity=50):
            super().__init__(capacity)
            self.name=name
            self.mileage=mileage
            self.max_speed=max_speed

        def seating_capacity(self):

            print("The seating capacity of a",self.name,"with maxspeed",self.max_speed,"and mileage",self.mileage ,"is", self.capacity,"passengers")


    School_bus=Bus(a,b,c)
    School_bus.seating_capacity()
