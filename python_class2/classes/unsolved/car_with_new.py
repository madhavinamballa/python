class Car:
    def __init__(self,year,make,color,moonroof,autopilot):
        self.year=year
        self.make=make
        self.color=color
        self.moonroof=moonroof
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
    def totalcost(self,color,moonroof):
        basecost=1000
        if color=="red":
            basecost=basecost+1000
        elif color=="blue":
            basecost=basecost+5000
        elif color=="grey":
            basecost=basecost+5000
        elif color=="white":
            basecost=basecost
        return basecost


def main():
    color=input("choose a color \
        red,blue,white,grey")
    moonroof=input("enter yes or no: ")
    autodrive=input("enter yes or no: ")
    car1=Car("x","y",color,moonroof)
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
    print(car1.totalcost(color,moonroof))
if __name__ == "__main__":
    main()