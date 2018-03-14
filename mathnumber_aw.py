
import time
def calcProd():
    product = 1
    for i in range(1, 100000):
        product = product*i
    return product
startTime = time.time()
#print(startTime)
prod = calcProd()
#print(prod) DO NOT TRY THIS AT HOME ... I broke the terminal
endTime = time.time()
#print(endTime)
print('The result is %s digits long.' %(len(str(prod))))
print('Took %s seconds to calculate.' % (endTime-startTime))
