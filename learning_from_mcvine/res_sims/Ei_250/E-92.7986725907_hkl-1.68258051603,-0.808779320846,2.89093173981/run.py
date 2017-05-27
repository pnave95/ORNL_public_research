#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-92.7986725907_hkl-1.68258051603,-0.808779320846,2.89093173981/sample/sampleassembly.xml'
psi = 0.001441717995923811
hkl2Q = array([[ -6.62026924e-01,   9.33389910e-01,   7.78791910e-17],
       [  6.60006335e-01,   4.68123727e-01,  -8.09165116e-01],
       [ -6.60006335e-01,  -4.68123727e-01,  -8.09165116e-01]])
pp = array([ 2.89819382,  0.77490165,  0.39533306])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023405417880699715
Q = array([-1.32791913, -3.30242621, -1.6848051 ])
E = -92.798672590687801
hkl_projection = array([-0.15948986,  0.70432856, -0.16324156])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
