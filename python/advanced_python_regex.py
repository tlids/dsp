# Q1

import pandas as pd
faculty = pd.read_csv('/Users/xiangli/ds/metis/metisgh/prework/dsp/python/faculty.csv')
degree = faculty[' degree']
degree.describe()
from collections import Counter
counts = Counter(degree)
print counts

#Q2
title = faculty[' title']
title.describe()
counts = Counter(title)
print counts

#Q3
email = faculty[' email']
print email

#Q4


