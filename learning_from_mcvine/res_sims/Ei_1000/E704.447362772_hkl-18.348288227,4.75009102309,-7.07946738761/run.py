#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E704.447362772_hkl-18.348288227,4.75009102309,-7.07946738761/sample/sampleassembly.xml'
psi = -0.009243017059033723
hkl2Q = array([[-0.6520163 ,  0.94041008,  0.        ],
       [ 0.66497034,  0.46104515, -0.80916512],
       [-0.66497034, -0.46104515, -0.80916512]])
pp = array([ 0.5638666 ,  2.94653262, -0.47062059])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0013795210804907559
Q = array([ 19.82968852, -11.80095467,   1.8848501 ])
E = 704.44736277211223
hkl_projection = array([-0.05217847,  0.47937837, -0.30903039])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
