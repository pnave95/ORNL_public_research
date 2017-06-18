# This program is designed to iterate through a sequence of Ei,E,dq values and compute covariance ellipses for each point.  The code is largely taken from the "1-test" jupyter notebook

#NOTE:  the mcvine-unstable environment is needed for this code to run properly

# Tools
import mcvine.cli
#from mcvine_workflow.singlextal.resolution import use_covmat, use_res_comps
from mcvine_workflow.singlextal.resolution import use_res_comps
import use_covmat

import numpy as np
import histogram as H, histogram.hdf as hh

from matplotlib import pyplot as plt
#import pandas as pd
import os
import glob

import find_E_Q_pairs_for_various_Ei as get_Eq_pairs



# Sample
sampleyml = "Si.yml"


# Instrument
instrument = use_covmat.instrument(
    name = 'ARCS',
    detsys_radius = "3.*meter",
    L_m2s = "13.6*meter",
    #L_m2s = "13.5*meter",
    #L_m2s = "8.1*meter",
    L_m2fc = "11.61*meter",
    #L_m2fc = "11.51*meter",
    #L_m2fc = "9.41*meter",
    offset_sample2beam = "-0.15*meter" # offset from sample to saved beam
    )
pixel = use_covmat.pixel(
    radius = "0.5*inch",
    height = "meter/128",
    pressure = "10*atm",
    )


