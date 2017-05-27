#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E101.272012359_hkl-11.625982052,4.59007167173,-1.43222717312/sample/sampleassembly.xml'
psi = -0.005154493526947787
hkl2Q = array([[-0.65585573,  0.93773644,  0.        ],
       [ 0.6630798 ,  0.46376003, -0.80916512],
       [-0.6630798 , -0.46376003, -0.80916512]])
pp = array([-0.21946182,  2.99196198,  0.94276978])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0025538643417011113
Q = array([ 11.61823163,  -8.10920553,  -2.55521761])
E = 101.27201235918432
hkl_projection = array([-0.16518   , -0.25289161,  0.19588953])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
