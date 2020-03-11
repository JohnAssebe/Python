import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
logging.debug('start of program')
def factorial(n):
    #logging.disable(logging.CRITICAL)
    logging.debug('start of factorial(%s%%)'%(n))
    total=1
    for i in range(1,n+1):
        total*=i
        logging.debug("the value of i: "+str(i)+"  total value: "+str(total))
    logging.debug("end of factorial(%s%%)"%(n)) 
    return total
print(factorial(6))
logging.debug("End of program")

    
