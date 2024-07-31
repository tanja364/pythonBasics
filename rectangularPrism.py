class Rectangle:
    def __init__(self, c, l, w):
        self.colour=c
        self.length=l
        self.width=w
    def perimeter(self):
        self.perimeter = 2*self.width + 2*self.length
        return self.perimeter
    def area(self):
        self.area = self.length * self.width
        return self.area
    def diagonal(self):
        self.diagonal = (self.width**2 + self.length**2)**(1/2)
        return self.diagonal
    def volume(self, h):
        self.height = h
        self.volume=self.length*self.width*self.height
        return(self.volume)
rect1=Rectangle('blue', 3, 6)
rect2=Rectangle('yellow', 6, 9)
print('rect1 length = ',rect1.length)
print('rect1 width = ', rect1.width)
print('rect1 area =', rect1.area())
print('rect1 perimeter = ',rect1.perimeter())
print('rect1 diagonal = ', rect1.diagonal())
print('rect1 colour = ',rect1.colour)
print('rect2 length = ', rect2.length)
print('rect2 width = ', rect2.width)
print('rect2 area = ', rect2.area())
print('rect2 perimeter = ',rect2.perimeter())
print('rect2 diagonal = ',rect2.diagonal())
print('rect2 colour = ', rect2.colour)

vol1 = rect1.volume(1)
vol2 = rect2.volume(3)

print('rect1 volume = ',vol1)
print('rect2 volume = ',vol2)