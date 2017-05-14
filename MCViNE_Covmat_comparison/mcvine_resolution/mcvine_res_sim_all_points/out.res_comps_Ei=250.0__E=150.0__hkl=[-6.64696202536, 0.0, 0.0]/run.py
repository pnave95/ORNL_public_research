#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[2 0 0]/out.res_comps_tmp31/sample/sampleassembly.xml'
psi = 0.2738988063152075
hkl2Q = array([[-0.88878049,  0.720809  , -0.        ],
       [ 0.50968893,  0.62846271, -0.80916512],
       [-0.50968893, -0.62846271, -0.80916512]])
pp = array([ 2.18963739,  2.05072867,  0.        ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0026476698928847714
Q = array([ 5.90769014, -4.79119007,  0.        ])
E = 150.0
hkl_projection = array([2, 0, 0])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
