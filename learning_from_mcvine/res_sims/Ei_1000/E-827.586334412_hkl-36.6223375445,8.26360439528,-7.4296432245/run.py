#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-827.586334412_hkl-36.6223375445,8.26360439528,-7.4296432245/sample/sampleassembly.xml'
psi = -0.0069473239983277625
hkl2Q = array([[ -6.54173473e-01,   9.38910772e-01,   7.74212558e-17],
       [  6.63910174e-01,   4.62570499e-01,  -8.09165116e-01],
       [ -6.63910174e-01,  -4.62570499e-01,  -8.09165116e-01]])
pp = array([-1.23792911,  2.73267845,  0.06798104])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011429579833863533
Q = array([ 34.3762685 , -27.12587385,  -0.67481229])
E = -827.58633441235258
hkl_projection = array([ 0.17558573,  0.51931773, -0.93637477])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
