 ###Using object oriented programming scheme (OOPS) kindly complete the following tasks which is given as below
 ###Create a python class called circle with constructor which will take a list as an argument for the task
 ###The list is [10,501,22,37,100,999,87,351].

## list=[10,501,22,37,100,999,87,351]


def circle(l):
     print(l)
     print(type(l))
     for i in l:
         print(i)
lst =[10,501,22,37,100,999,87,351]
circle(lst)

###Create a proper member variables inside the task if required and use them when necessary.
###For example for this task create a class private variable named pi=3.141.

class Circle:
    __PI=3.141
    def __init__(self, radius):
     self.radius = radius
    def area(self):
     return (Circle.__PI * self.radius * self.radius)
c1 = Circle(3)
print("area of c1 Circle is", c1.area())

###From the given List create two classes Methods Area and perimeter which will be going to calculate the Area
### and Perimeter.
class _Circle:
     __PI = 3.141
     def __init__(self, diameter):
      self.diameter = diameter
     def perimeter(self):
         return (Circle.__PI * self.diameter)
c2=_Circle(4)
print("perimeter of c1 Circle is", c2.perimeter())


###Kindly visit the URL and convert the UML diagram in to a Python Class and its methods.
 class TvClass:

     def __init__(self, brand, price, inches, OnOFF, volume=50, channel=1):
         self.brand = brand
         self.price = price
         self.inches = inches
         self.OnOFF = OnOFF
         self.volume = volume
         self.channel = channel

     def increaseVolume(self):
         if self.volume < 100:
             self.volume += 1

     def decreaseVolume(self):
         if self.volume > 0:
             self.volume -= 1

     def changeChannel(self, channelNumber):
         if 0 <= channelNumber <= 50:
             self.channel = channelNumber

     def reset(self):
         self.channel = 1
         self.volume = 50

     def showStatus(self):
         print(f"{self.brand} at channel {self.channel}, volume {self.volume}")


 class Plasma(TvClass):
     pass


 class LEDTv(TvClass):
     pass


 plasma = Plasma("Sony", 100000, 50, "on")
 plasma.showStatus()
 plasma.increaseVolume()
 plasma.increaseVolume()
 plasma.changeChannel(29)
 plasma.showStatus()

class LED_Plasma(TvClass):
    pass
   def __init__(self, thickness, energy_usage, Lifespan, Refresh_rate,viewing_angle, backlight,Display_details):
     self.thickness = thickness
     self.energy_usage = energy_usage
     self.Lifespan = Lifespan
     self.Refresh_rate = Refresh_rate
     self.viewing_angle = viewing_angle
     self.backlight = backlight
     self.Display_details = Display_details
