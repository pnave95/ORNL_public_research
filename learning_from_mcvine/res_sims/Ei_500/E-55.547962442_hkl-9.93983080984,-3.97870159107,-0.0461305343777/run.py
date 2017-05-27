#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-55.547962442_hkl-9.93983080984,-3.97870159107,-0.0461305343777/sample/sampleassembly.xml'
psi = -0.0016876597808697133
hkl2Q = array([[ -6.59102757e-01,   9.35457068e-01,   7.77070948e-17],
       [  6.61468037e-01,   4.66056029e-01,  -8.09165116e-01],
       [ -6.61468037e-01,  -4.66056029e-01,  -8.09165116e-01]])
pp = array([ 2.16974755,  2.07176147, -0.60615995])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016863764090624422
Q = array([  3.95009984, -11.13108344,   3.25675376])
E = -55.547962441985874
hkl_projection = array([-0.48640527, -0.48794715,  0.96246573])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
