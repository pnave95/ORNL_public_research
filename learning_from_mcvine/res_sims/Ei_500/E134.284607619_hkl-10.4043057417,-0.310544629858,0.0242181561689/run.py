#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E134.284607619_hkl-10.4043057417,-0.310544629858,0.0242181561689/sample/sampleassembly.xml'
psi = -0.003183537500065883
hkl2Q = array([[ -6.57702691e-01,   9.36441959e-01,  -7.76253674e-17],
       [  6.62164459e-01,   4.65066033e-01,  -8.09165116e-01],
       [ -6.62164459e-01,  -4.65066033e-01,  -8.09165116e-01]])
pp = array([ 2.01648652,  2.22121186, -0.0519888 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017471588972179579
Q = array([ 6.62127186, -9.89871525,  0.23168539])
E = 134.28460761896986
hkl_projection = array([ 0.89001826, -0.71084665,  0.83032183])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
