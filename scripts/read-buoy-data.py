import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

df = pd.read_table('./new.txt', 
                   delim_whitespace=True,
                   header=2, 
                   index_col=0, 
                   parse_dates=True)

nine_band = pd.DataFrame(df, columns=['22','22-18','18-16','16-14','14-12','12-10','10-8','8-6','6-2'], dtype=np.int64)   
sum_nine_band = nine_band.sum(1) 
nine_band_relative = nine_band.divide(sum_nine_band, axis=0)

long_period = nine_band[['22','22-18','18-16']].sum(axis=1)                                                                     
mid_period = nine_band[['16-14','14-12']].sum(axis=1)   
short_period = nine_band[['12-10','10-8','8-6','6-2']].sum(axis=1) 
period_group = pd.concat([long_period, mid_period, short_period], axis=1)                                                 
period_group_relative = period_group.divide(sum_nine_band, axis=0)


height = pd.DataFrame(df, columns=['(CM)', '(SEC)'])


