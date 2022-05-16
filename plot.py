from scipy import special
from matplotlib import rc
import matplotlib.pyplot as plt
import numpy as np

rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

x = np.linspace(0, 6)
plt.plot(x, special.erf(1/(np.sqrt(2)*x)), label=r'\textbf{time (s)}')
plt.plot(x, 1/(1+x**2), label='(1+x^2)')
plt.plot(x, (1+x**2)**(-0.5), label = '(1+x^2)^(-0.5)')
plt.xlabel('n')
plt.ylabel('Variance Adaptation factor')
plt.legend(loc='upper right')
plt.show()
