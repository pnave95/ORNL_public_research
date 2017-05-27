#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-0.725903511955_hkl-9.79119416396,0.729776902488,-2.62294931757/sample/sampleassembly.xml'
psi = -0.005494131685537066
hkl2Q = array([[ -6.55537200e-01,   9.37959142e-01,   7.74998056e-17],
       [  6.63237269e-01,   4.63534799e-01,  -8.09165116e-01],
       [ -6.63237269e-01,  -4.63534799e-01,  -8.09165116e-01]])
pp = array([-0.32741744,  2.98207945, -0.59874621])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0034045362303547233
Q = array([ 8.64214499, -7.6296348 ,  1.53188908])
E = -0.72590351195515268
hkl_projection = array([ 0.78583822, -0.69389277, -0.7541709 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
