#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/notebooks/3-generate-samples-for-fitting/tmp.use_res_comps/E-940.3357965_hkl-30.7705367397,-4.33257929438,-1.60464016031/sample/sampleassembly.xml'
psi = -0.0033461347734874912
hkl2Q = array([[ -6.57550419e-01,   9.36548887e-01,   7.76165047e-17],
       [  6.62240069e-01,   4.64958360e-01,  -8.09165116e-01],
       [ -6.62240069e-01,  -4.64958360e-01,  -8.09165116e-01]])
pp = array([ 0.36241006,  2.97802937, -0.47552976])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011401652263518425
Q = array([ 18.42662873, -30.08649004,   4.80419087])
E = -940.33579649969647
hkl_projection = array([0, 0, 1])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
