#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-394.702129653_hkl-19.8377556367,-3.32130623294,-0.0139141279385/sample/sampleassembly.xml'
psi = -0.0025717138627946883
hkl2Q = array([[ -6.58275505e-01,   9.36039385e-01,   7.76587527e-17],
       [  6.61879797e-01,   4.65471073e-01,  -8.09165116e-01],
       [ -6.61879797e-01,  -4.65471073e-01,  -8.09165116e-01]])
pp = array([ 0.68803088,  2.92003656, -0.39189716])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016214019735395363
Q = array([ 10.8696126 , -20.10841595,   2.69874397])
E = -394.70212965274038
hkl_projection = array([-0.77597036, -0.37896169, -0.83285847])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
