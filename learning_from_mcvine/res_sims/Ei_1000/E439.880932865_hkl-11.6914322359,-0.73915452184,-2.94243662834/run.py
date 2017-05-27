#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E439.880932865_hkl-11.6914322359,-0.73915452184,-2.94243662834/sample/sampleassembly.xml'
psi = -0.005024549122626062
hkl2Q = array([[ -6.55977577e-01,   9.37651209e-01,   7.75252571e-17],
       [  6.63019528e-01,   4.63846193e-01,  -8.09165116e-01],
       [ -6.63019528e-01,  -4.63846193e-01,  -8.09165116e-01]])
pp = array([ 2.38027386,  1.82600557, -0.54722573])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012747082482448401
Q = array([ 9.13013645, -9.94050156,  2.97901513])
E = 439.88093286485969
hkl_projection = array([ 0.31279925, -0.74858159,  0.22176553])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
