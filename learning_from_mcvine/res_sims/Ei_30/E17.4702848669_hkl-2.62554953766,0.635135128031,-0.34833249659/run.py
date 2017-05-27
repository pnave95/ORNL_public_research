#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E17.4702848669_hkl-2.62554953766,0.635135128031,-0.34833249659/sample/sampleassembly.xml'
psi = -0.004411986588054026
hkl2Q = array([[-0.65655182,  0.93724921,  0.        ],
       [ 0.66273527,  0.46425225, -0.80916512],
       [-0.66273527, -0.46425225, -0.80916512]])
pp = array([ 1.75330373,  2.4343225 ,  0.28187309])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0076172415933381445
Q = array([ 2.37558802, -2.00421717, -0.23207068])
E = 17.470284866936495
hkl_projection = array([-0.36573626,  0.50784953, -0.78660485])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
