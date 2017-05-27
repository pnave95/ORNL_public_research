#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-25.6317781983_hkl-7.38984562062,0.75541269983,-0.293386662734/sample/sampleassembly.xml'
psi = -0.004127326479477125
hkl2Q = array([[-0.65681859,  0.93706227,  0.        ],
       [ 0.66260309,  0.46444088, -0.80916512],
       [-0.66260309, -0.46444088, -0.80916512]])
pp = array([-0.06613041,  2.99927104,  0.17417772])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047608362256473949
Q = array([ 5.54872571, -6.43764024, -0.37385535])
E = -25.631778198300498
hkl_projection = array([ 0.01394199, -0.36152987,  0.09435168])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
