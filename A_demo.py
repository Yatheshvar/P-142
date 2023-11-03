import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/yathe/OneDrive/Desktop/python/Movie app/movie/Scripts/articles.csv')

df = df.sort_values(['total_events'], ascending=[False])

output = df[["url", "title", "text", "lang", "total_events"]].head(20)