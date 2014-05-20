class Rectangle(object):
    def __init__(self,width=1, height=2):
        self.width = width
        self.height = height
   
    def area(self):
        return self.width * self.height 
           
    def perimeter(self):
        return 2 * self.width + 2 * self.height