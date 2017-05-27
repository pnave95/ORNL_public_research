#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-228.357396686_hkl-23.9547160746,6.19195124067,-5.39862581451/sample/sampleassembly.xml'
psi = -0.006519841023869114
hkl2Q = array([[-0.65457478,  0.93863104,  0.        ],
       [ 0.66371237,  0.46285427, -0.80916512],
       [-0.66371237, -0.46285427, -0.80916512]])
pp = array([-1.23923332,  2.73208726,  0.10244295])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016442266172725596
Q = array([ 23.37296244, -17.11989198,  -0.64193126])
E = -228.35739668611751
hkl_projection = array([-0.29890886, -0.45502299,  0.19550689])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
