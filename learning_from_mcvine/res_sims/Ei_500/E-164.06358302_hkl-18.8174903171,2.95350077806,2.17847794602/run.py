#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-164.06358302_hkl-18.8174903171,2.95350077806,2.17847794602/sample/sampleassembly.xml'
psi = -0.0035521877374844997
hkl2Q = array([[-0.65735743,  0.93668436,  0.        ],
       [ 0.66233586,  0.46482189, -0.80916512],
       [-0.66233586, -0.46482189, -0.80916512]])
pp = array([ 0.46760601,  2.96333336,  0.71271479])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016633566440151172
Q = array([ 12.88314242, -17.26580124,  -4.15261816])
E = -164.06358302021943
hkl_projection = array([-0.98853247, -0.72507965,  0.74194408])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
