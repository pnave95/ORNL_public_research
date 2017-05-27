#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-39.8305665713_hkl-6.46652274494,-1.26640807906,-0.09465887277/sample/sampleassembly.xml'
psi = -0.00252384170689524
hkl2Q = array([[ -6.58320314e-01,   9.36007871e-01,  -7.76613673e-17],
       [  6.61857513e-01,   4.65502759e-01,  -8.09165116e-01],
       [ -6.61857513e-01,  -4.65502759e-01,  -8.09165116e-01]])
pp = array([ 0.84032387,  2.87990552, -0.48069706])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047141008689020065
Q = array([ 3.48151227, -6.59816868,  1.1013279 ])
E = -39.830566571261343
hkl_projection = array([-0.07212789,  0.65128521, -0.90707535])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
