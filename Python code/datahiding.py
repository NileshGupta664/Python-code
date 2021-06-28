class test:
    __x=10
    y=20
    def myfun1(self):
        print("this is function1")
class test2(test):
     def myfun2(self):
          print("this is function2 ")
          print(self.x)
          self.myfun1()
obj=test2()
obj.myfun2()