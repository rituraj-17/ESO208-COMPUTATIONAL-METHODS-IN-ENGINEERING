import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats
import os
x = np.array([0.5,0.8,1.5,2.1,5.4,3.2,1.8,0.9,2.2,0.7,
              4.3,3.8,4.7,6.4,4.1,3.1,2.7,1.6,0.6,1.1])
y = np.array([5.12,7.06,8.65,11.78,26.37,19.91,10.57,7.39,10.99,9.36,
              22.35,22.30,24.08,29.91,20.25,18.53,15.25,11.04,7.25,10.08])
n = len(x)
Sx, Sy   = x.sum(), y.sum()
Sxy, Sxx = (x*y).sum(), (x*x).sum()
a1 = (n*Sxy - Sx*Sy)/(n*Sxx - Sx**2)
a0 = Sy/n - a1*Sx/n
yhat = a0 + a1*x
e    = y - yhat
Sr  = (e**2).sum()
St  = ((y - y.mean())**2).sum()
s2  = Sr/(n-2)
se  = np.sqrt(s2)
r2 = (St - Sr)/St
print("n            =", n)
print("Sum x        = %.4f  Sum y  = %.4f" % (Sx, Sy))
print("Sum xy       = %.4f  Sum x2 = %.4f" % (Sxy, Sxx))
print("slope   a1   = %.6f" % a1)
print("intercept a0 = %.6f" % a0)
print("Sr           = %.6f" % Sr)
print("St           = %.6f" % St)
print("var(resid) s2= %.6f   (s_e = %.6f)" % (s2, se))
print("r^2          = %.6f   r = %.6f" % (r2, np.sqrt(r2)))
print()
print(" i     x       y      y_hat   residual")
for i in range(n):
    print("%2d  %5.2f  %7.2f  %7.4f  %8.4f" % (i+1, x[i], y[i], yhat[i], e[i]))
xp   = 7.0
yp   = a0 + a1*xp
tcrit = stats.t.ppf(0.95, n-2)
Sxx_c = ((x - x.mean())**2).sum()
half_mean = tcrit*se*np.sqrt(1/n + (xp - x.mean())**2/Sxx_c)
half_pred = tcrit*se*np.sqrt(1 + 1/n + (xp - x.mean())**2/Sxx_c)
print("\nxbar = %.4f  Sxx(centred) = %.4f  t(0.05,18) = %.4f" % (x.mean(), Sxx_c, tcrit))
print("y(7) = %.4f" % yp)
print("90%% CI (mean response)     : [%.4f , %.4f]  (+/- %.4f)" % (yp-half_mean, yp+half_mean, half_mean))
print("90%% Prediction interval    : [%.4f , %.4f]  (+/- %.4f)" % (yp-half_pred, yp+half_pred, half_pred))
fig, ax = plt.subplots(2, 2, figsize=(11, 8))
xs = np.linspace(0, 7.5, 200)
ax[0,0].plot(x, y, 'o', label='data')
ax[0,0].plot(xs, a0+a1*xs, 'r-', label='y = %.4f + %.4f x' % (a0, a1))
ax[0,0].errorbar([xp],[yp], yerr=[half_mean], fmt='s', color='g', capsize=5,
                 label='prediction at x=7')
ax[0,0].set_xlabel('x')
ax[0,0].set_ylabel('y')
ax[0,0].set_title('(a) Least squares fit,  $r^2$ = %.4f' % r2)
ax[0,0].legend()
ax[0,0].grid(alpha=.3)
ax[0,1].stem(x, e)
ax[0,1].axhline(0, color='k', lw=1)
ax[0,1].set_xlabel('x')
ax[0,1].set_ylabel('residual  $e_i$')
ax[0,1].set_title('(b) Residuals vs x')
ax[0,1].grid(alpha=.3)
ax[1,0].plot(np.arange(1,n+1), e, 'o-')
ax[1,0].axhline(0, color='k', lw=1)
ax[1,0].set_xlabel('observation order i')
ax[1,0].set_ylabel('$e_i$')
ax[1,0].set_title('(b) Residuals in data order')
ax[1,0].grid(alpha=.3)
ax[1,1].hist(e, bins=7, edgecolor='k')
ax[1,1].set_xlabel('residual')
ax[1,1].set_ylabel('frequency')
ax[1,1].set_title('(c) Histogram of residuals')
ax[1,1].grid(alpha=.3)
plt.tight_layout()
script_dir = os.path.dirname(os.path.abspath(__file__))
plt.savefig(os.path.join(script_dir, 'Q1_plots.png'), dpi=150)
dw = ((np.diff(e))**2).sum()/Sr
print("\nDurbin-Watson d = %.4f" % dw)
print("lag-1 autocorrelation = %.4f" % (np.corrcoef(e[:-1], e[1:])[0,1]))
x2 = np.array([0.1,0.2,0.4,0.6,0.9,1.3,1.5,1.7,1.8])
y2 = np.array([2.00,2.47,3.04,3.43,3.88,4.33,4.52,4.69,4.77])
X, Y = np.log(x2), np.log(y2)
m = len(X)
b = (m*(X*Y).sum() - X.sum()*Y.sum())/(m*(X*X).sum() - X.sum()**2)
lna = Y.mean() - b*X.mean()
a = np.exp(lna)
print("\nQ2")
print("sum X = %.6f  sum Y = %.6f  sum XY = %.6f  sum X2 = %.6f" %
      (X.sum(), Y.sum(), (X*Y).sum(), (X*X).sum()))
print("b = %.6f   ln a = %.6f   a = %.6f" % (b, lna, a))
r2b = 1 - ((Y-(lna+b*X))**2).sum()/((Y-Y.mean())**2).sum()
print("r^2 (log space) = %.6f" % r2b)
print("\n   x      y     X=lnx    Y=lny     XY       X^2")
for i in range(m):
    print("%5.1f  %5.2f  %7.4f  %7.4f  %8.4f  %7.4f" %
          (x2[i], y2[i], X[i], Y[i], X[i]*Y[i], X[i]**2))