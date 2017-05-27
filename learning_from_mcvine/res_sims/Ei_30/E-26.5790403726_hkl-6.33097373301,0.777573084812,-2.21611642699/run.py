#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-26.5790403726_hkl-6.33097373301,0.777573084812,-2.21611642699/sample/sampleassembly.xml'
psi = -0.005027767666359206
hkl2Q = array([[-0.65597456,  0.93765332,  0.        ],
       [ 0.66302102,  0.46384406, -0.80916512],
       [-0.66302102, -0.46384406, -0.80916512]])
pp = array([-1.36270873,  2.67264381, -0.68409092])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0066215600757138886
Q = array([ 6.13783678, -4.54765345,  1.16401909])
E = -26.579040372609054
hkl_projection = array([-0.22809053,  0.31638934, -0.96090215])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
