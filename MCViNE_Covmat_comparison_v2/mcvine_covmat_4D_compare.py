# We want to compute the MCViNE 4D and covmat 4D inverse covariance matrices for a random sampling of hklE points, plot along random hkl_dir directions, and compare

import sys
import glob
import os

import numpy as np
import scipy
import scipy.linalg
from matplotlib import pyplot as plt

import mcvine.cli
from mcni.utils import conversion as Conv
import compute_mcvine_res_sim_covmat
import h5py as hf
import use_covmat
import optimize_covmat_params_for_single_hardcoded_pt


def _list_mcvine_inv_covmats(mcvine_dir, workdir):
	
	# list all directories in mcvine_dir
	pattern = mcvine_dir + "E*"
	res_pts = glob.glob(pattern)

	# total number of results to analyze
	N = len(res_pts)

	# iterate through the list of results, collecting matrices as we go
	list_of_mats = []

	# also collect params (lists of [E, Ei, hkl, hkl_dir])
	list_of_params = []

	num_results_processed = 0

	for pt in res_pts:
		# change into directory containing results for this point
		#res_dir = mcvine_dir + pt
		res_dir = pt
		#os.chdir(res_dir)

		# compute the mcvine matrix
		mcvine_inv_cov, params = compute_mcvine_res_sim_covmat._compute_res_sim_inv_covmat_4D(res_dir, workdir)

		# append matrix to the list
		list_of_mats.append(mcvine_inv_cov)

		# append parameters to list
		list_of_params.append(params)

		# debug:
		num_results_processed += 1
		print "Processed " + str(num_results_processed) + " / " + str(N)


	return [list_of_mats, list_of_params]


def _get_inv_covmat_4D(dynamics_params, paramList):

	E_ = dynamics_params[0]
	Ei = dynamics_params[1]
	hkl = dynamics_params[2]
	hkl_dir_ = dynamics_params[3]

	instrument = use_covmat.instrument(
		name = 'ARCS',
		detsys_radius = "3.*meter",
		L_m2s = "13.6*meter",
		L_m2fc = "11.61*meter",
		offset_sample2beam = "-0.15*meter" # offset from sample to saved beam
		)

	class dynamics:
		hkl0 = hkl
		hkl_dir = hkl_dir_
		E=E_
		dq=0

	class scan:
		min, max, step = -5, 90., 0.5


	sampleyml = "Si.yml"

	tau_P = paramList[0]
	tau_M = paramList[1]
	pixel_radius = paramList[2]
	pixel_height = paramList[3]
	sigma_LMS = paramList[4]
	sigma_thetai = paramList[5]
	sigma_phii = paramList[6]
	
	tofwidths = use_covmat.tofwidths(P=tau_P, M=tau_M)
	beamdivs = use_covmat.beamdivs(theta=sigma_thetai, phi=sigma_phii)
	samplethickness = sigma_LMS
	
	radius_str = str(pixel_radius) + "*inch"
	height_str = str(pixel_height) + "*meter"
	pixel = use_covmat.pixel(
		#radius = "0.5*inch",
		radius = radius_str,
		#height = "meter/128",
		height = height_str,
		pressure = "10*atm",
	)

	cm_res = use_covmat.compute(
		sampleyml, Ei, dynamics, scan,
		instrument, pixel,
		tofwidths, beamdivs, samplethickness,
		plot=False)
	
	#ellipsoid_trace = cm_res['u']
	InvCov4D = cm_res['InvCov4D']
	
	return InvCov4D




def _get_inv_covmat_list(dynamics_params_list, paramList):

	inv_covmat_list = []
	numFailures = 0

	for dynamics_params in dynamics_params_list:

		try:
			inv_covmat = _get_inv_covmat_4D(dynamics_params, paramList)
			inv_covmat_list.append(inv_covmat)
		except:
			inv_covmat_list.append(-1)
			print "Failed for E, Ei, hkl, hkl_dir = " 
			print dynamics_params
			numFailures += 1


	print "numFailures = " + str(numFailures)
	return inv_covmat_list

