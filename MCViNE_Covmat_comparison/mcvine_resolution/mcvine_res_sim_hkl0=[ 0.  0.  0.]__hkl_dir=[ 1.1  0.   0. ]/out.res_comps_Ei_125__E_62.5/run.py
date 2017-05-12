#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[ 1.1  0.   0. ]/out.res_comps_tmp16/sample/sampleassembly.xml'
psi = 0.1668369045848139
hkl2Q = array([[-0.8066678 ,  0.81165475,  0.        ],
       [ 0.57392658,  0.57040027, -0.80916512],
       [-0.57392658, -0.57040027, -0.80916512]])
pp = array([ 2.24762698,  1.987001  ,  0.        ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.003643048313977743
Q = array([ 3.65007971, -3.67264513,  0.        ])
E = 62.5
hkl_projection = array([ 1.1,  0. ,  0. ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
