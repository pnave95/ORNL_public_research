#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-305.216282377_hkl-18.5189053588,0.748774683689,3.66957537083/sample/sampleassembly.xml'
psi = -0.002610287036224369
hkl2Q = array([[ -6.58239399e-01,   9.36064776e-01,   7.76566461e-17],
       [  6.61897751e-01,   4.65445542e-01,  -8.09165116e-01],
       [ -6.61897751e-01,  -4.65445542e-01,  -8.09165116e-01]])
pp = array([ 0.82555961,  2.88417256,  0.55157898])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016358005176797311
Q = array([ 10.25660172, -18.69436866,  -3.57517474])
E = -305.21628237707364
hkl_projection = array([-0.7393149 , -0.58519687, -0.05615094])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
