#repeated item of tuples
from collections import Counter
tup=(1,2,2,2,3,3,4,4,5,6,7,8,8,9)
for k, v in Counter(tup).items():
    if v > 1:
        print("Repeated: {}".format(k))

