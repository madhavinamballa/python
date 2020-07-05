class Car:
    def __init__(self,year,make):
        self.year=year
        self.make=make
        self.speed=0
    def accelerate(self):
    #Accelerate the car
        self.speed+=5
    def breaks(self):
    #cecelarete the car
        self.speed-=5
    def get_speed(self):
    #get the current speed of the car"
        return self.speed
def main():
    car1=Car("x","y")
    #call the accelerate function
    print("accelerating")
    for i in range(5):
        car1.accelerate()
        print(car1.get_speed())
        #call the brake function
        print("dcelerating")
    for i in range(5):
        car1.breaks()
        print(car1.get_speed())
if __name__ == "__main__":
    main()