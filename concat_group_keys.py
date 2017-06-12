s3 = pd.Series([0, 1, 2, 3], name='foo')
s4 = pd.Series([0, 1, 2, 3])
s5 = pd.Series([0, 1, 4, 5])

pd.concat([s3, s4, s5], axis=1, keys=['red','blue','yellow'])