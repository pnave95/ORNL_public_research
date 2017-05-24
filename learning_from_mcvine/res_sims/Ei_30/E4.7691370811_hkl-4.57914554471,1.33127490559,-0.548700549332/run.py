#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E4.7691370811_hkl-4.57914554471,1.33127490559,-0.548700549332/sample/sampleassembly.xml'
psi = -0.004628704722666074
hkl2Q = array([[-0.65634869,  0.93739147,  0.        ],
       [ 0.66283587,  0.46410861, -0.80916512],
       [-0.66283587, -0.46410861, -0.80916512]])
pp = array([-0.37641185,  2.97629201,  0.55108669])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0070703675098454663
Q = array([ 4.25163133, -3.41993918, -0.63323187])
E = 4.769137081103942
hkl_projection = array([-0.35792288,  0.43966483, -0.77524028])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
