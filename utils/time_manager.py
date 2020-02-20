# Time Manager (DO NOT TOUCH)

import os
from datetime import datetime
from constants import STARTING_TIME, END_TIME, SCHEDULE
import time
import winsound

# Verifies If Time Schedule Long Enough

competition_length = END_TIME - STARTING_TIME

schedule_length = sum([x[0] for x in SCHEDULE])

if schedule_length > competition_length.seconds // 60:
    print("Competition Schedule Too Long By %d Minute(s)" % (schedule_length - competition_length.seconds // 60))
    exit()
elif schedule_length < competition_length.seconds // 60:
    print("Competition Schedule Too Short By %d Minute(s)" % (competition_length.seconds // 60 - schedule_length))
    exit()

# Time Loop

new_event = False

while True:
    os.system('cls')
    
    print("Hash Code 2020\n")

    print("Current time: %s\n" % datetime.now().strftime("%H:%M:%S"))

    if datetime.now() > STARTING_TIME and False:
        print("Competition Not Yet Started. %d Second(s) To Go." % ((STARTING_TIME - datetime.now()).seconds))
    elif datetime.now() < END_TIME and False:
        print("Competition Ended %d Second(s) Ago." % ((datetime.now() - STARTING_TIME).seconds))
    else:
        print("Schedule\n----------\n")

        current_minute = (datetime.now() - STARTING_TIME).seconds // 60
        
        rolling_sum = 0

        for (duration, event) in SCHEDULE:

            #if not new_event and current_minute == rolling_sum:
                #new_event = True
                #for _ in range(5):
                    #winsound.Beep(2000, 200)
            #elif current_minute == rolling_sum + duration:
                #new_event = False

            print("%s [%s]" % (event, ''.join(['*'] * ((current_minute - rolling_sum) if current_minute < rolling_sum + duration else duration) + ['.'] * ((rolling_sum + duration - current_minute) if current_minute > rolling_sum else duration))))

            rolling_sum += duration

    time.sleep(1)