#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-425.061476376_hkl-7.16331321655,-4.33437108225,6.03053441798/sample/sampleassembly.xml'
psi = 0.0008676061577062296
hkl2Q = array([[-0.66149094,  0.93376983,  0.        ],
       [ 0.66027498,  0.46774473, -0.80916512],
       [-0.66027498, -0.46774473, -0.80916512]])
pp = array([ 2.51379564,  1.63732449,  0.19478078])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016161680221828561
Q = array([ -2.10522096, -11.53701574,  -1.3724762 ])
E = -425.061476376408
hkl_projection = array([-0.42257556,  0.48868514, -0.8454239 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
