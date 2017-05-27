#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-4.87492961714_hkl-8.60281485244,-0.825949662391,-2.07173901348/sample/sampleassembly.xml'
psi = -0.004191789807778925
hkl2Q = array([[-0.65675819,  0.93710461,  0.        ],
       [ 0.66263303,  0.46439817, -0.80916512],
       [-0.66263303, -0.46439817, -0.80916512]])
pp = array([ 0.52457698,  2.95378046, -0.92550765])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0034106780380550434
Q = array([ 6.47547025, -7.48319519,  2.34470859])
E = -4.8749296171360328
hkl_projection = array([-0.00823789, -0.73109865, -0.98668294])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
