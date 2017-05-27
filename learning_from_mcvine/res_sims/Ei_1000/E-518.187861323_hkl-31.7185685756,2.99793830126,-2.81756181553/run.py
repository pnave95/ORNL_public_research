#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-518.187861323_hkl-31.7185685756,2.99793830126,-2.81756181553/sample/sampleassembly.xml'
psi = -0.004989064737126008
hkl2Q = array([[-0.65601085,  0.93762793,  0.        ],
       [ 0.66300307,  0.46386972, -0.80916512],
       [-0.66300307, -0.46386972, -0.80916512]])
pp = array([-0.28442112,  2.986487  ,  0.01611868])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.001158357387127129
Q = array([ 24.6634195 , -27.04258144,  -0.14595436])
E = -518.18786132278069
hkl_projection = array([-0.20438296,  0.93230171,  0.1757294 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
