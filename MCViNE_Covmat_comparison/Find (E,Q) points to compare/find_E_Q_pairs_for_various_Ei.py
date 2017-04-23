#  The purpose of this script is to perform essentially the same task as the notebooks in this directory: find valid E,Q points for different Ei's.  This script computes multiple points for multiple Ei values to be used in comparing the correlation / covariance matrix method and MCViNE simulation method for analyzing ARCS resolution effects.


import numpy as np
import mcvine.cli
from mcvine_workflow.DGS import ARCS
import histogram.hdf as hh, histogram as H

from mcvine_workflow.singlextal import dynrange
from mcvine_workflow.sample import loadSampleYml


# This function takes the dynamics parameters (Ei, hkl0, and hkl_dir) and then computes valid (ARCS measurable) E,Q points, which it returns
def compute_E_dq_pairs(Ei, hkl0, hkl_dir, verbose=False):

    # Inputs

    # ARCS parameters
    L_PM=11.61
    R = 3.
    L_PS=13.6
    L_MS=L_PS-L_PM

    # Sample
    sample_yml = './Si.yml'


    # Dynamics parameters -- these will be passed into this function

    # sample angle range parameters
    psimin = -5.
    psimax = 90.
    dpsi = 1.

    # Dynamic Range:
    sample = loadSampleYml(sample_yml)
    psilist = np.arange(psimin, psimax, dpsi)
    qaxis = np.arange(-100, 100, .02)

    
    points_in_slice = list(dynrange.iterPointsInSlice(
            sample, psilist, Ei, hkl0, hkl_dir, qaxis,
            ARCS.scattering_angle_constraints,
            Erange=(-Ei, Ei)))
    all_qs = np.concatenate([qs for _p, qs, _E in points_in_slice ])
    qmin = np.min(all_qs); qmax = np.max(all_qs)

    all_Es = np.concatenate([Es for _p, _q, Es in points_in_slice ])
    Emin = np.min(all_Es); Emax = np.max(all_Es)



    fractions = [.9, .5, .25, 1./8, 1./16, 1./32, 1./64, 1./128]
    Eq_pairs = []
    for f in fractions:
        E = f*Ei
        #print 'E=', E
        # find maximum Es smaller than E
        max_Es_smaller = np.max(all_Es[all_Es<E])
        # find minimum Es greater than E
        min_Es_greater = np.min(all_Es[all_Es>E])
        # print E, max_Es_smaller, min_Es_greater
        Ebracket = min(max_Es_smaller, E*.99), max(min_Es_greater, E*1.01)
        # get qs
        qs = all_qs[ (all_Es>=Ebracket[0])*(all_Es<=Ebracket[1]) ]
        # print len(qs)
        while len(qs) < 10:
            Ebracket = Ebracket[0]*.95, Ebracket[1]*1.05
            qs = all_qs[ (all_Es>=Ebracket[0])*(all_Es<=Ebracket[1]) ]

        if verbose == True:
            print "Ebracket=", Ebracket, 'number of qs=', len(qs)

        Eq_pairs.append( (E, np.mean(qs)))
    Eq_pairs = np.array(Eq_pairs)

    return Eq_pairs


def compute_E_dq_pairs_for_Ei_list(Ei_list, hkl0, hkl_dir, verbose=False):

    list_of_pairs = []
    for Ei in Ei_list:
        pairs = compute_E_dq_pairs(Ei, hkl0, hkl_dir, verbose)
        list_of_pairs.append(pairs)

    list_of_pairs = np.array(list_of_pairs)
    return list_of_pairs



if __name__ == '__main__':

    Ei_Values = np.array([30., 60., 125., 250., 500., 1000.])
    hkl0 = np.array([0., 0., 0.])
    hkl_dir = np.array([1,0,0])
    all_pairs = compute_E_dq_pairs_for_Ei_list(Ei_Values, hkl0, hkl_dir)

    for i in range(len(Ei_Values)):
        Ei = Ei_Values[i]
        pairs = all_pairs[i]
        print "Ei = " + str(Ei) + "\n"
        print pairs
        print "\n\n"





