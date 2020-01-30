# Modules - a lot can be done inside of Python core, but if not, there's likely a module that can do it (math, random, etc.)

import time as t            # let's say you're importing a module with a long name. you can alias it as something shorter

print(t.localtime())

time_now = t.localtime()    # like Java, you can use dot notation to access certain fields about a variable / object
print("Time: " + str(time_now.tm_hour) + "h " + str(time_now.tm_min) + "m")

print(t.time())             # the number of seconds that have passed since "The Epic" - January 1st, 1970
t.sleep(5)                  # delay execution of code by 5 seconds
print(t.time())