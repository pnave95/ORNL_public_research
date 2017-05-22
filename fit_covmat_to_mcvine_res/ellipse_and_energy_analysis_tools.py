#  tools

import numpy as np
import scipy as sp
import scipy.integrate
from matplotlib import pyplot as plt

import use_covmat
import compute_mcvine_res_sim_covmat
import glob
import os
import sys

import h5py as hf


'''
Description:  This function takes a symmetric matrix, M, and finds the angle of the major axis of the corresponding ellipse; the angle returned is in the range [-pi/2, pi/2]
'''
def _get_ellipse_angle(M):
	
	# get eigenvectors / eigenvalues
	r = np.linalg.eig(M)
	eig_vecs = r[1]; lambdas = r[0]

	v1 = eig_vecs[:,0]; v2 = eig_vecs[:,1]
	L1 = lambdas[0]; L2 = lambdas[1]

	# smaller eigenvalue (in magnitude) corresponds to the eigenvector representing the major axis of the ellipse; find out which eigenvalue is smaller

	smaller = 1
	v = v2
	L = L2
	if abs(L1) < abs(L2):
		smaller = 0
		v = v1
		L = L1

	theta = np.arctan(v[1] / v[0])

	return theta



'''
Description:  2-D Gaussian function
Arguments:
	x (2xN numpy array): array containing x,y coordinate pairs at which the Gaussian function should be evaluated
	M (2x2 numpy array matrix):  inverse covariance matrix
'''
def _gaussian(x, M):
	covmat = np.linalg.inv(M)
	scaled_covmat = 2.0*np.pi*covmat
	a = 1.0 / np.sqrt( abs(np.linalg.det(scaled_covmat)) )

	f = []
	N = 1
	if np.shape(x) == (2,):
		N = 1
		arg = -0.5 * np.dot(x.T, np.dot(M, x))
		f.append(a * np.exp(arg) )
	else:
		N = len(x[0,:])
		for i in range(N):
			X = x[:,i]
			arg = -0.5 * np.dot(X.T, np.dot(M, X))
			f.append(a * np.exp(arg) )

	f = np.array(f)

	return f






'''
Description:  This function takes a symmetric inverse covariance matrix, M, and a parameter alpha; then a 2-D Gaussian is constructed, centered at zero, and an energy width interval [-a,a] such that when the Gaussian is integrated between the lines y=-a to y=a, the resulting integral value is alpha
'''
def _integrated_energy_width_from_ellipse(M, alpha):

	# create the gaussian function
	def func(y, x):
		X = np.array([x, y])
		return _gaussian(X, M)


	# find y range (E range) such that the function integrates to zero along the infinite strip corresponding to that y range
	r = np.linalg.eig(M)
	lambdas = r[0]
	#max_lambda = max(abs(lambdas[0]), abs(lambdas[1]))  # we will use this to determine bounds for x axis integration
	min_lambda = min(abs(lambdas[0]), abs(lambdas[1])) # min lambda corresponds to max (co)variance direction
	max_lambda = 1.0 / min_lambda  # this is not actually a "max_lambda" but a max (co)variance
	x_bound = 5 * max_lambda
	xu = x_bound
	xl = - x_bound

	# iteratively find y range
	y0 = 5 * max_lambda
	y1 = y0
	y2 = y0
	A, err = sp.integrate.dblquad(func, xl, xu, (lambda x: -y0), (lambda x: y0))
	epsilon = 0.01

	# create a variable to keep track of the minimum lower bound of y1 known to be too small
	smallest = 0.0
	
	# while(abs(A - alpha) > epsilon):
	# 	if A > alpha:
	# 		y0 = y1
	# 		if (0.5 * y1) > smallest:
	# 			y1 = 0.5 * y1
	# 		else:
	# 			y1 = y1 - (0.5 * (y1 - smallest))

	# 		A, err = sp.integrate.dblquad(func, xl, xu, (lambda x: -y1), (lambda x: y1))
	# 		y2 = y0
	# 	elif A < alpha:
	# 		smallest = y1
	# 		y0 = y1
	# 		y1 = (y2 + y1) / 2.0
	# 		A, err = sp.integrate.dblquad(func, xl, xu, (lambda x: -y1), (lambda x: y1))
	# 	print "A = " + str(A)

	# Try alternative strategy
	lub = 5 * max_lambda
	glb = 0.0
	y = lub
	A, err = sp.integrate.dblquad(func, xl, xu, (lambda x: -y), (lambda x: y))
	epsilon = 0.01

	while (abs(A - alpha) > epsilon) and ( (lub - glb) > 0.005):
		y = glb + 0.5 * (lub - glb)
		A, err = sp.integrate.dblquad(func, xl, xu, (lambda x: -y), (lambda x: y))

		if A > alpha:
			lub = y
			#y = glb + 0.5 * (lub - glb)
			#A, err = sp.integrate.dblquad(func, xl, xu, (lambda x: -y), (lambda x: y))
	
		elif A < alpha:
			glb = y
			#smallest = y1
			#y0 = y1
			#y1 = (y2 + y1) / 2.0
			#A, err = sp.integrate.dblquad(func, xl, xu, (lambda x: -y1), (lambda x: y1))
		
		print "A = " + str(A) + " +/- err = " + str(err) 
		print "corresponding to y = " + str(y)

	return 2.0*y  # this is the energy width




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


