df = [df1, df2, df3]
result = pd.concat(df, keys=['x', 'y', 'z'])
result.loc['y']