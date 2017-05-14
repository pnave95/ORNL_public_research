#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[1 0 0]/out.res_comps_tmp7/sample/sampleassembly.xml'
psi = 0.6302057551547307
hkl2Q = array([[-1.0843868 ,  0.36551557, -0.        ],
       [ 0.25845854,  0.76677726, -0.80916512],
       [-0.25845854, -0.76677726, -0.80916512]])
pp = array([ 1.62564312,  2.52136559,  0.        ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0066957415871206211
Q = array([ 4.44152569, -1.49711044,  0.        ])
E = 54.0
hkl_projection = array([1, 0, 0])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
