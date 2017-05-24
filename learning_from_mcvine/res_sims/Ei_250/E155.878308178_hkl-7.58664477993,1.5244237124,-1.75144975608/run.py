#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E155.878308178_hkl-7.58664477993,1.5244237124,-1.75144975608/sample/sampleassembly.xml'
psi = -0.004598000098442171
hkl2Q = array([[-0.65637747,  0.93737132,  0.        ],
       [ 0.66282162,  0.46412896, -0.80916512],
       [-0.66282162, -0.46412896, -0.80916512]])
pp = array([ 1.70812208,  2.46623579, -0.08103116])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0026684466314514273
Q = array([ 7.15102246, -5.59107546,  0.18370156])
E = 155.87830817757703
hkl_projection = array([ 0.7750029 ,  0.51051609, -0.24999532])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
