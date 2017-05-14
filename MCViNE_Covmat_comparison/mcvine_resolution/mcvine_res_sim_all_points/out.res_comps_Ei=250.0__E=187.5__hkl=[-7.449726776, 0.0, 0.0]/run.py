#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[2 0 0]/out.res_comps_tmp28/sample/sampleassembly.xml'
psi = 0.4359238525493491
hkl2Q = array([[ -9.93418590e-01,   5.67992849e-01,   7.31732342e-17],
       [  4.01631595e-01,   7.02453022e-01,  -8.09165116e-01],
       [ -4.01631595e-01,  -7.02453022e-01,  -8.09165116e-01]])
pp = array([  1.95107402e+00,   2.27888353e+00,   2.93583412e-16])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0028232439344611452
Q = array([  7.40069707e+00,  -4.23139153e+00,  -5.45120602e-16])
E = 187.5
hkl_projection = array([2, 0, 0])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
