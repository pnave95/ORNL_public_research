#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/notebooks/3-generate-samples-for-fitting/tmp.use_res_comps/E-727.285829721_hkl-8.74958335105,-0.839828112254,11.0287113159/sample/sampleassembly.xml'
psi = 0.0008152425363808458
hkl2Q = array([[ -6.61442048e-01,   9.33804470e-01,  -7.78446168e-17],
       [  6.60299473e-01,   4.67710157e-01,  -8.09165116e-01],
       [ -6.60299473e-01,  -4.67710157e-01,  -8.09165116e-01]])
pp = array([ 2.60804558,  1.48259849,  0.89081538])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011545667624709112
Q = array([ -2.049448  , -13.72143649,  -8.24448886])
E = -727.28582972057006
hkl_projection = array([0, 0, 1])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
