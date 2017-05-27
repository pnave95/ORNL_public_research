#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E162.797645063_hkl-18.4308396784,5.54711831191,-5.2290545175/sample/sampleassembly.xml'
psi = -0.007448646596585381
hkl2Q = array([[-0.65370269,  0.93923861,  0.        ],
       [ 0.66414199,  0.46223761, -0.80916512],
       [-0.66414199, -0.46223761, -0.80916512]])
pp = array([-0.84029412,  2.8799142 ,  0.06011388])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017617381966022732
Q = array([ 19.20519839, -12.32980383,  -0.25736613])
E = 162.79764506250854
hkl_projection = array([ 0.1984455 , -0.27020059, -0.15126059])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
