from yafdc.yafdc_start import importUsrInit, yafdcInit, yafdcLaunch   

from simple.simple_init import simpleInit

prj_name = "simple"
N_proc = 2

usr_init_hnd = importUsrInit(prj_name)

yafdcInit(N_proc, usr_init_hnd) 
yafdcLaunch(prj_name, N_proc)


