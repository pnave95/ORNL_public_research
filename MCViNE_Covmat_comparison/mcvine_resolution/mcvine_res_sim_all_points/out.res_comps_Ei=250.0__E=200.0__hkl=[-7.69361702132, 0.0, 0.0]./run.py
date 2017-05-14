#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[2 0 0]/out.res_comps_tmp27/sample/sampleassembly.xml'
psi = 0.4965439405040878
hkl2Q = array([[-1.02600454,  0.50676529, -0.        ],
       [ 0.35833718,  0.72549477, -0.80916512],
       [-0.35833718, -0.72549477, -0.80916512]])
pp = array([ 1.8779774 ,  2.33948731,  0.        ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0029208870709076309
Q = array([ 7.89368596, -3.89885809,  0.        ])
E = 200.0
hkl_projection = array([2, 0, 0])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
