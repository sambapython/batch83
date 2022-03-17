"""
fun()
print(x,y)
"""
"""
import hr# it will run hr frile and add all references to the fram "hr"
print(hr.x, hr.y)
hr.fun()
"""
"""
from hr import fun, fun1
fun()
fun1()
"""
"""
import hr
hr.fun()
hr.fun1()
"""
#import sales
#import ERP
#ERP.sales.create_customer()
#import ERP
"""
from ERP import sales,acc
sales.create_customer()
acc.create_account()
"""
"""
import stock
stock.create_product()
"""
"""
import sys
print(sys.path)
import stock
"""
"""
import sys
sys.path.append("C:\\Users\\Lenovo\\batch83")
import delivery
"""
#from ERP import sales
"""
import hr
import hr
import hr
"""
import hr
# it look for hr.py file in python path(sys.path). if the file not available, then it will throw no module error
# file is available:
        #it look for hr.pyc file in correponding __pycache__
               # if hr.pyc file not availabel, then it will create it.
               # hr.pyc is available:
                   #then it will take a decission that it has to create hr.pyc again.
                   # it will check for hr.py modified date and time hr.pyc modified date and time
                   # if hr.pyc modified date and time>hr.py modified date time: No changes in .py 
                   		# if hr.pyc compiled pyton version==python version currently runnning main.py
                   		    # it will run existing compiled file
                   		#else:
                   		    # it will create new compile file
                      # it will run the existing .pyc file itself.
                   #else
                       # it will create new.pyc file. and it will that new file.


import sys 
#sys.path.append("C:\\Users\\Lenovo\\batch83")
#sys.path.insert(0, "C:\\Users\\Lenovo\\batch83")

print(sys.path)

import a1 
a1.fun()