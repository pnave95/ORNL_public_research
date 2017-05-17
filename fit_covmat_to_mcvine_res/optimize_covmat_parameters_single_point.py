#  The purpose of this code is to optimize the parameters for the covariance resolution calculation by fitting the produced covariance matrix to the covariance matrix of the mcvine resolution simulation data

import numpy as np
import use_covmat
import compute_mcvine_res_sim_covmat
import os
import glob
import sys


# Sample
sampleyml = "Si.yml"


# Instrument
# instrument = use_covmat.instrument(
#     name = 'ARCS',
#     detsys_radius = "3.*meter",
#     L_m2s = "13.6*meter",
#     L_m2fc = "11.61*meter",
#     offset_sample2beam = "-0.15*meter" # offset from sample to saved beam
#     )
pixel = use_covmat.pixel(
    radius = "0.5*inch",
    height = "meter/128",
    pressure = "10*atm",
    )


def _get_Ei_E_hkl_from_filename(filename):
	
	s1 = filename[18:]
	#print s1
	i = s1.index('.') + 2
	Ei_str = s1[:i]
	Ei = float(Ei_str)

	ii = i + 4
	s2 = s1[ii:]
	j = s2.index('_')
	E_str = s2[:j]
	E = float(E_str)

	a = s2.index('[') + 1
	s3 = s2[a:]
	b = s3.index(',')
	h_str = s3[:b]
	h = float(h_str)

	aa = b + 2
	s4 = s3[aa:]
	bb = s4.index(',')
	k_str = s4[:bb]
	k = float(k_str)

	aaa = bb + 2
	s5 = s4[aaa:]
	bbb = s5.index(']')
	l_str = s5[:bbb]
	l = float(l_str)

	hkl = np.array([h,k,l])

	dynamic_var = [Ei, E, hkl]

	return dynamic_var



def _get_Ei_E_hkl_from_dirname(dirname):
	
	s1 = dirname[17:]
	#print s1
	i = s1.index('.') + 2
	Ei_str = s1[:i]
	Ei = float(Ei_str)

	ii = i + 4
	s2 = s1[ii:]
	j = s2.index('_')
	E_str = s2[:j]
	E = float(E_str)

	a = s2.index('[') + 1
	s3 = s2[a:]
	b = s3.index(',')
	h_str = s3[:b]
	h = float(h_str)

	aa = b + 2
	s4 = s3[aa:]
	bb = s4.index(',')
	k_str = s4[:bb]
	k = float(k_str)

	aaa = bb + 2
	s5 = s4[aaa:]
	bbb = s5.index(']')
	l_str = s5[:bbb]
	l = float(l_str)

	hkl = np.array([h,k,l])

	dynamic_var = [Ei, E, hkl]

	return dynamic_var


'''
Purpose:  This is a loss function which measures the "error" (or distance) between the "covmat" method covariance matrices and the mcvine resolution method covariance matrices
'''
def _covmat_mcvine_loss(paramList, hkl_dir_passed):
	
	# set any necessary classes (tofwidths, beamdivs, etc) based on specified parameter values
	#tof_width_P, tof_width_M = paramList[0]
	tof_width_P = paramList[0]
	tof_width_M = paramList[1]
	tofwidths = use_covmat.tofwidths(P=tof_width_P, M=tof_width_M)

	#beamdiv_theta, beamdiv_phi = paramList[1]
	beamdiv_theta = paramList[2]
	beamdiv_phi = paramList[3]
	beamdivs = use_covmat.beamdivs(theta=beamdiv_theta, phi=beamdiv_phi)

	#samplethickness = paramList[2]
	samplethickness = paramList[4]

	L_m2s_passed = paramList[5]
	L_m2fc_passed = paramList[6]
	

	# instrument
	instrument = use_covmat.instrument(
    name = 'ARCS',
    detsys_radius = "3.*meter",
    #L_m2s = "13.6*meter",
    L_m2s = str(L_m2s_passed) + "*meter",
    #L_m2fc = "11.61*meter",
    L_m2fc = str(L_m2fc_passed) + "*meter",
    offset_sample2beam = "-0.15*meter" # offset from sample to saved beam
    )


	# iterate through all or several Ei,E,q points, computing the "covmat" method covariance matrix at each point; for each, compare to an (already completed) mcvine resolution simulation ellipse and compute the loss/error
	#list_pts = glob.glob("mcvine_res_sim_Ei*.png")
	list_pts = glob.glob("out.res_comps_Ei=125.0__E=7.8125*")

	# make a list to hold distances between the (inverse) covmat and mcvine res sim covariance matrices
	cov_distances = []

	for point in list_pts:
		#Ei_pt, E_pt, hkl_pt = _get_Ei_E_hkl_from_filename(point)
		Ei_pt, E_pt, hkl_pt = _get_Ei_E_hkl_from_dirname(point)
		#print Ei, E, hkl

		class dynamics:
			hkl0 = hkl_pt
			hkl_dir = hkl_dir_passed
			E = E_pt
			dq = 0.
		class scan:
			min, max, step = -5., 90., 0.5

		u, mR, lambdas = use_covmat.compute(sampleyml, Ei_pt, dynamics, scan, instrument, pixel, tofwidths, beamdivs, samplethickness, plot=False)

		# recreate the "covmat" method inverse covariance matrix
		D = np.array([[lambdas[0], 0.0], [0.0, lambdas[1]]])
		A = np.dot(mR, D)
		B = np.dot(A, mR.T)
		covmat_cov_inv = B



		# Now, we lookup the mcvine resolution simulation data and compute the corresponding covariance matrix to compare:
		resfile = point + "/res.h5"
		mcvine_covmat = compute_mcvine_res_sim_covmat._get_mcvine_res_sim_covmat(resfile)
		mcvine_cov_inv = np.linalg.inv(mcvine_covmat)


		# compute distance between the two matrices
		#diff_mat = covmat_cov_inv - mcvine_cov_inv

		# TRY ALTERNATIVE METHOD (distance between actual covariance matrices)
		diff_mat = np.linalg.inv(covmat_cov_inv) - mcvine_covmat

		print "covmat_cov_inv = "
		print covmat_cov_inv
		print "\n"
		print "mcvine_cov_inv = "
		print mcvine_cov_inv
		print "\n"
		print "diff_mat = "
		print diff_mat
		print "\n"
		lambdas, eigvecs = np.linalg.eig(diff_mat)
		uniform_norm = max(np.fabs(lambdas))

		cov_distances.append(uniform_norm)


		print "completed computation for Ei= " + str(Ei_pt) + ", E=" + str(E_pt)

	# average all the covariance matrix losses/errors; return this average
	avg_dist = sum(cov_distances) / len(cov_distances)
	max_dist = max(cov_distances)
	min_dist = min(cov_distances)

	print "\n\n"
	print "avg_dist = " + str(avg_dist)
	print "min_dist = " + str(min_dist)
	print "max_dist = " + str(max_dist)
	print "\n\n"

	return [avg_dist, min_dist, max_dist]



