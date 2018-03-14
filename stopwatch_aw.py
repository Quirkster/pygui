# stopwatch, 339
import time
print('press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()
print('Started.')
StartTime = time.time()
lastTime=StartTime
lapNum = 1
totalTime=0
try:
    while True:
        input()
        lapTime=round(time.time()-lastTime, 2)
        totalTime = round(time.time() - StartTime, 2)
        print('Lap#%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nDone.')
    finalTime=round(time.time()-StartTime, 2)
    print('Final Time: ' + str(finalTime))
    print('Lap#%s' % (lapNum))
