#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-13.0140158467_hkl-8.51943848907,-1.48404038302,0.679277971415/sample/sampleassembly.xml'
psi = -0.0016712769381788488
hkl2Q = array([[ -6.59118082e-01,   9.35446270e-01,   7.77079918e-17],
       [  6.61460401e-01,   4.66066866e-01,  -8.09165116e-01],
       [ -6.61460401e-01,  -4.66066866e-01,  -8.09165116e-01]])
pp = array([ 1.81794083,  2.38643901, -0.17309668])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.002390050130689686
Q = array([ 4.18436653, -8.97772797,  0.65118567])
E = -13.014015846707167
hkl_projection = array([-0.41292277, -0.0279298 ,  0.5306875 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
