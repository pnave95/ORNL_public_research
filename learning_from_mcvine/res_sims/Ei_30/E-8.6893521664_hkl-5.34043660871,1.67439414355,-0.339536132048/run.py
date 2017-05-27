#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-8.6893521664_hkl-5.34043660871,1.67439414355,-0.339536132048/sample/sampleassembly.xml'
psi = -0.004426940923743448
hkl2Q = array([[-0.65653781,  0.93725902,  0.        ],
       [ 0.66274221,  0.46424234, -0.80916512],
       [-0.66274221, -0.46424234, -0.80916512]])
pp = array([-0.73043131,  2.90971993,  0.77211878])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0068235030008214539
Q = array([ 4.84091515, -4.07042071, -1.08012054])
E = -8.689352166399928
hkl_projection = array([-0.14228128, -0.50181681, -0.05408478])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
