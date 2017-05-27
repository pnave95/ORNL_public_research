#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-105.927283515_hkl0.145440576994,-2.37311559524,1.46674735151/sample/sampleassembly.xml'
psi = 0.0075961905955011354
hkl2Q = array([[-0.66775887,  0.92929783,  0.        ],
       [ 0.6571128 ,  0.47217683, -0.80916512],
       [-0.6571128 , -0.47217683, -0.80916512]])
pp = array([ 2.96187869,  0.47673327, -0.20837313])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032350121535657606
Q = array([-2.62034232, -1.67793669,  0.73340157])
E = -105.92728351536614
hkl_projection = array([-0.91970462, -0.40530938,  0.42397981])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
