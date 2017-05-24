import numpy as np
from matplotlib import pyplot as plt
import h5py as hf


def _get_res_data(resfile):
	f = hf.File(resfile, 'r')

	q_hdf = f.get("res/grid/x/bin centers")
	E_hdf = f.get("res/grid/E/bin centers")
	I_hdf = f.get("res/data")
	q = np.array(q_hdf)
	E = np.array(E_hdf)
	I = np.array(I_hdf)
	I = I.T

	return [q, E, I]


def _normalize_intensity(I):
	sum_weights = np.sum(np.sum(I))

	M = I
	if sum_weights != 0.0:
		M = I / sum_weights

	return M

def _sum_hstrip_intensity(M, center):
	return 0


def _compute_E_width(q, E, I):
	
	M = _normalize_intensity(I)





def _plot_resolution(q, E, I):

	dE = E[1] - E[0]
	dq = q[1] - q[0]
	Eg, qg = np.mgrid[slice(E[0], E[-1]+dE/2, dE), slice(q[0], q[-1]+dq/2, dq)]

	plt.pcolormesh(qg, Eg, I, cmap='viridis')
	plt.colorbar()

	plt.xlim(-1, 1)
	plt.ylim(-5,5)

	plt.show()



if __name__ == '__main__':

	resfile = "example_res.h5"

	q, E, I = _get_res_data(resfile)
	_plot_resolution(q, E, I)
	_compute_E_width(q, E, I)