#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E18.6667405772_hkl-3.64628433973,1.68777532261,-0.851120538423/sample/sampleassembly.xml'
psi = -0.006764053828897013
hkl2Q = array([[ -6.54345536e-01,   9.38790866e-01,  -7.74311444e-17],
       [  6.63825388e-01,   4.62692166e-01,  -8.09165116e-01],
       [ -6.63825388e-01,  -4.62692166e-01,  -8.09165116e-01]])
pp = array([-0.33441567,  2.98130276,  0.89767993])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0077941464715506554
Q = array([ 4.07131341, -2.24837121, -0.67699187])
E = 18.666740577244653
hkl_projection = array([-0.22038366,  0.15620737,  0.53160932])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
