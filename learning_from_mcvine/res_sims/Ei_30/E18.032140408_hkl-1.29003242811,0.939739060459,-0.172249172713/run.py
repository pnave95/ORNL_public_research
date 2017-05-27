#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E18.032140408_hkl-1.29003242811,0.939739060459,-0.172249172713/sample/sampleassembly.xml'
psi = -0.008475597898225867
hkl2Q = array([[-0.6527378 ,  0.93990943,  0.        ],
       [ 0.66461633,  0.46155532, -0.80916512],
       [-0.66461633, -0.46155532, -0.80916512]])
pp = array([ 2.86347981,  0.89469736,  0.7945868 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0077202781079047499
Q = array([ 1.58109847, -0.69926956, -0.62102604])
E = 18.032140407992053
hkl_projection = array([-0.49817868, -0.3837732 , -0.69655651])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
