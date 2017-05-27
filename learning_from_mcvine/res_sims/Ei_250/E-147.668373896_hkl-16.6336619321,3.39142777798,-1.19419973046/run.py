#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-147.668373896_hkl-16.6336619321,3.39142777798,-1.19419973046/sample/sampleassembly.xml'
psi = -0.003729557970172876
hkl2Q = array([[-0.65719128,  0.93680094,  0.        ],
       [ 0.6624183 ,  0.46470441, -0.80916512],
       [-0.6624183 , -0.46470441, -0.80916512]])
pp = array([-0.64175068,  2.93055559,  0.38734017])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023138832706396085
Q = array([ 13.96910108, -13.45146879,  -1.77792029])
E = -147.6683738958971
hkl_projection = array([-0.28619373, -0.05690922,  0.87844811])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
