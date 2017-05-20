#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/notebooks/3-generate-samples-for-fitting/tmp.use_res_comps/E893.773140638_hkl-8.03798750389,8.40688933751,-6.31824498238/sample/sampleassembly.xml'
psi = -0.07039546898361414
hkl2Q = array([[ -5.93324987e-01,   9.78499786e-01,   7.42888779e-17],
       [  6.91903834e-01,   4.19544122e-01,  -8.09165116e-01],
       [ -6.91903834e-01,  -4.19544122e-01,  -8.09165116e-01]])
pp = array([ 2.91937591,  0.69082869,  0.6919475 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016332231236583878
Q = array([ 14.95751572,  -1.6873255 ,  -1.69005815])
E = 893.77314063819699
hkl_projection = array([0, 0, 1])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
