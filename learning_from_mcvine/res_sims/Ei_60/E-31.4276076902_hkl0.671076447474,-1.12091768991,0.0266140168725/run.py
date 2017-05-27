#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-31.4276076902_hkl0.671076447474,-1.12091768991,0.0266140168725/sample/sampleassembly.xml'
psi = -0.04779437969025404
hkl2Q = array([[-0.61528673,  0.96484123,  0.        ],
       [ 0.68224578,  0.43507342, -0.80916512],
       [-0.68224578, -0.43507342, -0.80916512]])
pp = array([ 2.99924435, -0.06733014, -0.40222843])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047423440456505553
Q = array([-1.1958031 ,  0.14822168,  0.88547236])
E = -31.427607690213463
hkl_projection = array([-0.05646276, -0.35811969, -0.84112952])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
