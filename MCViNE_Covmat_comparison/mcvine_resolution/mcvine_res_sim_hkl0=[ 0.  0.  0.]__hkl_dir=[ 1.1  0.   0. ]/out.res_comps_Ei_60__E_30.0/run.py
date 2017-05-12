#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[ 1.1  0.   0. ]/out.res_comps_tmp8/sample/sampleassembly.xml'
psi = 0.16774842787116673
hkl2Q = array([[-0.8074073 ,  0.81091912,  0.        ],
       [ 0.57340641,  0.57092318, -0.80916512],
       [-0.57340641, -0.57092318, -0.80916512]])
pp = array([ 2.27170098,  1.95943223,  0.        ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0052612869224501792
Q = array([ 2.49804068, -2.50890591,  0.        ])
E = 30.0
hkl_projection = array([ 1.1,  0. ,  0. ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