def _save_covmat_and_mcvine_matrices(covmat_matrices, mcvine_matrices, E_values, hkl_values, Ei):

	# Create an output file to save results
	outfile = "Ei=" + str(Ei) + "__covmat_and_mcvine_matrices.h5"
	out = hf.File(outfile, 'w')

	# convert lists to numpy arrays
	cov_mats = np.array(covmat_matrices)
	mcv_mats = np.array(mcvine_matrices)
	E_vals = np.array(E_values)
	hkl_vals = np.array(hkl_values)
	for hkl in hkl_vals:
		hkl = np.array(hkl)

	#print "np.shape(cov_mats) = " + str(np.shape(cov_mats))

	# make new numpy arrays to hold information of inverse covariance matrices
	covmat_data = []
	mcvine_data = []
	for i in range(len(covmat_matrices)):
		C = covmat_matrices[i]
		var_q = C[0][0]
		cov_qE = C[0][1]
		var_E = C[1][1]
		C_data = np.array([var_q, cov_qE, var_E])
		covmat_data.append(C_data)

		M = mcvine_matrices[i]
		var_q = M[0][0]
		cov_qE = M[0][1]
		var_E = M[1][1]
		M_data = np.array([var_q, cov_qE, var_E])
		mcvine_data.append(M_data)

	covmat_data = np.array(covmat_data)
	mcvine_data = np.array(mcvine_data)


	# Create datasets to store data
	covmats = out.create_dataset("covmat_inverse_covariance_matrices", data=covmat_data)
	covmats.attrs['columns'] = "var_q, cov_qE, var_E"
	mcvmats = out.create_dataset("mcvine_inverse_covariance_matrices", data=mcvine_data)
	mcvmats.attrs['columns'] = "var_q, cov_qE, var_E"
	E = out.create_dataset("E_values", data=E_vals)
	hkl = out.create_dataset("hkl_values", data=hkl_vals)

	# return output file name
	return outfile





def _get_covmat_and_mcvine_inv_cov_matrices(paramList, hkl_dir_passed, Ei, workdir, startdir):
	
	# change into working directory
	os.chdir(workdir)

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


	# iterate through all or several Ei,E,q points, computing the "covmat" method covariance matrix at each point; for each, compare to an (already completed) mcvine resolution simulation ellipse
	dirs = "out.res_comps_Ei*"
	if Ei==60.0:
		dirs = "out.res_comps_Ei=60.0*"
	elif Ei==125.0:
		dirs = "out.res_comps_Ei=125.0*"
	elif Ei==250.0:
		dirs = "out.res_comps_Ei=250.0*"
	#list_pts = glob.glob("out.res_comps_Ei=125.0*")
	list_pts = glob.glob(dirs)

	# create lists to hold all covmat method and mcvine method inverse covariance matrices
	covmat_matrices = []
	mcvine_matrices = []
	# Also, collect the E values and hkl values
	E_values = []
	hkl_values = []

	# now compute the covmat and mcvine inverse covariance matrices
	for point in list_pts:
		#Ei_pt, E_pt, hkl_pt = _get_Ei_E_hkl_from_filename(point)
		Ei_pt, E_pt, hkl_pt = _get_Ei_E_hkl_from_dirname(point)
		#print Ei, E, hkl

		E_values.append(E_pt)
		hkl_values.append(hkl_pt)

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

		covmat_matrices.append(covmat_cov_inv)

		# Now, we lookup the mcvine resolution simulation data and compute the corresponding covariance matrix to compare:
		resfile = point + "/res.h5"
		mcvine_covmat = compute_mcvine_res_sim_covmat._get_mcvine_res_sim_covmat(resfile)
		mcvine_cov_inv = np.linalg.inv(mcvine_covmat)

		mcvine_matrices.append(mcvine_cov_inv)

	# sanity check
	if len(covmat_matrices) != len(mcvine_matrices):
		print "WARNING!!  Should have the same number of covmat and mcvine results!!"

	#outfile = _save_covmat_and_mcvine_matrices(covmat_matrices, mcvine_matrices, E_values, hkl_values, Ei_pt)

	# return to starting directory
	os.chdir(startdir)


	return [covmat_matrices, mcvine_matrices, E_values, hkl_values]

		


