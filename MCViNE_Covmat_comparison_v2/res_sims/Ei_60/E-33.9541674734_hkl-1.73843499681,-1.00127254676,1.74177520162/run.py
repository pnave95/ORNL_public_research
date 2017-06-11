#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison_v2/res_sims/Ei_60/E-33.9541674734_hkl-1.73843499681,-1.00127254676,1.74177520162/sample/sampleassembly.xml'
psi = 0.0010865059843753568
hkl2Q = array([[-0.66169533,  0.93362501,  0.        ],
       [ 0.66017258,  0.46788926, -0.80916512],
       [-0.66017258, -0.46788926, -0.80916512]])
pp = array([ 2.70558444,  1.29607593,  0.26719329])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047291170506751105
Q = array([-0.66057058, -2.90648896, -0.59918892])
E = -33.954167473416923
hkl_projection = array([-0.52577502, -0.32814417,  0.92651518])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
