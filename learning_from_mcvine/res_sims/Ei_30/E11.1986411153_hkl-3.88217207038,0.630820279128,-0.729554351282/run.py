#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E11.1986411153_hkl-3.88217207038,0.630820279128,-0.729554351282/sample/sampleassembly.xml'
psi = -0.004271661467421664
hkl2Q = array([[ -6.56683337e-01,   9.37157066e-01,  -7.75661346e-17],
       [  6.62670117e-01,   4.64345240e-01,  -8.09165116e-01],
       [ -6.62670117e-01,  -4.64345240e-01,  -8.09165116e-01]])
pp = array([ 0.36474904,  2.9777438 , -0.07912746])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0072611994268037333
Q = array([ 3.45083732, -3.0065215 ,  0.07989217])
E = 11.198641115309144
hkl_projection = array([ 0.87529479,  0.54850954, -0.72358108])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
