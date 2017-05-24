#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E176.585053023_hkl-16.7913179094,1.88746004713,-5.93596393347/sample/sampleassembly.xml'
psi = -0.006367080901161538
hkl2Q = array([[ -6.54718159e-01,   9.38531035e-01,  -7.74525811e-17],
       [  6.63641659e-01,   4.62955650e-01,  -8.09165116e-01],
       [ -6.63641659e-01,  -4.62955650e-01,  -8.09165116e-01]])
pp = array([-0.14267725,  2.99660528, -0.80879801])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017828927421583893
Q = array([ 16.18553082, -12.13727464,   3.27590812])
E = 176.58505302311585
hkl_projection = array([ 0.77852331, -0.61132641,  0.80643711])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
