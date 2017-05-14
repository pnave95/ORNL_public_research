#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[1 0 0]/out.res_comps_tmp24/sample/sampleassembly.xml'
psi = 0.0893275855521844
hkl2Q = array([[-0.74139807,  0.87167957,  0.        ],
       [ 0.61637054,  0.5242476 , -0.80916512],
       [-0.61637054, -0.5242476 , -0.80916512]])
pp = array([ 0.59707875,  2.93998248,  0.        ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.002414173602333813
Q = array([  8.8986303 , -10.46233407,   0.        ])
E = 15.625
hkl_projection = array([1, 0, 0])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
