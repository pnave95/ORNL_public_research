#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E215.64123498_hkl-3.75369043774,3.07668443793,-3.70100600634/sample/sampleassembly.xml'
psi = -0.04870964756310428
hkl2Q = array([[-0.61440339,  0.96540398,  0.        ],
       [ 0.6826437 ,  0.4344488 , -0.80916512],
       [-0.6826437 , -0.4344488 , -0.80916512]])
pp = array([ 2.95947029,  0.49146272, -0.36550623])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0031169947671472178
Q = array([ 6.93302782, -0.6792682 ,  0.50517923])
E = 215.64123497957979
hkl_projection = array([-0.60268012,  0.77357982, -0.71717411])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
