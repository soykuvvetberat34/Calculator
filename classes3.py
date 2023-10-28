#calculator with classes(python)
#divison: bolme, multiply: carpma ,toplama:add ,cıkarma:ext


class Cal(object):
    def __init__(self,a,b):
        self.value1=a
        self.value2=b
    
    def add(self):
        return "result:",self.value1 + self.value2
    def ext(self):
        return "result:",self.value1 - self.value2
    def mult(self):
        return "result:",self.value1 * self.value2
    def divison(self):
        return "result:",self.value1 / self.value2
        

i=0

while (i<4):
    print("CALCULATOR")
    print("enter what you want to do(1:add,2:ext,3:mult,4:divison)")    
    print("\n")
    enter=int(input("process?:"))

    if enter==1:
        v1=int(input("enter the first value:"))
        v2=int(input("enter the second value:"))
        c1=Cal(v1,v2)
        result=c1.add()
        print(result)
        i=4
    elif enter==2:
        v1=int(input("enter the first value:"))
        v2=int(input("enter the second value:"))
        c1=Cal(v1,v2)
        result=c1.ext()
        print(result)

        i=4
    elif enter==3:
        v1=int(input("enter the first value:"))
        v2=int(input("enter the second value:"))
        c1=Cal(v1,v2)
        result=c1.mult()
        print(result)

        i=4
    elif enter==4:
        v1=int(input("enter the first value:"))
        v2=int(input("enter the second value:"))
        c1=Cal(v1,v2)
        result=c1.divison()
        print(result)

        i=4
    else:
        print("your choose not defined.....")
        print("try again")
        i+=1


print("your process finished by program")

    
    
        
    