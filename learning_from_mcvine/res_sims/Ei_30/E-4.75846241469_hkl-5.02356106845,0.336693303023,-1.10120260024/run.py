#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-4.75846241469_hkl-5.02356106845,0.336693303023,-1.10120260024/sample/sampleassembly.xml'
psi = -0.003917783442727391
hkl2Q = array([[ -6.57014935e-01,   9.36924622e-01,  -7.75853782e-17],
       [  6.62505753e-01,   4.64579716e-01,  -8.09165116e-01],
       [ -6.62505753e-01,  -4.64579716e-01,  -8.09165116e-01]])
pp = array([-0.32057908,  2.98282233, -0.45688593])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0068611740544617028
Q = array([ 4.25316896, -4.03868078,  0.61861425])
E = -4.7584624146939056
hkl_projection = array([ 0.25233718,  0.28233418, -0.86884077])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
