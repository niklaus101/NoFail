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

N_proc = int(rs.get("N"))

np = int(sys.argv[1])
prj_name = sys.argv[2]

maxstep = 100

usr_job_hndlr = getUsrJob(prj_name)
usr_aggr_hndlr = getUsrAggr(prj_name)

#do my job
usr_job_hndlr(rs, np)
rs.lset("count_res", np, 1)

#scan count_res
for step in range(maxstep):
	all_jobs_done = 1
		
	for ii in range(N_proc):
				
		if int(rs.lindex("count_res", ii)) < 1:
			all_jobs_done = 0	
				
			#check if timer for this job is set
			not_in_work = 0
			timer_name = 'timer'+str(ii)
			if(rs.exists(timer_name)):
				not_in_work = 1
				break
				
			if not_in_work: 
				if(rs.delete('lock_key')):
					timer_name = 'timer'+str(i)
					rs.set(timer_name, "x")
					rs.expire(timer_name, COUNT_TIME)
					rs.lset("my_job", np, ii)		
					rs.set('lock_key', "x")
					#do someone's job
					usr_job_hndlr(rs, ii)
					rs.lset("count_res", ii, 1)
			
		if(all_jobs_done):
			jobs_done_flag = 1
			break

	if jobs_done_flag:
		break
			
print("All jobs done")

#aggregate results    
usr_aggr_hndlr(rs)