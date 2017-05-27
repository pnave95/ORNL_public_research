#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-169.442033738_hkl-0.137631494386,1.07179100383,4.06474024257/sample/sampleassembly.xml'
psi = 0.005825398644994163
hkl2Q = array([[ -6.66112233e-01,   9.30478836e-01,   7.81228420e-17],
       [  6.57947895e-01,   4.71012477e-01,  -8.09165116e-01],
       [ -6.57947895e-01,  -4.71012477e-01,  -8.09165116e-01]])
pp = array([ 2.98846469,  0.26282851,  0.71037138])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016622195530860242
Q = array([-1.87752663, -1.53777963, -4.1563019 ])
E = -169.44203373807517
hkl_projection = array([ 0.12002414, -0.02399978, -0.54248918])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
