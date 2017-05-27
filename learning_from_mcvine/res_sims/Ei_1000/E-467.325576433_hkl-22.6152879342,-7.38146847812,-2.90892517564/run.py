#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-467.325576433_hkl-22.6152879342,-7.38146847812,-2.90892517564/sample/sampleassembly.xml'
psi = -0.0028001434361645235
hkl2Q = array([[-0.65806167,  0.93618973,  0.        ],
       [ 0.66198611,  0.46531987, -0.80916512],
       [-0.66198611, -0.46531987, -0.80916512]])
pp = array([ 1.20177708,  2.74876915, -0.98428672])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011707029997473431
Q = array([ 11.92149259, -23.25336358,   8.32662758])
E = -467.32557643295212
hkl_projection = array([ 0.44238952, -0.42165998,  0.99677071])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
