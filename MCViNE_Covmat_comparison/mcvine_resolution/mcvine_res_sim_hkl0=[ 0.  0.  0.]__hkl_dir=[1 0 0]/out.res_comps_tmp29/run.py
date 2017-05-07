#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[1 0 0]/out.res_comps_tmp29/sample/sampleassembly.xml'
psi = 0.16682512119547396
hkl2Q = array([[ -8.06658232e-01,   8.11664259e-01,  -8.95587681e-17],
       [  5.73933301e-01,   5.70393506e-01,  -8.09165116e-01],
       [ -5.73933301e-01,  -5.70393506e-01,  -8.09165116e-01]])
pp = array([  2.24451689e+00,   1.99051348e+00,  -2.19632605e-16])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0018204773392102571
Q = array([  7.31172321e+00,  -7.35709891e+00,   8.11779881e-16])
E = 250.0
hkl_projection = array([1, 0, 0])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
