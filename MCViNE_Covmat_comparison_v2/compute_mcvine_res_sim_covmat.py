#  The purpose of this file is to compute the covariance matrix associated to a mcvine resolution simulation


import numpy as np
import histogram as H, histogram.hdf as hh
from matplotlib import pyplot as plt
import glob  # unix style pathname pattern matching
import os
import h5py as hf


def _get_mcvine_res_sim_covmat(resfile):
	
	res = hh.load(resfile)

	q = res.x
	E = res.E
	dE = E[1]-E[0]
	dq = q[1]-q[0]
	Eg, qg = np.mgrid[slice(E[0], E[-1]+dE/2, E[1]-E[0]), slice(q[0], q[-1]+dq/2, q[1]-q[0])]


	# compute the variance in q and E
	
	# we must debug:  there is some huge intensity value which is throwing everything off
	maxelement = np.max(res.I.T)
	#print maxelement
	maxindex1, maxindex2 = np.where(res.I.T == maxelement)
	#print maxindex1, maxindex2
	#print maxindex1.shape
	#print maxindex2.shape
	m11 = maxindex1[0]
	m12 = maxindex2[0]
	#print m11, m12
	withoutmax = np.copy(res.I.T)
	withoutmax[m11][m12] = 0.0
	maxelement2 = np.max(withoutmax)
	m21, m22 = np.where(withoutmax == maxelement2)
	#print maxelement2
	#print m21, m22

	#print "withoutmax[m11][m12] = " + str(withoutmax[m11][m12])

	# remove erroneous max element if it exists
	if np.fabs(maxelement - maxelement2) > 0.1*maxelement2:
	    I = withoutmax
	else:
	    I = res.I.T
	    

	weighted_qs = np.multiply(qg, I)
	weighted_Es = np.multiply(Eg, I)
	print weighted_qs.shape

	sum_weights = np.sum(I)
	print sum_weights
	q_mean = np.sum(weighted_qs) / sum_weights
	print "q_mean = " + str(q_mean)
	E_mean = np.sum(weighted_Es) / sum_weights
	print "E_mean = " + str(E_mean)

	print q.shape, E.shape

	q_avg = np.average(qg, axis=None, weights=I)
	E_avg = np.average(Eg, axis=None, weights=I)
	#print res.I.T
	print q_avg, E_avg

	
	q_avg_array = np.zeros(I.shape)
	q_avg_array.fill(q_avg)
	q_diffs = qg - q_avg_array
	q_diffs2 = np.square(q_diffs)
	w_q_diffs2 = np.multiply(q_diffs2, I)
	wq_diff_sum = np.sum(w_q_diffs2)
	Var_q = wq_diff_sum / sum_weights
	print "Var_q = " + str(Var_q)

	E_avg_array = np.zeros(I.shape)
	E_avg_array.fill(E_avg)
	E_diffs = Eg - E_avg_array
	E_diffs2 = np.square(E_diffs)
	w_E_diffs2 = np.multiply(E_diffs2, I)
	wE_diff_sum = np.sum(w_E_diffs2)
	Var_E = wE_diff_sum / sum_weights
	print "Var_E = " + str(Var_E)

	# Now, compute the covariance of q and E
	product_diffs = np.multiply(q_diffs, E_diffs)
	w_prod_diffs = np.multiply(product_diffs, I)
	sum_w_prod_diffs = np.sum(w_prod_diffs)
	Cov_qE = sum_w_prod_diffs / sum_weights
	print "Cov_qE = " + str(Cov_qE)

	covmat = np.array([[Var_q, Cov_qE], [Cov_qE, Var_E]])

	return covmat


def _get_Ei_and_E_from_dirname(dirname):
	s = dirname[17:] 
	Ei = s[:s.index('_')]

	Eindex = s.index('E')
	start = Eindex + 2
	E = s[start:]

	return [Ei, E]

def _plot_res_sim_covmat(M, figpath, showfig=False):
	N = np.linalg.inv(M)  # compute inverse of covariance matrix
	r = np.linalg.eig(N)
	mR = r[1]; lambdas = r[0]
	RR = 2*np.log(2)
	theta = np.arange(0, 360, 1.)*np.pi/180
	u1p = np.sqrt(RR/lambdas[0])*np.cos(theta)
	u2p = np.sqrt(RR/lambdas[1])*np.sin(theta)
	up = np.array([u1p, u2p]).T
	u_ = np.dot(up, mR.T)

	plt.figure()
	plt.plot(u_[:,0], u_[:,1], 'g.', label="mcvine res")
	#plt.show()
	plt.savefig(figpath)

	if showfig == True:
		plt.plot(u_[:,0], u_[:,1], 'g.', label="mcvine res")
		plt.show()


def _iterate_plotting():

	#os.chdir(parentdir)
	dirs = glob.glob('out.res_comps_Ei_*')

	# debug:
	print "current directory = " + os.getcwd() + "\n"
	print "dirs = "
	print dirs

	for dirname in dirs:
		print dirname

		resfile = dirname + "/res.h5"
		covmat = _get_mcvine_res_sim_covmat(resfile)

		Ei_str, E_str = _get_Ei_and_E_from_dirname(dirname)
		figtitle = "mcvine_res_sim_covmat_ellipse_Ei=" + Ei_str + ", E=" + E_str + ".png"
		_plot_res_sim_covmat(covmat, figtitle)

	return dirs


# must supply the directory with the mcvine result files and the current working directory
def _compute_res_sim_inv_covmat_4D(mcvine_dir, workdir):

	# change into mcvine directory
	os.chdir(mcvine_dir)
	
	# get mcvine-simulated data

	dhkls = np.load('dhkls.npy')
	dEs = np.load('dEs.npy')
	probs = np.load('probs.npy')

	# collect metadata (simulation parameters)
	f = hf.File('parameters.h5', 'r')
	E = f.get("E")
	E = np.array(E)
	E = E[0]
	Ei = f.get("Ei")
	Ei = np.array(Ei)
	Ei = Ei[0]
	hkl = f.get("hkl")
	hkl = np.array(hkl)
	hkl_dir = f.get("hkl_dir")
	hkl_dir = np.array(hkl_dir)

	params = [E, Ei, hkl, hkl_dir]

	# change back to working directory
	os.chdir(workdir)

	dhs,dks,dls = dhkls.T
	dhs_np = np.array(dhs)
	dks_np = np.array(dks)
	dls_np = np.array(dls)
	dEs_np = np.array(dEs)


	# mask outliers
	mask = (dhs_np > -2.)*(dhs_np < 2.)* (dks_np > -2.)*(dks_np < 2.)* (dls_np > -2.)*(dls_np < 2.)
	
	Data = np.array([dhs_np[mask], dks_np[mask], dls_np[mask], dEs_np[mask]])

	mcvine_cov = np.cov(Data, aweights=probs[mask])
	mcvine_inv_cov = np.linalg.inv(mcvine_cov)	



	return [mcvine_inv_cov, params]


if __name__ == '__main__':

	dirs = _iterate_plotting()