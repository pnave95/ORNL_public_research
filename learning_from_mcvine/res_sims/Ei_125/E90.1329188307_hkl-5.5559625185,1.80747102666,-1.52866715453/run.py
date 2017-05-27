#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E90.1329188307_hkl-5.5559625185,1.80747102666,-1.52866715453/sample/sampleassembly.xml'
psi = -0.007733970309634262
hkl2Q = array([[-0.65343468,  0.93942509,  0.        ],
       [ 0.66427385,  0.46204809, -0.80916512],
       [-0.66427385, -0.46204809, -0.80916512]])
pp = array([ 1.40969334,  2.64816251,  0.162433  ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.00392731800880657
Q = array([ 5.84656794, -3.67795428, -0.22559837])
E = 90.13291883073083
hkl_projection = array([ 0.53660075, -0.43557627, -0.23214879])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
