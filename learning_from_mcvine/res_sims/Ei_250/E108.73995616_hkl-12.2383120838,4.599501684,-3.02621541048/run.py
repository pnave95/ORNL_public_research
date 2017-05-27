#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E108.73995616_hkl-12.2383120838,4.599501684,-3.02621541048/sample/sampleassembly.xml'
psi = -0.005924938963115835
hkl2Q = array([[-0.65513306,  0.93824146,  0.        ],
       [ 0.6634369 ,  0.46324903, -0.80916512],
       [-0.6634369 , -0.46324903, -0.80916512]])
pp = array([-0.75028625,  2.90466358,  0.46513589])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0025481673187172935
Q = array([ 13.07690496,  -7.94988582,  -1.27304837])
E = 108.73995615969812
hkl_projection = array([ 0.56325116,  0.43243183, -0.5713468 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
