#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E40.8799946684_hkl-19.544413436,5.45608815026,-2.69186684884/sample/sampleassembly.xml'
psi = -0.005966675198018851
hkl2Q = array([[ -6.55093900e-01,   9.38268807e-01,   7.74742276e-17],
       [  6.63456236e-01,   4.63221339e-01,  -8.09165116e-01],
       [ -6.63456236e-01,  -4.63221339e-01,  -8.09165116e-01]])
pp = array([-0.52755944,  2.95324923,  0.45356665])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017128349025220895
Q = array([ 18.20923757, -14.56360685,  -2.23671145])
E = 40.879994668406312
hkl_projection = array([ 0.7917316 , -0.17183331, -0.29829447])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
