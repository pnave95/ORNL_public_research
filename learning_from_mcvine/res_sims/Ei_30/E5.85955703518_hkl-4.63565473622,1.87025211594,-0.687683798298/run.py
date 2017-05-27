#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E5.85955703518_hkl-4.63565473622,1.87025211594,-0.687683798298/sample/sampleassembly.xml'
psi = -0.005581480481770741
hkl2Q = array([[-0.65545527,  0.9380164 ,  0.        ],
       [ 0.66327776,  0.46347686, -0.80916512],
       [-0.66327776, -0.46347686, -0.80916512]])
pp = array([-0.83453947,  2.88158704,  0.87181973])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0071351968128716969
Q = array([ 4.73508631, -3.16277604, -0.95689303])
E = 5.8595570351843378
hkl_projection = array([-0.64073757, -0.85202396,  0.71472377])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
