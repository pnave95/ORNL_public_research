#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E32.0236267423_hkl-2.1844575787,1.10773713115,0.0138153854142/sample/sampleassembly.xml'
psi = -0.006702984323061492
hkl2Q = array([[-0.65440287,  0.9387509 ,  0.        ],
       [ 0.66379713,  0.4627327 , -0.80916512],
       [-0.66379713, -0.4627327 , -0.80916512]])
pp = array([ 2.70977328,  1.28729515,  0.7564077 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0053446654403691979
Q = array([ 2.15565742, -1.54446816, -0.90752117])
E = 32.02362674233423
hkl_projection = array([ 0.44389496,  0.31443722, -0.15153936])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
