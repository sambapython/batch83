class Operation:
	def add(self, x,y):
		print(f"x={x}, y={y}")
		try:
			res=x+y
		except Exception as err:
			print(err)
			res=None
		#return 10
		return res