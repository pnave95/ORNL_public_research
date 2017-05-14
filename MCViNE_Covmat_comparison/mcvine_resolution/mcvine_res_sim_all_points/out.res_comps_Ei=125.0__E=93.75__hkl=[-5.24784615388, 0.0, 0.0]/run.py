#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[2 0 0]/out.res_comps_tmp20/sample/sampleassembly.xml'
psi = 0.43448282312005915
hkl2Q = array([[-0.99259906,  0.5694238 , -0.        ],
       [ 0.40264343,  0.70187353, -0.80916512],
       [-0.40264343, -0.70187353, -0.80916512]])
pp = array([ 1.96722591,  2.26495524,  0.        ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0039875835066678061
Q = array([ 5.20900718, -2.98824852,  0.        ])
E = 93.75
hkl_projection = array([2, 0, 0])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
