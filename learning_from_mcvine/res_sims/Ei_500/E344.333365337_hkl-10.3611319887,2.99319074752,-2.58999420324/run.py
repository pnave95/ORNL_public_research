#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E344.333365337_hkl-10.3611319887,2.99319074752,-2.58999420324/sample/sampleassembly.xml'
psi = -0.007011120887748594
hkl2Q = array([[ -6.54113572e-01,   9.38952505e-01,   7.74178148e-17],
       [  6.63939683e-01,   4.62528142e-01,  -8.09165116e-01],
       [ -6.63939683e-01,  -4.62528142e-01,  -8.09165116e-01]])
pp = array([ 1.74798932,  2.43814137,  0.11131042])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0019326427755627529
Q = array([ 10.4842551 ,  -7.14623067,  -0.32625258])
E = 344.33336533653267
hkl_projection = array([-0.32883175, -0.86678016, -0.69512598])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
