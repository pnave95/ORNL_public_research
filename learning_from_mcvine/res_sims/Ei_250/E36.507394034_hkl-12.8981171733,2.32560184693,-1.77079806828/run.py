#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E36.507394034_hkl-12.8981171733,2.32560184693,-1.77079806828/sample/sampleassembly.xml'
psi = -0.003947136337074555
hkl2Q = array([[ -6.56987433e-01,   9.36943907e-01,  -7.75837813e-17],
       [  6.62519390e-01,   4.64560269e-01,  -8.09165116e-01],
       [ -6.62519390e-01,  -4.64560269e-01,  -8.09165116e-01]])
pp = array([-0.04844128,  2.99960888,  0.13225654])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0024357722198953438
Q = array([ 11.18784527, -10.18178764,  -0.44892786])
E = 36.507394033950504
hkl_projection = array([-0.28938798, -0.31686602,  0.00598012])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