'''
if use_inverse==True, then the inverse covariance matrices will be used to compute the matrix difference.  If False, then the covariance matrices from mcvine and the covmat method will be used directly to compute the matrix difference (the error)
'''
def _get_mat_errors(mcv_inv_covmats, inv_covmats, dynamics_params, use_inverse=True):

	errs = []
	mcv_inv_covmats_revised = []
	inv_covmats_revised = []
	dynamics_params_revised = []

	for i in range(len(inv_covmats)):
		if type(inv_covmats) != int:
			mcv = mcv_inv_covmats[i]
			cov = inv_covmats[i]

			mcv_inv_covmats_revised.append(mcv)
			inv_covmats_revised.append(cov)
			dynamics = dynamics_params[i]
			dynamics_params_revised.append(dynamics)

			err = optimize_covmat_params_for_single_hardcoded_pt._matrixDifference(mcv, cov)

			if use_inverse==False:
				cov_standard = np.linalg.inv(cov)
				mcv_standard = np.linalg.inv(mcv)
				err = optimize_covmat_params_for_single_hardcoded_pt._matrixDifference(mcv_standard, cov_standard)

			errs.append(err)

	return [errs, dynamics_params_revised, mcv_inv_covmats_revised, inv_covmats_revised]


def _num_errs_over_threshold(threshold, errs):

	num = 0

	for err in errs:
		if err > threshold:
			num += 1

	return num 


def _get_2D_submatrix(M, i, j):

	# M is a 4x4 matrix from which we want to extract a 2x2 submatrix consisting of the i,i; i,j; j,i; and j,j entries
	M_ii = M[i][i]
	M_ij = M[i][j]
	M_ji = M[j][i]
	M_jj = M[j][j]

	M_2D = np.array([[M_ii, M_ij], [M_ji, M_jj]])
	return M_2D

def _plot_three_directions(M, N, Ei, E, hkl):

	# M is an inverse covariance matrix from a mcvine resolution simulation and N is the inverse covariance matrix from the covmat estimation method

	# for h
	M_h = _get_2D_submatrix(M, 0, 3)

	r = np.linalg.eig(M_h)
	mR = r[1]; lambdas = r[0]
	RR = 2*np.log(2)
	theta = np.arange(0, 360, 1.)*np.pi/180
	u1p = np.sqrt(RR/lambdas[0])*np.cos(theta)
	u2p = np.sqrt(RR/lambdas[1])*np.sin(theta)
	up = np.array([u1p, u2p]).T
	u_h = np.dot(up, mR.T)

	# for k
	M_k = _get_2D_submatrix(M, 1, 3)

	r = np.linalg.eig(M_k)
	mR = r[1]; lambdas = r[0]
	RR = 2*np.log(2)
	theta = np.arange(0, 360, 1.)*np.pi/180
	u1p = np.sqrt(RR/lambdas[0])*np.cos(theta)
	u2p = np.sqrt(RR/lambdas[1])*np.sin(theta)
	up = np.array([u1p, u2p]).T
	u_k = np.dot(up, mR.T)

	# for l
	M_l = _get_2D_submatrix(M, 2, 3)

	r = np.linalg.eig(M_l)
	mR = r[1]; lambdas = r[0]
	RR = 2*np.log(2)
	theta = np.arange(0, 360, 1.)*np.pi/180
	u1p = np.sqrt(RR/lambdas[0])*np.cos(theta)
	u2p = np.sqrt(RR/lambdas[1])*np.sin(theta)
	up = np.array([u1p, u2p]).T
	u_l = np.dot(up, mR.T)


	# for h
	N_h = _get_2D_submatrix(N, 0, 3)

	r = np.linalg.eig(N_h)
	mR = r[1]; lambdas = r[0]
	RR = 2*np.log(2)
	theta = np.arange(0, 360, 1.)*np.pi/180
	u1p = np.sqrt(RR/lambdas[0])*np.cos(theta)
	u2p = np.sqrt(RR/lambdas[1])*np.sin(theta)
	up = np.array([u1p, u2p]).T
	v_h = np.dot(up, mR.T)

	# for k
	N_k = _get_2D_submatrix(N, 1, 3)

	r = np.linalg.eig(N_k)
	mR = r[1]; lambdas = r[0]
	RR = 2*np.log(2)
	theta = np.arange(0, 360, 1.)*np.pi/180
	u1p = np.sqrt(RR/lambdas[0])*np.cos(theta)
	u2p = np.sqrt(RR/lambdas[1])*np.sin(theta)
	up = np.array([u1p, u2p]).T
	v_k = np.dot(up, mR.T)

	# for l
	N_l = _get_2D_submatrix(N, 2, 3)

	r = np.linalg.eig(N_l)
	mR = r[1]; lambdas = r[0]
	RR = 2*np.log(2)
	theta = np.arange(0, 360, 1.)*np.pi/180
	u1p = np.sqrt(RR/lambdas[0])*np.cos(theta)
	u2p = np.sqrt(RR/lambdas[1])*np.sin(theta)
	up = np.array([u1p, u2p]).T
	v_l = np.dot(up, mR.T)


	figtitle = "hkl_3dir_plot_for_Ei=" + str(Ei) + "_E=" + str(E) + "_hkl=" + str(hkl) + ".png"

	fig = plt.figure()

	ax1 = fig.add_subplot(231)
	ax1.plot(u_h[:,0], u_h[:,1])
	ax1.set_title("h")

	ax2 = fig.add_subplot(232)
	ax2.plot(u_k[:,0], u_k[:,1])
	ax2.set_title("k")

	ax3 = fig.add_subplot(233)
	ax3.plot(u_l[:,0], u_l[:,1])
	ax3.set_title("l")

	ax4 = fig.add_subplot(234)
	ax4.plot(v_h[:,0], v_h[:,1])
	#ax4.set_title("h")

	ax5 = fig.add_subplot(235)
	ax5.plot(v_k[:,0], v_k[:,1])
	#ax5.set_title("k")

	ax6 = fig.add_subplot(236)
	ax6.plot(v_l[:,0], v_l[:,1])
	#ax6.set_title("l")

	fig.suptitle("mcvine (top) vs covmat (bottom)")

	plt.gcf()
	plt.savefig(figtitle)



