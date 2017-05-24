#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E98.5170419596_hkl-4.9007303377,1.62126817672,-2.04312384538/sample/sampleassembly.xml'
psi = -0.00941044319986747
hkl2Q = array([[-0.65185884,  0.94051923,  0.        ],
       [ 0.66504753,  0.46093381, -0.80916512],
       [-0.66504753, -0.46093381, -0.80916512]])
pp = array([ 1.79087637,  2.4068157 , -0.28134093])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0040927966762613352
Q = array([ 5.63157925, -2.92018896,  0.34135089])
E = 98.517041959568076
hkl_projection = array([-0.19430634,  0.064485  , -0.93062361])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
