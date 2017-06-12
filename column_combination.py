import pandas as pd
from itertools import product
df = pd.read_csv('sample_input.csv',encoding='ISO-8859-1')
df = pd.DataFrame(list(product(df.s1,df.s2)), columns=['s1', 's2'])

df.to_csv('input_combination.tsv',encoding='ISO-8859-1')