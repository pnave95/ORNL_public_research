#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-22.1318541761_hkl-2.76263894169,-0.56548800976,1.59106483064/sample/sampleassembly.xml'
psi = -0.000412700147261978
hkl2Q = array([[-0.66029489,  0.93461598,  0.        ],
       [ 0.6608733 ,  0.466899  , -0.80916512],
       [-0.6608733 , -0.466899  , -0.80916512]])
pp = array([ 2.06965218,  2.17175962,  0.50217592])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0066492516904170101
Q = array([ 0.39894819, -3.58889885, -0.82986099])
E = -22.131854176149144
hkl_projection = array([ 0.96399566,  0.03999165,  0.56827999])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
