# to plot scatterplot and draw regression line
import matplotlib.pyplot as plt
from scipy import stats

# basic scatter from two lists
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

print(stats.linregress(x, y)) # estimated model parameters by minimizing sum of sq resid.
# LinregressResult(slope=np.float64(-1.751287711552612), 
# intercept=np.float64(103.10596026490066), 
# rvalue=np.float64(-0.7585915243761551), # correlation coefficient 
# pvalue=np.float64(0.0026468739224561008), #p-value, is slope significantly different from 0, if p<0.05, yes
# stderr=np.float64(0.45353615760774196), # standard error of the slope, unceratainty in the slope
# intercept_stderr=np.float64(3.903492810154512)) # standard error of the inrcept, uncertainty in the intercept
slope, intercept, r, p, std_err = stats.linregress(x, y)

def func(x): # manually writing mx+b
  return slope * x + intercept

mymodel = list(map(func, x))
# Takes every value inside x
# Applies func() to it
# Stores all the results in a list

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()