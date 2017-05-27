#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-93.8761871532_hkl-11.5343646448,-0.759883248789,-3.03774531703/sample/sampleassembly.xml'
psi = -0.004511478047869563
hkl2Q = array([[ -6.56458572e-01,   9.37314523e-01,   7.75531045e-17],
       [  6.62781455e-01,   4.64186308e-01,  -8.09165116e-01],
       [ -6.62781455e-01,  -4.64186308e-01,  -8.09165116e-01]])
pp = array([-0.38947199,  2.97461116, -0.93712645])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032681197130941891
Q = array([ 9.08155728, -9.75397511,  3.07290856])
E = -93.876187153229182
hkl_projection = array([-0.32421079, -0.24403343, -0.7868646 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
