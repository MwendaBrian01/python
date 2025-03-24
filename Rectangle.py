class Rectangle:
    def __init__(self, length, width):  
        self.length = length
        self.width = width

    def area(self):
            return  self.length*self.width
    def perimeter(self):
          return  2*(self.length+self.width)
    
rect= Rectangle(2,5)


print(f"area:{rect.area()}")
print(f"perimeter:{rect.perimeter()}")
    

    


    
        
