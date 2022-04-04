from app import Operation
import unittest
class TestAdd(unittest.TestCase):
	"""
	add(10,20)-->30
	add("str1","str2")--> str1str2
	add(10,"str2")-->None
	add("str1",20)-->None
	"""
	@classmethod
	def setUpClass(cls):
		print("SIGNIN")
		cls.op = Operation()

	@classmethod
	def tearDownClass(cls):
		print("SIGNOUT")
		cls.op= None

	def setUp(self):
		self.x=1233
		print("prepare test data")

	def tearDown(self):
		print("remove test data")


	def test_10_20(self):
		print(self.x)
		print("executing test_10_20")
		act_res = self.op.add(10,20)
		exp_res=30 
		self.assertEqual(act_res, exp_res, "test_10_20 FAILED")

	def test_str1_str2(self):
		print("executing test_str1_str2")
		act_res = self.op.add("str1","str2")
		exp_res="str1str2" 
		self.assertEqual(act_res, exp_res, "test_str1_str2 FAILED")

	def test_str1_20(self):
		print("executing test_str1_20")
		act_res = self.op.add("str1",20)
		exp_res=None
		self.assertEqual(act_res, exp_res, "test_str1_20 FAILED")

	def test_10_str2(self):
		print("executing test_10_str2")
		act_res = self.op.add(10,"str2")
		exp_res=None
		self.assertEqual(act_res, exp_res, "test_10_str2 FAILED")

unittest.main()
