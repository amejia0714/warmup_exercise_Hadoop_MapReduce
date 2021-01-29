#!/usr/bin/python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")

    if len(line) >=4: 
        cause = line[1]
        state = line[2]
        deaths = line[3]
            if cause.lower() == 'diabetes':
                print '%s\t%s\t%s' % (state, cause, deaths)

        print '%s\t%s\t%s' % (state, cause, deaths)
       
