#  The purpose of this file is to compute the covariance matrix associated to a mcvine resolution simulation


import numpy as np
import histogram as H, histogram.hdf as hh
from matplotlib import pyplot as plt


def _get_mcvine_res_sim_covmat(resfile):
	
	res = hh.load(resfile)
	
	q = res.x
	E = res.E
	dE = E[1]-E[0]
	dq = q[1]-q[0]
	Eg, qg = np.mgrid[slice(E[0], E[-1]+dE/2, E[1]-E[0]), slice(q[0], q[-1]+dq/2, q[1]-q[0])]

