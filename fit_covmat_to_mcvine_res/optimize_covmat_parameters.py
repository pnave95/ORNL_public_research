#  The purpose of this code is to optimize the parameters for the covariance resolution calculation by fitting the produced covariance matrix to the covariance matrix of the mcvine resolution simulation data

import numpy as np


'''
Purpose:  This is a loss function which measures the "error" (or distance) between the "covmat" method covariance matrices and the mcvine resolution method covariance matrices
'''
def _covmat_mcvine_loss(paramList):
	
	# set any necessary classes (tofwidths, beamdivs, etc) based on specified parameter values

	# iterate through all or several Ei,E,q points, computing the "covmat" method covariance matrix at each point; for each, compare to an (already completed) mcvine resolution simulation ellipse and compute the loss/error

	# average all the covariance matrix losses/errors; return this average

	


'''
Purpose:  This function uses gradient descent to optimize the parameters
Arguments:
	numIters (int):  number of iterations (gradient descending steps)
	paramList (numpy array of current parameter values, doubles/floats)
	halfStep (decimal):  used for numerically computing derivatives
	convStepSize (decimal):  gradient descent step size
'''
def _optimize_parameters(numIters, paramList, halfStep, convStepSize):
	
	for i in range(numIters):
		partialsList = []  # create empty list to hold partial derivatives (loss w.r.t. parameters)
		
		# compute the gradient
		for j in range(len(paramList)):
			up_params = np.copy(paramList)
			down_params = np.copy(paramList)
			up_params[j] += halfStep
			down_params[j] -= halfStep
			up_loss = _covmat_mcvine_loss(up_params)
			d_loss = _covmat_mcvine_loss(down_params)
			diff = up_loss - d_loss
			partial = diff / (2*halfStep)
			partialsList.append(partial)
		gradient = np.array(partialsList)

		# perform gradient descent
		paramList -= (convStepSize * gradient)


	# return the optimized parameter values
	return paramList