def _get_covmat_and_mcvine_thetas_and_Ewidths(covmat_matrices, mcvine_matrices, alpha):

	#covmat_matrices, mcvine_matrices, E_values, hkl_values = _get_covmat_and_mcvine_inv_cov_matrices(paramList, hkl_dir)

	N = len(covmat_matrices) # = len(mcvine_matrices)

	# make lists to collect thetas and Ewidths
	covmat_thetas = []
	covmat_Ewidths = []
	mcvine_thetas = []
	mcvine_Ewidths = []

	for i in range(N):
		invcovmat = covmat_matrices[i]
		cov_theta = _get_ellipse_angle(invcovmat)
		cov_Ewidth = _integrated_energy_width_from_ellipse(invcovmat, alpha)
		covmat_thetas.append(cov_theta)
		covmat_Ewidths.append(cov_Ewidth)

		invmcvmat = mcvine_matrices[i]
		mcv_theta = _get_ellipse_angle(invmcvmat)
		mcv_Ewidth = _integrated_energy_width_from_ellipse(invmcvmat, alpha)
		mcvine_thetas.append(mcv_theta)
		mcvine_Ewidths.append(mcv_Ewidth)

		print "thetas and widths computed for i=" + str(i)

	return [covmat_thetas, covmat_Ewidths, mcvine_thetas, mcvine_Ewidths]



def _plot_thetas_vs_E(covmat_thetas, mcvine_thetas, E_values, Ei):

	cov_thetas = np.array(covmat_thetas)
	mcv_thetas = np.array(mcvine_thetas)
	E_vals = np.array(E_values)

	plt.figure()
	plt.plot(E_vals, cov_thetas, label="covmat")
	plt.plot(E_vals, mcv_thetas, label="mcvine")
	plt.legend()
	plt.title("Energy Transfer vs. Covariance Ellipse Angle")
	plt.xlabel("E (meV)")
	plt.ylabel("Covariance Ellipse Angle (radians)")
	title = "Ei=" + str(Ei) + "__E_vs_ellipse_angle.png"
	plt.savefig(title)


def _plot_Ewidths_vs_E(covmat_Ewidths, mcvine_Ewidths, E_values, Ei, alpha):

	cov_widths = np.array(covmat_Ewidths)
	mcv_widths = np.array(mcvine_Ewidths)
	E_vals = np.array(E_values)

	plt.figure()
	plt.plot(E_vals, cov_widths, label="covmat")
	plt.plot(E_vals, mcv_widths, label="mcvine")
	plt.legend()
	plt.title("Energy Transfer vs. Energy Width")
	plt.xlabel("E (meV)")
	ylabel = "E width (meV) (alpha=" + str(alpha) + ")"
	plt.ylabel(ylabel)
	title = "Ei=" + str(Ei) + "__E_vs_Ewidth.png"
	plt.savefig(title)


def _save_and_plot_thetas_Ewidths_vs_E(covmat_matrices, mcvine_matrices, E_values, Ei, alpha, outfile):

	# open outfile in read/write mode
	f = hf.File(outfile, 'r+')

	# get angles and E widths
	covmat_thetas, covmat_Ewidths, mcvine_thetas, mcvine_Ewidths = _get_covmat_and_mcvine_thetas_and_Ewidths(covmat_matrices, mcvine_matrices, alpha)

	# save this data to the output file
	cov_thetas = np.array(covmat_thetas)
	cov_widths = np.array(covmat_Ewidths)
	mcv_thetas = np.array(mcvine_thetas)
	mcv_widths = np.array(mcvine_Ewidths)

	thetas = np.array([cov_thetas, mcv_thetas])
	widths = np.array([cov_widths, mcv_widths])

	theta_data = f.create_dataset("ellipse_angles", data=thetas)
	theta_data.attrs['columns'] = "covmat_angle, mcvine_angle"
	width_data = f.create_dataset("E_widths", data=widths)
	width_data.attrs['columns'] = "covmat_Ewidth, mcvine_Ewidth"

	alpha_arr = np.array([alpha])
	alpha_data = f.create_dataset("alpha", data=alpha_arr)


	# Now plot 
	_plot_thetas_vs_E(covmat_thetas, mcvine_thetas, E_values, Ei)
	_plot_Ewidths_vs_E(covmat_Ewidths, mcvine_Ewidths, E_values, Ei, alpha)

	print "All data saved and plotted"




