#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E42.6645581609_hkl-1.84651347822,0.760673112196,-1.36746816197/sample/sampleassembly.xml'
psi = -0.01659412194528242
hkl2Q = array([[-0.64508569,  0.94517767,  0.        ],
       [ 0.66834154,  0.45614447, -0.80916512],
       [-0.66834154, -0.45614447, -0.80916512]])
pp = array([ 2.89091983,  0.80161245, -0.50815694])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0056646363884894245
Q = array([ 2.61348464, -0.77454343,  0.49099739])
E = 42.664558160869007
hkl_projection = array([-0.00498321,  0.89181602,  0.37031432])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
