""" Scrubbing A Stuborn Pan """

import random

dirty = True # state of the pan
scrub_count = 0 # number of scrubs

while(dirty):
    # continue looping as long as the pan is still dirty
    # by checking that the dirty variable is true.
    scrub_count += 1 #add 1 to the scrub_count
    print('Scrub the pan: {}'.format(scrub_count))# print how many times the pan was scrubbed

    print('Rinse & check if the pan is clean.') # rinse the pan to checl if it's clean

    if not random.randint(0,9): #get a random # between 0-9
        #When the # of times has reached the # generated
        print('All clean!')
        dirty = False
    else:
        print('Still dirty...')
