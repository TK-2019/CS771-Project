import numpy as np
import sklearn
from scipy.linalg import khatri_rao
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, SGDClassifier, Perceptron, RidgeClassifier
from sklearn.svm import LinearSVC
# You are allowed to import any submodules of sklearn that learn linear models e.g. sklearn.svm etc
# You are not allowed to use other libraries such as keras, tensorflow etc
# You are not allowed to use any scipy routine other than khatri_rao

# SUBMIT YOUR CODE AS A SINGLE PYTHON (.PY) FILE INSIDE A ZIP ARCHIVE
# THE NAME OF THE PYTHON FILE MUST BE submit.py

# DO NOT CHANGE THE NAME OF THE METHODS my_fit, my_map etc BELOW
# THESE WILL BE INVOKED BY THE EVALUATION SCRIPT. CHANGING THESE NAMES WILL CAUSE EVALUATION FAILURE

# You may define any new functions, variables, classes here
# For example, functions to calculate next coordinate or step length

################################
# Non Editable Region Starting #
################################
def my_fit( X_train, y_train ):
################################
#  Non Editable Region Ending  #
################################

	# Use this method to train your model using training CRPs
	# X_train has 32 columns containing the challeenge bits
	# y_train contains the responses
	
	# THE RETURNED MODEL SHOULD BE A SINGLE VECTOR AND A BIAS TERM
	# If you do not wish to use a bias term, set it to 0
  X_train = my_map(X_train)

  model = LogisticRegression(C = 100, tol=0.1)
  model.fit(X_train,y_train)

  # model = LinearSVC(loss = 'squared_hinge',C = 10, dual = False, tol = 0.001)
  # model.fit(X_train,y_train)

  # model = LinearSVC(loss = 'squared_hinge',C = 10, max_iter = 5000)
  # model.fit(X_train,y_train)

  # model = SGDClassifier(loss = 'squared_hinge')
  # model.fit(X_train,y_train)

  # model = RidgeClassifier(alpha = 1,)
  # model = model.fit(X_train,y_train)
  w = model.coef_
  b = model.intercept_

  return w[0],b


################################
# Non Editable Region Starting #
################################
def my_map( X ):
################################
#  Non Editable Region Ending  #
################################

	# Use this method to create features.
	# It is likely that my_fit will internally call my_map to create features for train points

  X = 1 - 2*X
  new_features_list = []

  # Iterate over each feature
  for i in range(0, 31):
      # Calculate the product of the first i features
      X[:, i+1] = X[:, i]*X[:, i+1]
      # Append the new feature to the list

  new_features_list.append(X)
  # Stack the new features horizontally to create the final feature matrix
  new_features = np.column_stack(new_features_list)
  # return new_features

  features = []
  features.append(new_features)
  for i in range(0,31):
    prod = khatri_rao(new_features[ :, i].reshape(-1,1).T,new_features[ :, i+1:].T)
    # print(prod.shape)
    features.append(prod.T)

  features = np.column_stack(features)
  # indices = np.array([31,61,90,118,145,171,196,220,243,265,286,306,325,343,360,376,391,405,218,430,441,451,460,468,475,481,486,490,])

  # print('Successful')
  # print(features.shape)
  return features