def _plot_all_results(mcv_mats, cov_mats, dynamics_params_list, plotdir):

	workdir = os.getcwd()
	os.chdir(plotdir)

	N = len(mcv_mats)
	for i in range(N):
		E, Ei, hkl, hkl_dir = dynamics_params_list[i]
		M = mcv_mats[i] 
		N = cov_mats[i] 

		_plot_three_directions(M, N, Ei, E, hkl)


	os.chdir(workdir)





if __name__ == '__main__':

	# record name of current working directory
	workdir = os.getcwd()
	
	# get the name of the directory where all the mcvine results are stored
	mcvine_dir = sys.argv[1]

	list_of_mats, list_of_params = _list_mcvine_inv_covmats(mcvine_dir, workdir)

	# define covmat parameters and run the covmat computations
	#paramList = [11.28741, 6.9908, 0.4406, 0.0078, 0.004, 0.00207, 0.0114589]
	paramList = [7.0750576, 6.2124, 0.30695, 0.0062777, 0.000201275, 0.04274, 0.027485]
	list_inv_covmats = _get_inv_covmat_list(list_of_params, paramList)

	errs, dynamics_params, mcv_mats, cov_mats = _get_mat_errors(list_of_mats, list_inv_covmats, list_of_params)

	print "max(errs) = " + str(max(errs))
	print "min(errs) = " + str(min(errs))
	print "mean(errs) = " + str(sum(errs) / len(errs))
	print "total number of comparisons = " + str(len(errs))
	print "number errs over 1000 = " + str(_num_errs_over_threshold(1000., errs))
	print "number errs over 2000 = " + str(_num_errs_over_threshold(2000., errs))
	print "number errs over 3000 = " + str(_num_errs_over_threshold(3000., errs))
	print "number errs over 10,000 = " + str(_num_errs_over_threshold(10000., errs))


	# debug through plotting

	# select mcvine and covmat inverse matrices to compare
	M = mcv_mats[0]
	N = cov_mats[0]
	E, Ei, hkl, hkl_dir = dynamics_params[0]
	_plot_three_directions(M, N, Ei, E, hkl)

	plotdir = "covmat_vs_mcv_plots_2"
	_plot_all_results(mcv_mats, cov_mats, dynamics_params, plotdir)