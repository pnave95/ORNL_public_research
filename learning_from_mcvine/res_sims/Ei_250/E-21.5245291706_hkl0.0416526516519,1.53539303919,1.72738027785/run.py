#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-21.5245291706_hkl0.0416526516519,1.53539303919,1.72738027785/sample/sampleassembly.xml'
psi = 0.0106850693861857
hkl2Q = array([[ -6.70626170e-01,   9.27230776e-01,   7.83965039e-17],
       [  6.55651169e-01,   4.74204313e-01,  -8.09165116e-01],
       [ -6.55651169e-01,  -4.74204313e-01,  -8.09165116e-01]])
pp = array([ 2.99996701,  0.0140694 ,  0.70860863])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023941513548588105
Q = array([-0.15381002, -0.05241956, -2.64012235])
E = -21.524529170611117
hkl_projection = array([ 0.91998188, -0.02191626, -0.22797049])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
