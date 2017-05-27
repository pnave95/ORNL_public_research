#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-53.4909027727_hkl-7.04852831429,-2.91656434211,1.52834054743/sample/sampleassembly.xml'
psi = -0.0009395527623266677
hkl2Q = array([[-0.65980239,  0.93496373,  0.        ],
       [ 0.66111919,  0.46655075, -0.80916512],
       [-0.66111919, -0.46655075, -0.80916512]])
pp = array([ 2.54571163,  1.58724677, -0.2057918 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016817363840208911
Q = array([ 1.71202393, -8.663892  ,  1.12330227])
E = -53.490902772727168
hkl_projection = array([ 0.30696872,  0.98661403, -0.58657737])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
