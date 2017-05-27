#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E6.07333656424_hkl-1.04572858678,0.309069108397,0.416878135822/sample/sampleassembly.xml'
psi = -0.0022293143206168504
hkl2Q = array([[-0.65859597,  0.93581394,  0.        ],
       [ 0.66172038,  0.46569767, -0.80916512],
       [-0.66172038, -0.46569767, -0.80916512]])
pp = array([ 2.85616788,  0.91777177,  0.52401067])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0071049781374474151
Q = array([ 0.6173732 , -1.0288138 , -0.58741119])
E = 6.0733365642382182
hkl_projection = array([ 0.44258607,  0.04291884,  0.12854078])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
