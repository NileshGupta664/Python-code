class test:
    def myfun(self):
        print("this is function1")
class test2(test):
     def myfun(self):
          print("this is function2 ")
obj=test2()
obj.myfun()