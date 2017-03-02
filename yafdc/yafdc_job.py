import sys, redis
	
def getUsrJob(prj_name):
	#import user job function
	my_module = __import__(prj_name + "_job")
	usr_job_hndlr = getattr(my_module, prj_name + "Job")
    
	return usr_job_hndlr
	
def getUsrAggr(prj_name):
	#import user aggreg function
	my_module = __import__(prj_name + "_job")
	usr_agr_hndlr = getattr(my_module, prj_name + "Aggreg")

    return usr_agr_hndlr

rs=redis.StrictRedis(host='192.168.1.101', port=6379, db = 0)

np = int(sys.argv[1])
prj_name = sys.argv[2]

usr_job_hndlr = getUsrJob(prj_name)
usr_aggr_hndlr = getUsrAggr(prj_name)

#do the job    
usr_job_hndlr(rs, np)
usr_aggr_hndlr(rs)