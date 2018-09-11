# ---
# jupyter:
#   jupytext_format_version: '1.2'
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.5.2
# ---

# # Linear regression
#
#

# ## Least squares
#
# A mathematical procedure for finding the best-fitting curve to a given set of points by minimizing the sum of the squares of the offsets ("the residuals") of the points from the curve. The sum of the squares of the offsets is used instead of the offset absolute values because this allows the residuals to be treated as a continuous differentiable quantity. However, because squares of the offsets are used, outlying points can have a disproportionate effect on the fit, a property which may or may not be desirable depending on the problem at hand. 
#

# ### Show the data
#

# +
# %matplotlib inline

import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn import datasets

# load data
d = datasets.load_diabetes()

X = d.data[:, 2]
Y = d.target

# draw original data
plt.scatter(X, Y)
plt.show()
# -

# ### Theory
# For $N$ observation data:
# $$
# \mathbf{X} = \{x_1, x_2, ..., x_N \} \\
# \mathbf{Y} = \{y_1, y_2, ..., y_N \}
# $$
#
# We want to find the model which can predict the data. The simplest model is linear model, which has the form of 
# $$
# y = ax + b
# $$
#
# The purpose is to find parameters $a, b$ which best fit the model to the observation data. 
#
# We use the sum of squares to measure the differences (loss function) between the model's prediction and observation data:
# $$
# L = \sum_{i=1}^{N} (y_i - a x_i + b)^2
# $$
#
# To make the loss function minimize, we can find the parameters:
# $$
# \frac{\partial L}{\partial a} = -2 \sum_{i=1}^{N} (y_i - a x_i - b) x_i \\
# \frac{\partial L}{\partial b} = -2 \sum_{i=1}^{N} (y_i - a x_i - b)
# $$
# When the loss is minimized, therefore the partial difference is zero, then we can get:
# $$
# -2 \sum_{i=1}^{N} (y_i - a x_i - b) x_i = 0 \\
# -2 \sum_{i=1}^{N} (y_i - a x_i - b) = 0 \\
# $$
#
# We reoder the items as:
# $$
# a \sum x_i^2 + b \sum x_i = \sum y_i x_i \\
# a \sum x_i + b N = \sum y_i
# $$
# By solving the linear equation we can obtain the model parameters.

# ### Program

# +
N = X.shape[0]

S_X2 = np.sum(X*X)
S_X  = np.sum(X)
S_XY = np.sum(X*Y)
S_Y  = np.sum(Y)

A1 = np.array([[S_X2, S_X], 
               [S_X, N]])
B1 = np.array([S_XY, S_Y])

coeff = np.linalg.inv(A1).dot(B1)

print('a = %f, b = %f' % (coeff[0], coeff[1]))

x_min = np.min(X)
x_max = np.max(X)
y_min = coeff[0] * x_min + coeff[1]
y_max = coeff[0] * x_max + coeff[1]

plt.scatter(X, Y)
plt.plot([x_min, x_max], [y_min, y_max], 'r')
plt.show()
