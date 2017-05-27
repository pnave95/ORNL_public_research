#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-99.1089493921_hkl-21.9222274107,4.49232865856,-4.48783007507/sample/sampleassembly.xml'
psi = -0.005909452033038125
hkl2Q = array([[-0.65514759,  0.93823132,  0.        ],
       [ 0.66342973,  0.4632593 , -0.80916512],
       [-0.66342973, -0.4632593 , -0.80916512]])
pp = array([ -8.28121321e-01,   2.88343807e+00,   6.39688426e-04])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016698743305317929
Q = array([  2.03199987e+01,  -1.64079783e+01,  -3.64009684e-03])
E = -99.108949392126419
hkl_projection = array([ 0.56943073,  0.44332774, -0.21988783])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
