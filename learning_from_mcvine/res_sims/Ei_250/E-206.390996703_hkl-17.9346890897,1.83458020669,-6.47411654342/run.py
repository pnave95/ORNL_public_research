#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-206.390996703_hkl-17.9346890897,1.83458020669,-6.47411654342/sample/sampleassembly.xml'
psi = -0.004794119109897072
hkl2Q = array([[-0.65619362,  0.93750003,  0.        ],
       [ 0.66291263,  0.46399896, -0.80916512],
       [-0.66291263, -0.46399896, -0.80916512]])
pp = array([-1.30379093,  2.70187513, -0.78274584])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0022990172789353696
Q = array([ 17.27656859, -12.95854486,   3.75415096])
E = -206.3909967026934
hkl_projection = array([-0.95900978,  0.41590479, -0.8369992 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
