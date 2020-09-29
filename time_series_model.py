from datetime import date, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
startyear = '2012'
startmonth = '10'
startday = '01'

y1 = open("data_y.txt","r") 
y2 = y1.read().split(',')
y= [float(x) for x in y2]
print(y)
print(len(y))
y1.close()
startdate = date(int(startyear), int(startmonth), int(startday))
DATE=[]
N=len(y)
i=0
#while startdate < date(int(endyear), int(endmonth), int(endday)):
while i<500:
    print(startdate)
    startdate += timedelta(days=1)
    DATE.append(startdate)
    i+=1

Y=pd.DataFrame(data=y,index=DATE)
# Lets print the data to see if there is any pattern, trend , seasonality 
plt.plot(Y)
import statsmodels.api as sm
import itertools
p = d = q = range(0, 3)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
import warnings
warnings.filterwarnings("ignore") # specify to ignore warning messages

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(Y,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)

            results = mod.fit()

            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue
mod = sm.tsa.statespace.SARIMAX(Y,
                                order=(0, 1, 1),
                                seasonal_order=(2, 2, 2, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)

results = mod.fit()
#
print(results.summary().tables[1])
results.plot_diagnostics(figsize=(15, 12))
plt.show()


pred = results.get_prediction(start=pd.to_datetime('2013-10-01'), dynamic=False)
pred_ci = pred.conf_int()
startdate1,enddate1=pd.to_datetime('2013-10-01').date(),pd.to_datetime('2014-02-12').date()
df=Y.loc[startdate1:enddate1]

ax = df.plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7)

ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)

ax.set_xlabel('Date')
ax.set_ylabel('User rating')
plt.legend()

plt.show()
