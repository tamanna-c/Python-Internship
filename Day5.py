#Task-1
"""class Hello:
    def myfunction(self):
        print("This is a method of class hello")
a=Hello()
a.myfunction()"""

#Task-2
"""class Hello:
    def myfunction(self):
        print("This is a method of class hello")

    def show(self,name):
        print("Value is",name)
a=Hello()
a.myfunction()
a.show("Tamanna")"""

#Task-3
"""class Myclass:
    def func1(self,n1,n2):
        ans=n1+n2
        print("Ans is :",ans)
a=Myclass()
a.func1(14,78)"""

#Task-4
"""class Hello:
    def myfunction(self):
        print("This is a method of class hello")

    def show(self,name):
        print("Value is",name)
    
    def __init__(self):
        print("This is hello class")
a=Hello()
a.myfunction()
a.show("Tamanna")"""

#Task-5
"""class Hello:
    def myfunction(self):
        print("This is a method of class hello")

    def show(self,name):
        print("Value is",name)
    
    def __init__(self,nm):
        print("This is hello class")
        print("Name is:",nm)
a=Hello("Tara")
a.myfunction()
a.show("Tamanna")"""

#Task-6
"""class Hello:
    name=""
    def func1(self):
        print("This is a method of class hello")
    
    def func2(self,name):
        self.name=name

    def show(self):
        print("Name is",self.name)
    
a=Hello()
a.func1()
a.func2("Tamanna")
a.show()"""

#Task-7
"""class Myclass:
    n1=0
    n2=0
    
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    
    def func1(self):
        ans=self.n1+self.n2
        print("Ans is:",ans)
a=Myclass(90,76)
a.func1()"""

#Task-8
"""class Myclass:
    def func1(self):
        print("This is parent class method")

class Myclass1(Myclass):
    def func2(self):
        print("This is child class method")

a=Myclass1()
a.func1()
a.func2()"""

#Task-9
"""class Myclass:
    def func1(self):
        print("This is parent class method")

class Myclass1(Myclass):
    def func2(self):
        print("This is child class method")

a=Myclass1()
a.func1()
a.func2()"""

#Task-10
"""class Myclass:
    def __init__(self):
        print("This is Myclass")

    def func1(self):
        print("This is parent class method")

class Myclass1(Myclass):
    def __init__(self):
        print("This is Myclass1")
    def func2(self):
        print("This is child class method")

class Myclass2(Myclass1):
    def func3(self):
        print("This is child class method of myclass1")
a=Myclass2()
a.func1()
a.func2()
a.func3()"""

#Task-11
"""class Myclass:
    def __init__(self):
        print("This is Myclass")

    def func1(self):
        print("This is parent class method")

class Myclass1:
    def __init__(self):
        print("This is Myclass1")
    def func2(self):
        print("This is parent class method")

class Myclass2(Myclass,Myclass1):
    def func3(self):
        print("This is child class method of myclass1")
a=Myclass2()
a.func1()
a.func2()
a.func3()"""

#Task-12
"""class Myclass:
    def __init__(self):
        print("This is Myclass")

    def func1(self):
        print("This is parent class method")

class Myclass1(Myclass):
    def __init__(self):
        print("This is Myclass1")
    def func2(self):
        print("This is child class method")

class Myclass2(Myclass):
    def func3(self):
        print("This is child class method of myclass1")
a=Myclass1()
a.func1()
a.func2()
b=Myclass2()
b.func3()"""

#Task-13
"""class Myclass:
    def func1(self):
        print("This is myclass")
class Myclass1:
    def func1(self):
        print("This is myclass1")
a=Myclass1()
a.func1()"""

#Task-14
class Myclass:
    def func1(self,n1,n2):
        ans=n1+n2
        print("Ans is :",ans)
    def func1(self,n1,n2,n3):
        ans=n1+n2+n3
        print("Ans is :",ans)
    
a=Myclass()
#a.func1(14,78)
a.func1(10,20,30)


