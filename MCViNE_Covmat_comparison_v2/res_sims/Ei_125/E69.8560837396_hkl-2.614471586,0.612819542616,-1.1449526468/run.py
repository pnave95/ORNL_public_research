#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison_v2/res_sims/Ei_125/E69.8560837396_hkl-2.614471586,0.612819542616,-1.1449526468/sample/sampleassembly.xml'
psi = -0.008507479723147119
hkl2Q = array([[-0.65270783,  0.93993024,  0.        ],
       [ 0.66463105,  0.46153413, -0.80916512],
       [-0.66463105, -0.46153413, -0.80916512]])
pp = array([ 2.84554419,  0.95019908, -0.24854377])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0037005402788809171
Q = array([ 2.87475605, -1.64614905,  0.43058355])
E = 69.856083739638933
hkl_projection = array([-0.37561013, -0.1349485 , -0.87035464])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
