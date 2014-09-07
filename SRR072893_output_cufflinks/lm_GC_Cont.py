#!/usr/bin/env python

import pandas
import matplotlib.pyplot as plot
import statsmodels.api as sm

df = pandas.read_csv( "GC_Ratios.csv" ) #pandas will read my file

model = sm.formula.ols( formula = "Gene_Name ~ GC_Ratio", data=df ) #dependent variable ~ independent variable for regression model

res = model.fit()
print res.summary()

plot.scatter( df["Gene_Name"], df["GC_Ratio"] ) #this will take those columns from our file

plot.savefig( "lmGC.png" )