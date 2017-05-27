#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-157.924982877_hkl-7.02817827356,-2.89176060814,3.23324730716/sample/sampleassembly.xml'
psi = -0.0002260439590169511
hkl2Q = array([[ -6.60469331e-01,   9.34492715e-01,   7.77872850e-17],
       [  6.60786135e-01,   4.67022343e-01,  -8.09165116e-01],
       [ -6.60786135e-01,  -4.67022343e-01,  -8.09165116e-01]])
pp = array([ 2.22538446,  2.01188072,  0.05896305])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023067776048781258
Q = array([ 0.5945759 , -9.42829694, -0.27631912])
E = -157.92498287695057
hkl_projection = array([ 0.03111452,  0.24946993, -0.05185703])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
