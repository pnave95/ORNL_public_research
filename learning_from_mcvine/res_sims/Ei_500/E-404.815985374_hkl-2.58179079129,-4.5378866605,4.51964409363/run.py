#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-404.815985374_hkl-2.58179079129,-4.5378866605,4.51964409363/sample/sampleassembly.xml'
psi = 0.0030441787429318834
hkl2Q = array([[-0.66352179,  0.93232784,  0.        ],
       [ 0.65925534,  0.46918076, -0.80916512],
       [-0.65925534, -0.46918076, -0.80916512]])
pp = array([  2.84455301e+00,   9.53162211e-01,  -2.11364128e-03])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016181839559239303
Q = array([-4.25815104, -6.65669459,  0.01476125])
E = -404.81598537366051
hkl_projection = array([ 0.10776319, -0.80495462, -0.38715273])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
