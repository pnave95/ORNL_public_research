#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-340.660816913_hkl-29.7870425633,1.89896106814,-3.34371207411/sample/sampleassembly.xml'
psi = -0.004938383857586017
hkl2Q = array([[-0.65605837,  0.93759468,  0.        ],
       [ 0.66297956,  0.46390332, -0.80916512],
       [-0.66297956, -0.46390332, -0.80916512]])
pp = array([-0.10933612,  2.99800694, -0.13746413])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.00116971423213882
Q = array([ 23.01782363, -25.49607926,   1.16904212])
E = -340.66081691273541
hkl_projection = array([-0.44427871,  0.85066543,  0.29127991])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
