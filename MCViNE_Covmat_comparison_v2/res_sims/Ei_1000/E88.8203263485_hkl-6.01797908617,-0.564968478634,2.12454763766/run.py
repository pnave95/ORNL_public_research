#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison_v2/res_sims/Ei_1000/E88.8203263485_hkl-6.01797908617,-0.564968478634,2.12454763766/sample/sampleassembly.xml'
psi = -0.0017347160543883947
hkl2Q = array([[-0.65905874,  0.93548808,  0.        ],
       [ 0.66148997,  0.4660249 , -0.80916512],
       [-0.66148997, -0.4660249 , -0.80916512]])
pp = array([ 2.83520634,  0.9806146 ,  0.17978647])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012092290868794377
Q = array([ 2.18711377, -6.8831292 , -1.26195705])
E = 88.820326348466551
hkl_projection = array([ 0.75437165,  0.37768877,  0.5420931 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