def _get_reordered_Es_thetas_Ewidths_from_file(outfile):

	f = hf.File(outfile, 'r')

	Es = f.get("E_values")
	Es = np.array(Es)
	Es = Es.tolist()

	Ewidths = f.get("E_widths")
	Ewidths = np.array(Ewidths)
	Ewidths = Ewidths.T

	thetas = f.get("ellipse_angles")
	thetas = np.array(thetas)
	thetas = thetas.T

	print "np.shape(Ewidths) = " + str(np.shape(Ewidths))
	print "np.shape(thetas) = " + str(np.shape(thetas))

	#Es_ordered = []
	#widths_ordered = []
	#thetas_ordered = []

	Es_ordered = sorted(Es)
	widths_ordered = []
	thetas_ordered = []
	for E in Es_ordered:
		i = Es.index(E)

		width = Ewidths[i]
		widths_ordered.append(width)

		theta = thetas[i]
		thetas_ordered.append(theta)

	widths_ordered = np.array(widths_ordered)
	thetas_ordered = np.array(thetas_ordered)
	Es_ordered = np.array(Es_ordered)

	print "Es = " + str(Es)
	print "Es_ordered = " + str(Es_ordered)

	print "widths = "
	print Ewidths

	print "widths_ordered = " 
	print widths_ordered

	print "thetas = "
	print thetas 

	print "thetas_ordered = "
	print thetas_ordered


	return [Es_ordered, thetas_ordered, widths_ordered]







if __name__ == '__main__':

	startdir = os.getcwd()
	workdir = sys.argv[1]
	#os.chdir(workdir)

	paramList = [10., 8., 0.01, 0.01, 0.0015, 13.6, 11.41]
	hkl_dir = np.array([1, 0, 0])
	Ei = 125.0
	alpha = 0.5

	# compute the matrices
	#covmat_matrices, mcvine_matrices, E_values, hkl_values = _get_covmat_and_mcvine_inv_cov_matrices(paramList, hkl_dir, Ei, workdir, startdir)

	# save the results to a file
	#outfile = _save_covmat_and_mcvine_matrices(covmat_matrices, mcvine_matrices, E_values, hkl_values, Ei)
	#print "Results saved in output file:  " + outfile
	#_save_and_plot_thetas_Ewidths_vs_E(covmat_matrices, mcvine_matrices, E_values, Ei, alpha, outfile)

	outfile = "Ei=125.0__covmat_and_mcvine_matrices.h5"
	Es, thetas, widths = _get_reordered_Es_thetas_Ewidths_from_file(outfile)
	thetas = thetas.T
	cov_thetas = thetas[0]
	mcv_thetas = thetas[1]
	widths = widths.T
	cov_widths = widths[0]
	mcv_widths = widths[1]
	_plot_thetas_vs_E(cov_thetas, mcv_thetas, Es, Ei)
	_plot_Ewidths_vs_E(cov_widths, mcv_widths, Es, Ei, alpha)

	#Try computing angle and Ewidth now for a single matrix
	# C = covmat_matrices[3]
	# M = mcvine_matrices[3]

	# print "C = "
	# print C
	# print "M = "
	# print M

	# C_theta = _get_ellipse_angle(C)
	# M_theta = _get_ellipse_angle(M)

	# print "C_theta = " + str(C_theta)
	# print "M_theta = " + str(M_theta)

	# #C_Ewidth = _integrated_energy_width_from_ellipse(C, alpha)
	# #print "C_Ewidth = " + str(C_Ewidth)
	# #M_Ewidth = _integrated_energy_width_from_ellipse(M, alpha)
	# #print "M_Ewidth = " + str(M_Ewidth)
	# xu = 0.5
	# xl = -0.5
	# yu = 10.0
	# yl = -10.0
	# num = 100
	# #M = np.array([[5.2, 2.1], [2.1, 3.65]])

	# x = np.linspace(xu, xl, num=num)
	# y = np.linspace(yu, yl, num=num)
	# #coords = np.array([x, y])
	# coords = np.meshgrid(x, y)
	# Xs, Ys = coords
	# xs = Xs.flatten()
	# ys = Ys.flatten()
	# coord_vec = np.array([xs, ys])
	# #f = _gaussian(coord_vec, M)
	# f = _gaussian(coord_vec, C)





	# # print "np.shape(xs) = " + str(np.shape(xs))
	# # print "np.shape(ys) = " + str(np.shape(ys))
	# # print "np.shape(f) = " + str(np.shape(f))
	# # print np.amin(f), np.amax(f)

	# # E_width = _integrated_energy_width_from_ellipse(M, 0.5)
	# # print "E_width = " + str(E_width)

	# plotting_xs = xs * 20

	# heatmap, xedges, yedges = np.histogram2d(plotting_xs, ys, bins=num, weights=f)
	# extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
	# plt.clf()
	# plt.imshow(heatmap.T, extent=extent, origin='lower')
	# plt.show()