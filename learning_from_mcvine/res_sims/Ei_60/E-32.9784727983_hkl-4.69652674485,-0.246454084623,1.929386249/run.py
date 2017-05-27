#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-32.9784727983_hkl-4.69652674485,-0.246454084623,1.929386249/sample/sampleassembly.xml'
psi = -0.0014655511139577552
hkl2Q = array([[-0.65931051,  0.93531065,  0.        ],
       [ 0.66136451,  0.46620294, -0.80916512],
       [-0.66136451, -0.46620294, -0.80916512]])
pp = array([ 1.70946771,  2.46530326,  0.62088353])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047450213145455991
Q = array([ 1.6574459 , -5.40709465, -1.36177   ])
E = -32.978472798318862
hkl_projection = array([ 0.95354778, -0.99046567, -0.61549754])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
