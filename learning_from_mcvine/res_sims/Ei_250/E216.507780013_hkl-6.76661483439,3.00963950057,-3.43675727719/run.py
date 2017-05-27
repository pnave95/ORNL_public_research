#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E216.507780013_hkl-6.76661483439,3.00963950057,-3.43675727719/sample/sampleassembly.xml'
psi = -0.009303329902795749
hkl2Q = array([[-0.65195958,  0.9404494 ,  0.        ],
       [ 0.66499815,  0.46100504, -0.80916512],
       [-0.66499815, -0.46100504, -0.80916512]])
pp = array([ 1.69618057,  2.47446388, -0.25213369])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0031265512965878233
Q = array([ 8.69840129, -3.39183747,  0.34560881])
E = 216.50778001285732
hkl_projection = array([ 0.49200904,  0.16086807,  0.43723577])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
