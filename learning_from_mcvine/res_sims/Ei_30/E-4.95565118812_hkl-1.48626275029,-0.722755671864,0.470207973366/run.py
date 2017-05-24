#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-4.95565118812_hkl-1.48626275029,-0.722755671864,0.470207973366/sample/sampleassembly.xml'
psi = -0.0003683085454233658
hkl2Q = array([[ -6.60336380e-01,   9.34586667e-01,   7.77794652e-17],
       [  6.60852570e-01,   4.66928332e-01,  -8.09165116e-01],
       [ -6.60852570e-01,  -4.66928332e-01,  -8.09165116e-01]])
pp = array([ 2.6433642 ,  1.41867041, -0.14897166])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0068459728748923587
Q = array([ 0.19306027, -1.94606987,  0.20435279])
E = -4.9556511881222818
hkl_projection = array([-0.39127337, -0.96622442, -0.79918623])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
