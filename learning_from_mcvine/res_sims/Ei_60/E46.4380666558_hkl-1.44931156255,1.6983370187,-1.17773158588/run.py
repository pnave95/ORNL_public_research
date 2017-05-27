#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E46.4380666558_hkl-1.44931156255,1.6983370187,-1.17773158588/sample/sampleassembly.xml'
psi = 0.10133768941502551
hkl2Q = array([[ -7.51813308e-01,   8.62712653e-01,   8.42594007e-17],
       [  6.10029967e-01,   5.31612288e-01,  -8.09165116e-01],
       [ -6.10029967e-01,  -5.31612288e-01,  -8.09165116e-01]])
pp = array([ 2.98242571, -0.3242482 ,  0.49025328])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0058692699247713453
Q = array([ 2.84409976,  0.27861399, -0.42125576])
E = 46.438066655794117
hkl_projection = array([ 0.64161696,  0.38046975, -0.17917776])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
