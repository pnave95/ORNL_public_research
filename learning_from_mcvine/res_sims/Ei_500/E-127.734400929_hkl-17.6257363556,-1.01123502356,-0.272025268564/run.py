#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-127.734400929_hkl-17.6257363556,-1.01123502356,-0.272025268564/sample/sampleassembly.xml'
psi = -0.0031364502613596664
hkl2Q = array([[ -6.57746785e-01,   9.36410988e-01,   7.76279348e-17],
       [  6.62142560e-01,   4.65097212e-01,  -8.09165116e-01],
       [ -6.62142560e-01,  -4.65097212e-01,  -8.09165116e-01]])
pp = array([ 0.7747276 ,  2.89824035, -0.17861542])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016639682120115377
Q = array([ 11.10380917, -16.84873759,   1.03836946])
E = -127.73440092884584
hkl_projection = array([ 0.68223603, -0.76247277,  0.2526447 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
