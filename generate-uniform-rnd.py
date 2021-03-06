#this python program generates a uniform and logarithmic distribution of random points

import random
import math

def rndln(a,b):
	x=random.uniform(0,1)
	n=a* 10**(x * math.log10(b/a) )
	return(n)


# Enter ranges of the parameters and call subroutine rndom

m0min=0
m0max=1000

mhfmin=0
mhfmax=1000

a0min=-3
a0max=3

tbmin=2
tbmax=60

f1=open('./uniform-rnd.txt', 'w+')

for i in range(0, 10000):
	
	#uniform distribution
	m0=random.uniform(m0min,m0max)     #m0
	mhf=random.uniform(mhfmin,mhfmax)  #mhf
	a0=random.uniform(a0min,a0max)     #a0
	tb=random.uniform(tbmin,tbmax)     #tanb
	
	f1.write('%4.2e \t %4.2e \t %4.2e \t %4.2e\n' % (m0,mhf,a0,tb))
	
	#log distribution

	m0=rndln(m0min+1,m0max)     #m0
	mhf=rndln(mhfmin+1,mhfmax)  #mhf
	tb=rndln(tbmin+1,tbmax)     #tanb

	t1=rndln(0.01,a0max)        #a0
	if (i%2==1): a0=t1
	else: a0=-t1
	print a0

	f1.write('%4.2e \t %4.2e \t %4.2e \t %4.2e\n' % (m0,mhf,a0,tb))



