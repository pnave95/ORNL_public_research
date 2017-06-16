# For a specified Ei, scan through the current directory, find all png's corresponding to that Ei, then create a gif of images from low to high E


# STATUS:  incomplete

import sys
import glob

def _get_Ei_and_E_from_mcvine_res_filename(filename):

	p1 = filename.index('=') + 1
	s = filename[p1:]

	p2 = s.index('_')
	Ei = s[:p2]
	Ei = float(Ei)

	p2 = s.index('=') + 1
	s = s[p2:]
	p3 = s.index('_')

	E = s[:p3]
	E = float(E)

	return [Ei, E]


def _make_Ei_E_filename_dict(filelist):

	Ei_list = []
	E_list = []

	for filename in filelist:
		Ei, E = _get_Ei_and_E_from_mcvine_res_filename(filename)
		Ei_list.append(Ei)
		E_list.append(E)

	D = dict(filename=filelist, Ei=Ei_list, E=E_list)

	return D

# this function is incomplete
def _make_gifs():

	# collect list of all png files
	filelist = glob.glob("mcvine_res_sim_Ei=*.png")

	# make dictionary of filenames, Ei values, E values
	imagedict = _make_Ei_E_filename_dict(filelist)

	# determine all Ei values
	unique_Eis = set(imagedict['Ei'])

	# create a list of subdictionaries of imagedict (one subdict for each Ei)
	LD = []
	for Ei in unique_Eis:



if __name__ == '__main__':

	filename = sys.argv[1]
	Ei, E = _get_Ei_and_E_from_mcvine_res_filename(filename)
	print Ei, E