#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E18.9573303003_hkl-4.86815025034,-1.30514852852,0.60747406222/sample/sampleassembly.xml'
psi = -0.0012812279724517706
hkl2Q = array([[-0.6594829 ,  0.93518911,  0.        ],
       [ 0.66127856,  0.46632483, -0.80916512],
       [-0.66127856, -0.46632483, -0.80916512]])
pp = array([ 2.57274065,  1.54305073, -0.15999582])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0024179947930154898
Q = array([ 1.94568554, -5.44454451,  0.56453384])
E = 18.957330300266278
hkl_projection = array([ 0.49018326, -0.66230303,  0.1603806 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
