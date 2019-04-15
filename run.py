import time
import json
print("started building...")


time.sleep(5)
print("finished building...")

with open('output.txt', 'w') as outfile:
    data = {"test": "passed"}
    json.dump(data, outfile)
