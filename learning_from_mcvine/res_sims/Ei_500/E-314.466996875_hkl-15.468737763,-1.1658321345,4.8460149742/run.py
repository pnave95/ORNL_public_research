#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-314.466996875_hkl-15.468737763,-1.1658321345,4.8460149742/sample/sampleassembly.xml'
psi = -0.0017121691759252615
hkl2Q = array([[ -6.59079829e-01,   9.35473222e-01,  -7.77057529e-17],
       [  6.61479459e-01,   4.66039817e-01,  -8.09165116e-01],
       [ -6.61479459e-01,  -4.66039817e-01,  -8.09165116e-01]])
pp = array([ 1.43278414,  2.63574081,  0.4544204 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016331299720885924
Q = array([  6.21841967, -17.27235009,  -2.97787558])
E = -314.46699687488677
hkl_projection = array([ 0.21435295, -0.69362961, -0.38513222])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
