#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E44.9034687562_hkl-4.16253229967,1.0944954941,-1.79715662762/sample/sampleassembly.xml'
psi = -0.008665827806325455
hkl2Q = array([[-0.65255899,  0.94003359,  0.        ],
       [ 0.66470412,  0.46142888, -0.80916512],
       [-0.66470412, -0.46142888, -0.80916512]])
pp = array([ 0.85672703,  2.87506849, -0.63393178])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0057917159117934101
Q = array([ 4.63839094, -2.57862835,  0.56856888])
E = 44.903468756152165
hkl_projection = array([ 0.75326946, -0.44898733,  0.61432964])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
