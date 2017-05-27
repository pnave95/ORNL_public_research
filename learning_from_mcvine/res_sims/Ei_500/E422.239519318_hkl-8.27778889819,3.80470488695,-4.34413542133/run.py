#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E422.239519318_hkl-8.27778889819,3.80470488695,-4.34413542133/sample/sampleassembly.xml'
psi = -0.012847841479898696
hkl2Q = array([[-0.64862206,  0.94275437,  0.        ],
       [ 0.66662801,  0.45864506, -0.80916512],
       [-0.66662801, -0.45864506, -0.80916512]])
pp = array([ 2.29023408,  1.93773783, -0.20799233])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0021475880079079904
Q = array([ 10.80140164,  -4.06649632,   0.43648837])
E = 422.23951931759643
hkl_projection = array([ 0.79293318, -0.82854068,  0.17664773])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
