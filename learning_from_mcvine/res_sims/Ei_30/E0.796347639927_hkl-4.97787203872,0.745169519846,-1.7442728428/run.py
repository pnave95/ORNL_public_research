#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E0.796347639927_hkl-4.97787203872,0.745169519846,-1.7442728428/sample/sampleassembly.xml'
psi = -0.005212402197654323
hkl2Q = array([[-0.65580142,  0.93777442,  0.        ],
       [ 0.66310665,  0.46372163, -0.80916512],
       [-0.66310665, -0.46372163, -0.80916512]])
pp = array([-0.89342497,  2.86387706, -0.65892452])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0069826655775970439
Q = array([ 4.91526136, -3.51371278,  0.80843956])
E = 0.79634763992702418
hkl_projection = array([-0.44199447, -0.90806185, -0.43736505])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
