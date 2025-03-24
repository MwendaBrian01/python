class circle:
    def __init__ (self,radius):
      self.radius= radius
    def area(self):
        return 3.14*  (self.radius*self.radius)

    def circumference(self):
      return 3.14*(self.radius+self.radius)
circ = circle(7)
print(f"Area:{circ.area()}")
print(f"circumference:{circ.circumference()}")
