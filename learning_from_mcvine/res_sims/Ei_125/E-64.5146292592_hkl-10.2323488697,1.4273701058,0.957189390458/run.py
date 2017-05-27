#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-64.5146292592_hkl-10.2323488697,1.4273701058,0.957189390458/sample/sampleassembly.xml'
psi = -0.0036376812889416803
hkl2Q = array([[-0.65727734,  0.93674055,  0.        ],
       [ 0.6623756 ,  0.46476527, -0.80916512],
       [-0.6623756 , -0.46476527, -0.80916512]])
pp = array([ 0.24500783,  2.98997846,  0.6159345 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032907608675883777
Q = array([ 7.03692732, -9.36653248, -1.92950236])
E = -64.514629259219504
hkl_projection = array([-0.41290513, -0.17316279,  0.49340975])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
