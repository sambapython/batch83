import time
a=input("enter a vlaue:")
b=input("enter b vlaue:")
print("before convertion: a=%s, b=%s"%(a,b))
try:
    a=float(a)#ValueError
    b=float(b)
    print("after convertion: a=%s, b=%s"%(a,b))
    time.sleep(10)
    res=a/b#ZeroDivisionError
    print("res=",res)
except ZeroDivisionError as err:
    print("ERROR: expecting b!=0")
except ValueError as err:
    print("ERROR: Expecting only numbers..")
except Exception as err:
    print("ERROR: %s"%err)
except:
    print("SYSTEM RAISED ERRORS")
print("End")