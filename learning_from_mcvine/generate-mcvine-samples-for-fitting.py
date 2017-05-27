from matplotlib import pyplot as plt
import numpy as np
import os
#import historgram.hdf as hh
#import histogram as H
import h5py as hf

import mcvine.cli
from mcvine_workflow.DGS import ARCS
from mcvine_workflow import singlextal as sx
from mcvine_workflow.sample import loadSampleYml
from mcvine_workflow.singlextal import io as sxio, coords_transform, dynrange
from mcvine_workflow.singlextal.resolution import use_covmat, use_res_comps


# Instrument: ARCS

instrument = use_covmat.instrument(
    name = 'ARCS',
    detsys_radius = "3.*meter",
    L_m2s = "13.6*meter",
    L_m2fc = "11.61*meter",
    offset_sample2beam = "-0.15*meter" # offset from sample to saved beam
    )
pixel = use_covmat.pixel(
    radius = "0.5*inch",
    height = "meter/128",
    pressure = "10*atm",
    )

# scan
class psi_scan:
    min = -5
    max = 90.
    step = 1.


def _get_hklEs_for_Ei(N_samples, Ei, xtal_orientation):

	# randomly select spherical coordinates and E's
	theta_min = -5
	theta_max = 120
	thetas = np.random.random(N_samples)*(theta_max - theta_min) + theta_min

	z_min = -1.
	z_max = 1.
	zs = np.random.random(N_samples)*(z_max - z_min) + z_min

	E_min = -Ei*.95
	E_max = Ei*.95
	Es = np.random.random(N_samples)*(E_max - E_min) + E_min

	rs = np.ones(N_samples)*3. # radius of the cylinder of the detector system

	# convert to hkl values
	hkls = coords_transform.rtzE2hkl(r=rs, theta=np.deg2rad(thetas), z=zs, E=Es, xtalori=xtal_orientation, Ei=Ei)

	# hklE array
	#hklEs = np.hstack((hkls, Es[:,np.newaxis]))

	hklEs = [hkls, Es]

	return hklEs



def _get_beam_dir_for_Ei(Ei):

	beam = "/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/"
	if Ei==30.0:
		beam = beam + "beam_30_1e9"
	elif Ei==60.0:
		beam = beam + "beam_60_1e9"
	elif Ei==125.0:
		beam = beam + "beam_125_1e9"
	elif Ei==250.0:
		beam = beam + "beam_250_1e9"
	elif Ei==500.0:
		beam = beam + "beam_500_1e9"
	elif Ei==1000.0:
		beam = beam + "beam_1000_1e9"
	else:
		print "Error!!  No beam simulation exists for Ei=" + str(Ei)

	return beam


def _get_results_dir_for_Ei(Ei):

	name = "Ei_"
	if Ei==30:
		name = name + "30"
	elif Ei==60:
		name = name + "60"
	elif Ei==125:
		name = name + "125"
	elif Ei==250:
		name = name + "250"
	elif Ei==500:
		name = name + "500"
	elif Ei==1000:
		name = name + "1000"

	return name


def _setup_and_run_simulations_for_Ei(Ei, N_samples, xo, sample_yml, workdir):

	# change into appropriate directory
	dirname = _get_results_dir_for_Ei(Ei)
	os.chdir(dirname)
	current_dir_path = os.getcwd()

	# get name of directory containing beam simulation for this Ei
	beam = _get_beam_dir_for_Ei(Ei) 

	# get hklE's
	hkls, Es = _get_hklEs_for_Ei(N_samples, Ei, xo)

	# set up and run simulations
	for E, hkl in zip(Es, hkls):
		print "E,hkl = " + str(E) + ", " + str(hkl)

		# create output directory
		outdir = os.path.join(current_dir_path, 'E%s_hkl%s' % (E, '%s,%s,%s' % tuple(hkl)))

		# randomly choose hkl_dir
		h_dir = np.random.random()*2.0 - 1.0
		k_dir = np.random.random()*2.0 - 1.0
		l_dir = np.random.random()*2.0 - 1.0
		hkl_dir = np.array([h_dir, k_dir, l_dir])

		# setup the resolution computation
		use_res_comps.setup(outdir, sample_yml, beam, E, hkl, hkl_dir, psi_scan, instrument, pixel)

		# change into the new 'outdir' directory
		os.chdir(outdir)

		# record relevant information in 'outdir' in an hdf5 file
		# hklE, hkl_dir, Ei
		f = hf.File('parameters.h5', 'w')
		hkl_arr = np.array(hkl)
		E_arr = np.array([E])
		Ei_arr = np.array([Ei])
		d1 = f.create_dataset("hkl", data=hkl_arr)
		d2 = f.create_dataset("hkl_dir", data=hkl_dir)
		d3 = f.create_dataset("E", data=E_arr)
		d4 = f.create_dataset("Ei", data=Ei_arr)
		hf.File.close(f)

		# run the simulation
		os.system("python run.py")

		# change back up
		os.chdir(current_dir_path)
		
	# change back into workdir
	os.chdir(workdir)



def _setup_and_run_simulations_many_Ei(Eis, N_samples, xo, sample_yml, workdir):

	for Ei in Eis:
		_setup_and_run_simulations_for_Ei(Ei, N_samples, xo, sample_yml, workdir)

		print "Completed simulations for Ei = " + str(Ei)


if __name__ == '__main__':

	workdir = "/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims"
	#workdir = "res_sims"
	os.chdir(workdir)

	sample_yml = workdir + '/Si.yml'
	xo = sxio.loadXtalOriFromSampleYml('Si.yml')

	Eis = [30.0, 60.0, 125.0, 250.0, 500.0, 1000.0]
	N_samples = 100



	# try single Ei
	#hklEs = _get_hklEs_for_Ei(10, 30.0, xo)
	#print hklEs
	#print np.shape(hklEs)

	#_setup_and_run_simulations_for_Ei(30.0, 10, xo, sample_yml, workdir)

	_setup_and_run_simulations_many_Ei(Eis, N_samples, xo, sample_yml, workdir)