#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[2 0 0]/out.res_comps_tmp11/sample/sampleassembly.xml'
psi = 0.49240366720065676
hkl2Q = array([[-1.0238976 ,  0.51100888, -0.        ],
       [ 0.36133784,  0.72400494, -0.80916512],
       [-0.36133784, -0.72400494, -0.80916512]])
pp = array([ 1.84587474,  2.36489882,  0.        ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0059550489084337823
Q = array([ 3.89103592, -1.94194604,  0.        ])
E = 48.0
hkl_projection = array([2, 0, 0])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
