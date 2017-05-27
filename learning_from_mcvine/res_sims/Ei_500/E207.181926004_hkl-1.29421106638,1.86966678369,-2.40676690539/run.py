#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E207.181926004_hkl-1.29421106638,1.86966678369,-2.40676690539/sample/sampleassembly.xml'
psi = 0.02105105679893054
hkl2Q = array([[-0.68020163,  0.92022938,  0.        ],
       [ 0.65070044,  0.48097519, -0.80916512],
       [-0.65070044, -0.48097519, -0.80916512]])
pp = array([ 2.99214836, -0.21690601, -0.10886858])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017886241677692546
Q = array([ 3.66300174,  0.86588744,  0.43460268])
E = 207.18192600433815
hkl_projection = array([ 0.10017192, -0.08419275, -0.76669018])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
