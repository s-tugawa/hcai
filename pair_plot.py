import pandas as pd
import seaborn as sns
import sys

file=sys.argv[1]
df = pd.read_csv(file, index_col=0,sep=" ")

pg = sns.pairplot(df,corner=True,markers="x")
pg.set(xscale="log",yscale="log")
pg.savefig('pairplot.eps')
