import logging#debug,info,warn,error
logging.basicConfig(level=logging.DEBUG, filename="log.txt",
format="%(asctime)s=>%(levelname)s=>%(filename)s=>%(message)s")# logging.WARN
logging.info("SERVER STARTED")
a=input("enter a vlaue:")
logging.info("A entered")
b=input("enter b vlaue:")
logging.info("Bentered")
logging.debug("before convertion: a=%s, b=%s"%(a,b))
try:
    a=float(a)#ValueError
    logging.info("A converted")
    b=float(b)
    logging.info("B converted")
    logging.debug("after convertion: a=%s, b=%s"%(a,b))
    res=a/b#ZeroDivisionError
    print("res=",res)
    logging.debug("Res=%s"%res)
except:
    error = "SYSTEM RAISED ERRORS"
    print(error)
    logging.error(error)
logging.info("DONE")