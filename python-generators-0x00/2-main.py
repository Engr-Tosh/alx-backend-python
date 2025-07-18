#!/usr/bin/python3
import sys
processing = __import__('1-batch_processing')

##### print processed users in a batch of 50
try:
    for users in processing.batch_processing(50):
        print(users)

except BrokenPipeError:
    sys.stderr.close()