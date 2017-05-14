#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[1 0 0]/out.res_comps_tmp26/sample/sampleassembly.xml'
psi = 0.16235078886310667
hkl2Q = array([[ -8.03018514e-01,   8.15265379e-01,  -8.91631768e-17],
       [  5.76479678e-01,   5.67819836e-01,  -8.09165116e-01],
       [ -5.76479678e-01,  -5.67819836e-01,  -8.09165116e-01]])
pp = array([  6.94013005e-02,   2.99919714e+00,  -3.28013370e-16])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0024034964283887665
Q = array([  1.07703902e+01,  -1.09346498e+01,   1.19589049e-15])
E = 3.90625
hkl_projection = array([1, 0, 0])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