# Given a list of Ei values, along with an hkl point and slice direction, find measurable (by ARCS) E,Q points
def _get_valid_E_Q_points(EiValues, hkl0_passed, hkl_dir_passed):
    all_pairs = get_Eq_pairs.compute_E_dq_pairs_for_Ei_list(Ei_Values, hkl0, hkl_dir)

    # make a directory to record all results
    workdir = os.getcwd()  # current working directory

    counter = 0
    counter_str = str(counter)
    newdir = "covmat_results" + counter_str + "_hkl0=" + str(hkl0_passed[0]) + "," + str(hkl0_passed[1]) + "," + str(hkl0_passed[2]) + ",  hkl_dir=" + str(hkl_dir_passed[0]) + "," + str(hkl_dir_passed[1]) + "," + str(hkl_dir_passed[2])

    # check if directory already exists; if so, increment counter
    list_results = glob.glob("covmat_results*")
    while (newdir in list_results):
        counter += 1
        counter_str = str(counter)
        newdir = "covmat_results" + counter_str + "_hkl0=" + str(hkl0_passed[0]) + "," + str(hkl0_passed[1]) + "," + str(hkl0_passed[2]) + ",  hkl_dir=" + str(hkl_dir_passed[0]) + "," + str(hkl_dir_passed[1]) + "," + str(hkl_dir_passed[2])

    newdirpath = workdir + "/" + newdir

    try:
        os.mkdir(newdirpath)
    except:
        cmd = "rm -r " + newdir
        os.system(cmd)
        os.mkdir(newdirpath)

    # create list to collect results
    data = []

    # loop through Ei values
    for i in range(len(EiValues)):
        Ei = EiValues[i]   
        Eq_pairs = all_pairs[i]

        # loop through all E, dq pairs for a fixed Ei
        #for j in range(8):
        for j in range(len(Eq_pairs)):
            E_coord = Eq_pairs[j][0]
            dq_coord = Eq_pairs[j][1]

            class dynamics:
                #hkl0 = [-16/3.,-8/3.,8/3.]
                #hkl_dir = np.array([-1.,1.,-1.])/3
                hkl0 = hkl0_passed
                hkl_dir = hkl_dir_passed
                #E = 40.
                #dq = 0
                E = E_coord
                dq = dq_coord
            class scan:
                #psimin, psimax, dpsi = -5, 90., 0.5
                min, max, step = -5., 90., 0.5
                #psimin, psimax, dpsi = 45., 47., 0.2


            # compute covariance matrix
            #tofwidths = use_covmat.tofwidths(P=10,M=8)
            #beamdivs = use_covmat.beamdivs(theta = 0.01, phi = 0.01)
            #samplethickness = 0.0015

            # compute covariance matrix (with revised parameters)
            tofwidths = use_covmat.tofwidths(P=11.2874,M=6.9908)
            beamdivs = use_covmat.beamdivs(theta = 0.0020705, phi = 0.0114589)
            samplethickness = 0.004168


            # the code which computes the "measurable" E,dq points is not perfect and sometimes produces points which don't work; hence we "try" to use these points
            try:
                # u is a list of points to plot
                # mR holds both eigenvectors for the covariance matrix
                # lambdas are eigenvalues of the covariance matrix
                '''
                u, mR, lambdas = use_covmat.compute(
                    sampleyml, Ei, dynamics, scan,
                    instrument, pixel,
                    tofwidths, beamdivs, samplethickness,
                    plot=False)
                '''
                cm_res = use_covmat.compute(
                    sampleyml, Ei, dynamics, scan,
                    instrument, pixel,
                    tofwidths, beamdivs, samplethickness,
                    plot=False)
                u = cm_res['u']
                mR = cm_res['mR']
                lambdas = cm_res['lambdas']
                
                plt.figure()
                plt.plot(u[:,0], u[:,1], '.')
                figtitle = "covmat_ellipse_Ei=" + str(Ei) + ", E=" + str(dynamics.E) + ", dq=" + str(dynamics.dq) + ".png"
                figpath = newdir + "/" + figtitle
                plt.savefig(figpath)
                
                # debug:
                # print "Ei, E, dq = " + str(Ei) + ", " + str(dynamics.E) + ", " + str(dynamics.dq) + ".  Unscaled covariance matrix: \n"
                # print cov
                # print "\n\n"


                # find E width of ellipse
                uE = u[:,1]
                Ewidth = np.amax(uE) - np.amin(uE)

                data_entry = [Ei, dynamics.E, dynamics.dq, Ewidth]
                # if I wished to collect the major and minor axis widths, I would need to use RR / lambdas[i], for i=1,2 (but his requires RR to be known)

                data.append(data_entry)

            except:
                pass

            #print "Ei, E, dq = " + str(Ei) + ", " + str(dynamics.E) + ", " + str(dynamics.dq)
            #print u
            #print "\n\n"

    # create Pandas dataframe to store data and save as a csv file
    data = np.array(data)
    print "data.shape = " + str(data.shape)
    #df = pd.DataFrame(data=data, columns=['Ei', 'E', 'dq', 'E_width'])
    #localpath = newdir + "/covmat_data.csv"
    #df.to_csv('covmat_data.csv', index=False)
    #df.to_csv(localpath, index=False)

    
    # plot E vs Ewidth for each value of Ei
    for Ei in EiValues:
        relevant_points = data[data[:,0] == Ei]  # this extracts all points for a given Ei value
        plt.figure()
        Es = relevant_points[:,1]
        dEs = relevant_points[:,3]
        plt.plot(Es, dEs)
        plt.xlabel("E (meV)")
        plt.ylabel("E width (meV)")
        figtitle = "Energy vs Energy Width for Ei=" + str(Ei) + ".png"
        figpath = newdir + "/" + figtitle
        plt.savefig(figpath)
    

    #return df



if __name__ == '__main__':

    Ei_Values = np.array([30., 60., 125., 250., 500., 1000.])
    #hkl0 = np.array([-16/3., -8/3., 8/3.])
    #hkl_dir = np.array([-1.,1.,-1.])

    hkl0 = np.array([0., 0., 0.])
    hkl_dir = np.array([0.,0.,1.])

    #df = _get_valid_E_Q_points(Ei_Values, hkl0, hkl_dir)
    _get_valid_E_Q_points(Ei_Values, hkl0, hkl_dir)