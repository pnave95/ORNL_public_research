

import numpy as np
import os
import glob
import sys


def _get_Ei_E_dq_from_filename(filename):

	s1 = filename[18:]
	print s1
	i = s1.index(',')
	Ei = s1[:i]

	ii = i + 4
	s2 = s1[ii:]
	j = s2.index(',')
	E = s2[:j]

	jj = j + 5
	s3 = s2[jj:]
	k = s3.index('p') - 1
	dq = s3[:k]

	return [Ei, E, dq]


def _get_hkl(hkl0, hkl_dir, dq):
	hkl = hkl0 + hkl_dir * dq
	return hkl


def _copy_files_with_name_change(workdir, hkl0, hkl_dir):

	current_dir = os.getcwd()
	print "current_dir = " + current_dir
	
	os.chdir(workdir)
	print "changed to workdir = " + workdir

	# collect list of all relevant files
	png_list = glob.glob("mcvine_res_sim_Ei*dq*.png")

	# copy the files to the new directory
	for filename in png_list:
		cmd = "cp " + '"' + filename + '"' + " " + current_dir
		#print cmd
		os.system(cmd)

	# change back to 'current_dir'
	os.chdir(current_dir)
	print "changed back to current_dir = " + str(os.getcwd())

	# rename files
	png_list = glob.glob("mcvine_res_sim_Ei*dq*.png")
	for filename in png_list:
		Ei, E, dq = _get_Ei_E_dq_from_filename(filename)
		dq_float = float(dq)
		hkl = _get_hkl(hkl0, hkl_dir, dq_float)
		h = hkl[0]
		k = hkl[1]
		l = hkl[2]

		newfilename = "mcvine_res_sim_Ei=" + Ei + "__E=" + E + "__hkl=[" + str(h) + ", " + str(k) + ", " + str(l) + "].png"
		#newpath = current_dir + "/" + newfilename

		# save the file with the new name
		cmd2 = "mv " + '"' + filename + '"' + " " + '"' + newfilename + '"'
		os.system(cmd2)

	



if __name__ == '__main__':

	hkl0 = np.array([0., 0., 0.])
	hkl_dir = np.array([2., 0., 0.])

	workdir = sys.argv[1]
	workdir = os.path.abspath(workdir)
	print "directory = " + workdir

	_copy_files_with_name_change(workdir, hkl0, hkl_dir)


	
