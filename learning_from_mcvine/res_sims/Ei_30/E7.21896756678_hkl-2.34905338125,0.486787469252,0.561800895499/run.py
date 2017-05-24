#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E7.21896756678_hkl-2.34905338125,0.486787469252,0.561800895499/sample/sampleassembly.xml'
psi = -0.002490044050091817
hkl2Q = array([[-0.65835195,  0.93598562,  0.        ],
       [ 0.66184178,  0.46552513, -0.80916512],
       [-0.66184178, -0.46552513, -0.80916512]])
pp = array([ 2.1621904 ,  2.07964724,  0.78999856])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0071669294721665722
Q = array([ 1.49685685, -2.23360082, -0.84848113])
E = 7.2189675667752766
hkl_projection = array([-0.88544239,  0.95032654, -0.92886178])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
