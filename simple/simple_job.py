def simpleAggreg(rs):
	N=int(rs.get("N"))
       
        print("N = " + str(N))
 
	sum = 0
	for i in range(N):
                key_i = "spec_key"+str(i+1)
		sum += float(rs.get(key_i))
        sum /= N

	rs.set("result", sum)


def simpleJob(rs, np):
	rs.set("spec_key"+str(np),np+1)
