print("this is hr")
def fun():
	print("hello")

x=1000
y=2000
z=300

 
	#python hr.py, the above condition evaluatesd to True. and fun1 signature executed. 
	#fun1 reference added to memory
	#import hr:  the above condition evaluate to False. so fun1 can not access. 
	#Because fun1 not added to memory

if __name__ == "__main__":
	def fun1():
		print("this is fun1")
		print("hi")
#fun1()