'''
Purpose:  This function uses gradient descent to optimize the parameters
Arguments:
	numIters (int):  number of iterations (gradient descending steps)
	paramList (numpy array of current parameter values, doubles/floats)
	halfStep (decimal):  used for numerically computing derivatives
	convStepSize (decimal):  gradient descent step size
'''
#def _optimize_parameters(numIters, paramList, halfStep, convStepSize):
def _optimize_parameters(numIters, paramList, paramHalfSteps, hkl_dir):

	# flatten the paramList for convenience:
	#paramList = [paramList[0][0], paramList[0][1], paramList[1][0], paramList[1][1], paramList[2]]
	#paramHalfSteps = [paramHalfSteps[0][0], paramHalfSteps[0][1], paramHalfSteps[1][0], paramHalfSteps[1][1], paramHalfSteps[2]]

	# compute initial distance (avg, min, max)
	original_distances = _covmat_mcvine_loss(paramList, hkl_dir)
	
	for i in range(numIters):
		partialsList = []  # create empty list to hold partial derivatives (loss w.r.t. parameters)
		
		# compute the gradient
		for j in range(len(paramList)):
			halfStep = paramHalfSteps[j]
			#convStepSize = halfStep
			#downHalfStep = -1.0 * np.array(halfStep)
			#downHalfStep = downHalfStep.tolist()

			loss = _covmat_mcvine_loss(paramList, hkl_dir)
			loss_avg = loss[0]
			up_params = np.copy(paramList)
			down_params = np.copy(paramList)
			up_params[j] += halfStep
			#up_params[j] = [sum(x) for x in zip(up_params[j], halfStep)]
			down_params[j] -= halfStep
			#down_params[j] = [sum(x) for x in zip(down_params[j], downHalfStep)]
			up_loss = _covmat_mcvine_loss(up_params, hkl_dir)
			up_loss_avg = up_loss[0]
			d_loss = _covmat_mcvine_loss(down_params, hkl_dir)
			d_loss_avg = d_loss[0]
			diff = up_loss_avg - d_loss_avg
			partial = diff / (2*halfStep)
			partialsList.append(partial)

			# perform componentwise gradient descent (since step sizes are different)
			#paramList[j] -= (halfStep * partial)
			paramList[j] -= halfStep * (partial / abs(partial))

			print "paramListUpdated:  " + str(paramList)

			#if (up_loss_avg < loss_avg) or (d_loss_avg < loss_avg):
			#	if up_loss_avg < d_loss_avg:
			#		paramList[j] += 
		#gradient = np.array(partialsList)

		# perform gradient descent
		#paramList -= (convStepSize * gradient)

	# compute final distances
	final_distances = _covmat_mcvine_loss(paramList, hkl_dir)

	# return the optimized parameter values (and original and final distances for debugging and analysis purposes)
	return [paramList, original_distances, final_distances]


if __name__ == '__main__':

	startdir = os.getcwd()
	workdir = sys.argv[1]
	os.chdir(workdir)

	#paramList = [[10, 8], [0.01, 0.01], 0.0015]
	#paramList = [15.5, 13.5, 0.065, 0.065, 0.0125, 8.1, 9.41]
	paramList = [10., 8., 0.01, 0.01, 0.0015, 13.6, 11.41]
	#paramList = [10.5, 7.5, 0.015, 0.015, 0.0010]
	#paramList = [12, 6, 0.03, 0.03, 0.0005, 13.6, 11.61]
	originalParamList = np.copy(np.array(paramList))
	#paramHalfSteps = [[0.05, 0.05], [0.0005, 0.0005], 0.0001]
	paramHalfSteps = [0.05, 0.05, 0.0005, 0.0005, 0.0001, 0.05, 0.02]
	numIters = 50
	hkl_dir = np.array([1, 0, 0])
	#_covmat_mcvine_loss(paramList, hkl_dir)
	results = _optimize_parameters(numIters, paramList, paramHalfSteps, hkl_dir)

	finalParamList = np.array(results[0])
	original_distances = results[1]
	final_distances = results[2]

	print "\n\n\n"
	print "Original parameters = " + str(originalParamList)
	print "Final parameters = " + str(finalParamList)
	print "\n"
	print "original avg, min, max distances:  " + str(original_distances[0]) + ", " + str(original_distances[1]) + ", " + str(original_distances[2])
	print "final avg, min, max distances:  " + str(final_distances[0]) + ", " + str(final_distances[1]) + ", " + str(final_distances[2])

	os.chdir(startdir)

	