import time
import sys


while True:
    print("Hi from Docker")
    # flush the print output immediately to the console
    sys.stdout.flush() # This is important for the output to be visible in the Docker logs
    time.sleep(2)