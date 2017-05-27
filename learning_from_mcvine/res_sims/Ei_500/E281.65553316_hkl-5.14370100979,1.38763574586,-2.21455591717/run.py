#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E281.65553316_hkl-5.14370100979,1.38763574586,-2.21455591717/sample/sampleassembly.xml'
psi = -0.008684772483120117
hkl2Q = array([[-0.65254118,  0.94004595,  0.        ],
       [ 0.66471286,  0.46141629, -0.80916512],
       [-0.66471286, -0.46141629, -0.80916512]])
pp = array([ 2.8556661 ,  0.9193319 , -0.19385405])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0018509087281645721
Q = array([ 5.75089985, -3.17320537,  0.66911496])
E = 281.65553316002399
hkl_projection = array([ 0.62781049, -0.71301034, -0.64452609])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
