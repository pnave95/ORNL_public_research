#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E21.5624905606_hkl-6.30255352706,1.62624189346,-3.04540882937/sample/sampleassembly.xml'
psi = -0.009223338511404177
hkl2Q = array([[-0.65203481,  0.94039725,  0.        ],
       [ 0.66496127,  0.46105823, -0.80916512],
       [-0.66496127, -0.46105823, -0.80916512]])
pp = array([-1.29710188,  2.70509274, -0.82331472])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0051595906424893251
Q = array([ 7.21595107, -3.77300096,  1.14834038])
E = 21.562490560579775
hkl_projection = array([ 0.36476778,  0.84327638, -0.7667928 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
