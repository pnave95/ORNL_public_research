#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E20.497346292_hkl-3.3850505029,0.974499827563,-1.24042915781/sample/sampleassembly.xml'
psi = -0.006395167830163126
hkl2Q = array([[-0.6546918 ,  0.93854942,  0.        ],
       [ 0.66365466,  0.46293701, -0.80916512],
       [-0.66365466, -0.46293701, -0.80916512]])
pp = array([ 0.1850827 ,  2.99428529, -0.2994484 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0078983837452946092
Q = array([ 3.68611275, -2.1516646 ,  0.21518074])
E = 20.497346291978403
hkl_projection = array([-0.44258514, -0.33377596, -0.86463382])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
