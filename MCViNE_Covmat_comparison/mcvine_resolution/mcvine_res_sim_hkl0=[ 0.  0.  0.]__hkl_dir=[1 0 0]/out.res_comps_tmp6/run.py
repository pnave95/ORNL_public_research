#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[1 0 0]/out.res_comps_tmp6/sample/sampleassembly.xml'
psi = 0.25257407709666324
hkl2Q = array([[ -8.73208518e-01,   7.39596685e-01,  -8.32466125e-17],
       [  5.22973831e-01,   6.17451664e-01,  -8.09165116e-01],
       [ -5.22973831e-01,  -6.17451664e-01,  -8.09165116e-01]])
pp = array([ -4.83886689e-01,   2.96071844e+00,  -3.33248899e-16])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0069406235462329104
Q = array([  4.43272397e+00,  -3.75446172e+00,   4.22590077e-16])
E = 0.234375
hkl_projection = array([1, 0, 0])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
