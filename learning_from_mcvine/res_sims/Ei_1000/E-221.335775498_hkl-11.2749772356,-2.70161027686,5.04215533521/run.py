#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-221.335775498_hkl-11.2749772356,-2.70161027686,5.04215533521/sample/sampleassembly.xml'
psi = -0.0008947738940640112
hkl2Q = array([[-0.65984426,  0.93493418,  0.        ],
       [ 0.6610983 ,  0.46658035, -0.80916512],
       [-0.6610983 , -0.46658035, -0.80916512]])
pp = array([ 2.43917373,  1.74654845,  0.23369089])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011789343655225675
Q = array([  2.32033874, -14.15445049,  -1.89388741])
E = -221.33577549794393
hkl_projection = array([-0.53020083, -0.36537833,  0.40962936])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
