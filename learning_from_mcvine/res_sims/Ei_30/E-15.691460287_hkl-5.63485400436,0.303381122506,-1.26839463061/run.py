#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-15.691460287_hkl-5.63485400436,0.303381122506,-1.26839463061/sample/sampleassembly.xml'
psi = -0.003879223659405491
hkl2Q = array([[-0.65705106,  0.93689929,  0.        ],
       [ 0.66248784,  0.46460526, -0.80916512],
       [-0.66248784, -0.46460526, -0.80916512]])
pp = array([-0.59751177,  2.9398945 , -0.50464151])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0067145846962018089
Q = array([ 4.74366913, -4.54903541,  0.78085527])
E = -15.691460286959277
hkl_projection = array([ 0.13916183, -0.12988524, -0.22252118])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
