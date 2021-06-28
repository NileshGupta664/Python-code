class rectangle:
    def rec_area(self,height,width):
        area=height*width
        print("area of rectangle is:",area)
class square(rectangle):
    def squ_area(self,side):
        area=side*side
        print("area of square",area)
obj=square()
obj.rec_area(10,20)
obj.squ_area(5)