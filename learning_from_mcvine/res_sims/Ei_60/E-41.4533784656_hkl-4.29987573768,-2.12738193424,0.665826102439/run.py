#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-41.4533784656_hkl-4.29987573768,-2.12738193424,0.665826102439/sample/sampleassembly.xml'
psi = -0.0008896449805983961
hkl2Q = array([[ -6.59849056e-01,   9.34930797e-01,   7.77508361e-17],
       [  6.61095906e-01,   4.66583742e-01,  -8.09165116e-01],
       [ -6.61095906e-01,  -4.66583742e-01,  -8.09165116e-01]])
pp = array([ 1.91542031,  2.30893158, -0.51295405])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047097585841382635
Q = array([ 0.99069055, -5.32335171,  1.18263999])
E = -41.453378465637961
hkl_projection = array([-0.51966466, -0.0717748 ,  0.36365954])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
