#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-54.02960007_hkl-20.5050543551,1.53042777716,-5.85458766561/sample/sampleassembly.xml'
psi = -0.005532488425215385
hkl2Q = array([[ -6.55501222e-01,   9.37984285e-01,  -7.74977281e-17],
       [  6.63255049e-01,   4.63509359e-01,  -8.09165116e-01],
       [ -6.63255049e-01,  -4.63509359e-01,  -8.09165116e-01]])
pp = array([-0.51074983,  2.95620273, -0.6542299 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016877334958085119
Q = array([ 18.33923697, -15.81039497,   3.49895934])
E = -54.029600069954313
hkl_projection = array([ 0.46851231,  0.78316252, -0.93344545])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
