#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-584.254994499_hkl-8.00658356155,-2.54242735651,8.63241793292/sample/sampleassembly.xml'
psi = 0.0008945111900977844
hkl2Q = array([[-0.66151607,  0.93375204,  0.        ],
       [ 0.6602624 ,  0.4677625 , -0.80916512],
       [-0.6602624 , -0.4677625 , -0.80916512]])
pp = array([ 2.65555258,  1.39572221,  0.5414208 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011574585202893959
Q = array([ -2.08184646, -12.70333724,  -4.92780793])
E = -584.25499449893493
hkl_projection = array([ 0.03990747,  0.84111854,  0.42384699])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
