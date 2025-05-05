import pandas as pd
import numpy as np 

A = list(range(1000))
l1 = [x if x%2==0 for x in A]
l2 = sum(l1)
print(l2, l1)
