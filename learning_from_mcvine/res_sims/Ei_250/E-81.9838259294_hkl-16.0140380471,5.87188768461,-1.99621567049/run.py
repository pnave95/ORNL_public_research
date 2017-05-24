#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-81.9838259294_hkl-16.0140380471,5.87188768461,-1.99621567049/sample/sampleassembly.xml'
psi = -0.0049756255133141985
hkl2Q = array([[-0.65602345,  0.93761912,  0.        ],
       [ 0.66299683,  0.46387863, -0.80916512],
       [-0.66299683, -0.46387863, -0.80916512]])
pp = array([-1.14618963,  2.77240858,  0.76500352])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023552994142316723
Q = array([ 15.72211209, -11.36522319,  -3.1360586 ])
E = -81.983825929436904
hkl_projection = array([-0.13407221,  0.2296061 ,  0.50526748])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
