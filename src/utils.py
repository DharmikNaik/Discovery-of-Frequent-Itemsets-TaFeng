import time


def flattenList(nonFlatList):
    return [item for sublist in nonFlatList for item in sublist]

def timeRun(fn, *args):
    startTime = time.time()
    endTime = time.time()
    fn(*args)
    runDuration = endTime - startTime
    return runDuration
