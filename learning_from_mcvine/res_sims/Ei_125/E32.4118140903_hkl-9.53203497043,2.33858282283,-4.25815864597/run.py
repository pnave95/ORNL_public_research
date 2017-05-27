#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E32.4118140903_hkl-9.53203497043,2.33858282283,-4.25815864597/sample/sampleassembly.xml'
psi = -0.008734199274373904
hkl2Q = array([[-0.65249471,  0.9400782 ,  0.        ],
       [ 0.66473567,  0.46138344, -0.80916512],
       [-0.66473567, -0.46138344, -0.80916512]])
pp = array([-1.28326473,  2.71168428, -0.71180826])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0035116073507012184
Q = array([ 10.60469178,  -5.91723102,   1.55325379])
E = 32.411814090319155
hkl_projection = array([-0.85197463,  0.72023438, -0.91732069])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
