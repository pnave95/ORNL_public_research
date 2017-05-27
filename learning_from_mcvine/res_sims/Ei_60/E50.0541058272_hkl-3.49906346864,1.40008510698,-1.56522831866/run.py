#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E50.0541058272_hkl-3.49906346864,1.40008510698,-1.56522831866/sample/sampleassembly.xml'
psi = -0.01065576602832567
hkl2Q = array([[ -6.50687087e-01,   9.41330275e-01,  -7.72222599e-17],
       [  6.65621021e-01,   4.60105251e-01,  -8.09165116e-01],
       [ -6.65621021e-01,  -4.60105251e-01,  -8.09165116e-01]])
pp = array([ 1.54207687,  2.57332449, -0.17822396])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0061391792067792394
Q = array([ 4.25057036, -1.9294181 ,  0.13362813])
E = 50.05410582716604
hkl_projection = array([ 0.64371578,  0.05319596, -0.53536101])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
