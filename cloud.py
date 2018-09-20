#!/usr/bin/env python3.6
from typing import Dict
import time
import re

str2="We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake."
str3='The bill came to five dollars.'

start_time = time.time()
cloudhash: Dict[str, int] = {}
for word in re.split(r"\W",str3.lower()):
    if word is '':
        continue
    if word in cloudhash:
        cloudhash[word] += 1
    else:
        cloudhash[word] = 1


print(time.time()-start_time)
print(cloudhash)



