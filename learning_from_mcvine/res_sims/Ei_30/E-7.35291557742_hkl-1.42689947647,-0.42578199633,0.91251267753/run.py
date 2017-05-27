#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-7.35291557742_hkl-1.42689947647,-0.42578199633,0.91251267753/sample/sampleassembly.xml'
psi = -0.00011056065189202761
hkl2Q = array([[ -6.60577245e-01,   9.34416435e-01,   7.77936350e-17],
       [  6.60732198e-01,   4.67098650e-01,  -8.09165116e-01],
       [ -6.60732198e-01,  -4.67098650e-01,  -8.09165116e-01]])
pp = array([ 2.66083211,  1.38563071,  0.27865346])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0068118686236652223
Q = array([ 0.05832294, -1.95843396, -0.39384549])
E = -7.3529155774209407
hkl_projection = array([ 0.13655409, -0.39451419, -0.21391375])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
