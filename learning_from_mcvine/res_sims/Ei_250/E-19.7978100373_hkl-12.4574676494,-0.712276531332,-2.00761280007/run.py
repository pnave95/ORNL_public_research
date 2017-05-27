#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-19.7978100373_hkl-12.4574676494,-0.712276531332,-2.00761280007/sample/sampleassembly.xml'
psi = -0.002937455443559058
hkl2Q = array([[ -6.57933112e-01,   9.36280081e-01,   7.76387884e-17],
       [  6.62049995e-01,   4.65228965e-01,  -8.09165116e-01],
       [ -6.62049995e-01,  -4.65228965e-01,  -8.09165116e-01]])
pp = array([ 0.52594139,  2.95353782, -0.58767137])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023919619870633661
Q = array([  9.05375783, -11.06105087,   2.20083957])
E = -19.797810037308665
hkl_projection = array([-0.46680371,  0.69821457, -0.91360799])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
