#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-98.4799571019_hkl-20.759115994,5.57086282432,-0.876600192199/sample/sampleassembly.xml'
psi = -0.005176524247686971
hkl2Q = array([[-0.65583507,  0.93775089,  0.        ],
       [ 0.66309001,  0.46374542, -0.80916512],
       [-0.66309001, -0.46374542, -0.80916512]])
pp = array([-0.41159167,  2.97163125,  0.68505273])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016772080559865478
Q = array([ 17.88980462, -16.47689804,  -3.79843357])
E = -98.47995710192572
hkl_projection = array([-0.04524122, -0.99203712, -0.26756261])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
