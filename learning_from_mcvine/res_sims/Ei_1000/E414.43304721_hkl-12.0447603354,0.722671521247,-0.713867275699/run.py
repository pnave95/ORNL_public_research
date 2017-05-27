#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E414.43304721_hkl-12.0447603354,0.722671521247,-0.713867275699/sample/sampleassembly.xml'
psi = -0.004559838512106476
hkl2Q = array([[ -6.56413242e-01,   9.37346268e-01,   7.75504779e-17],
       [  6.62803903e-01,   4.64154255e-01,  -8.09165116e-01],
       [ -6.62803903e-01,  -4.64154255e-01,  -8.09165116e-01]])
pp = array([  2.33917583e+00,   1.87836536e+00,   1.25964588e-03])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012637834719453728
Q = array([  8.85848371e+00,  -1.06233356e+01,  -7.12408837e-03])
E = 414.43304720964443
hkl_projection = array([-0.12659639, -0.0207826 , -0.40228187])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
