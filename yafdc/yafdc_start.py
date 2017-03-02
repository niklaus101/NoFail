import redis

def importUsrInit(prj_name):
	#import user init function
	my_module = __import__(prj_name + "_init")
	usr_init_hndlr = getattr(my_module, prj_name + "Init")
    
	return usr_init_hndlr

def yafdcInit(N = 1, usr_init):
    print("-= YAFDC ver 0 =-")
	rs = redis.StrictRedis(host="127.0.0.1", port=6379, db=0)
	
	#yafdc initialization
	rs.set("N", N)
	
	for i in range(N):
		rs.lpush("count_res", 0)
	    rs.set("sem"+str(i), 1)
		
	#user initialization
	usr_init(rs)

def yafdcLaunch(prj_name, N = 1):
    print("-= YAFDC ver 0 =-")
	
	print("Distributing code...")
    #сваливаем рабочий код пользователя и рамочный код в одну папку
	os.system("mkdir yafdc_tmp")
	os.system("cp /yafdc/yafdc_job.py yafdc_tmp") 
	os.system("cp " +  prj_name +"/" + prj_name + "_job  yafdc_tmp")
    #раскидываем по узлам
	os.system("parallel rsync /yafdc_tmp")
	#запускаем
	os.system("python /yafdc_tmp/yafdc_job.py")
	print("Done")


