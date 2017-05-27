#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-11.471421321_hkl-0.579362241311,-0.812168892945,0.175689238922/sample/sampleassembly.xml'
psi = 0.0012948225613532032
hkl2Q = array([[-0.66188981,  0.93348715,  0.        ],
       [ 0.66007509,  0.46802677, -0.80916512],
       [-0.66007509, -0.46802677, -0.80916512]])
pp = array([ 2.97710327,  0.36994069, -0.1899235 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033694618681672783
Q = array([-0.26858659, -1.00317126,  0.51501713])
E = -11.471421320989421
hkl_projection = array([ 0.52030862, -0.91595951, -0.09850013])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
