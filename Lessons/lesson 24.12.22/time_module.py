import time

def toglleIsRun(value=False):
    global isRun
    isRun = value
    
def start():
    global start_time
    toglleIsRun(True)
    start_time = time.time()

def finish():
    if isRun:
        toglleIsRun(False)
        return time.time() - start_time
    else:
        return -1

toglleIsRun()