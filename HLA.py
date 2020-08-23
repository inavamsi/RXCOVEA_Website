import random
import matplotlib.pyplot as plt
from matplotlib import colors

def simulate(days,r,i,a1,a2,b1,b2,c1,c2,name):
	N=1000
	I1=r*i*N
	I2=(1-r)*i*N
	S1=N*r -I1-I2
	S2=N*(1-r) -I1-I2
	R1=0
	R2=0

	S=[]
	R=[]
	I=[]
	S1l=[]
	S2l=[]
	I1l=[]
	I2l=[]
	R1l=[]
	R2l=[]
	S1l.append(S1)
	S2l.append(S2)
	I1l.append(I1)
	I2l.append(I2)
	R1l.append(R1)
	R2l.append(R2)
	S.append(S1+S2)
	R.append(R1+R2)
	I.append(I1+I2)

	for i in range(days):
		dS1= a1*(c1*I1+c2*I2)*S1/N
		dS2= a2*(c1*I1+c2*I2)*S2/N
		dR1= b1*I1
		dR2= b2*I2
		S1 = S1-dS1
		S2 = S2-dS2
		R1 = R1 +dR1
		R2 = R2 +dR2
		I1 = I1 +dS1-dR1
		I2 = I2 +dS2-dR2

		S1l.append(S1)
		S2l.append(S2)
		I1l.append(I1)
		I2l.append(I2)
		R1l.append(R1)
		R2l.append(R2)
		S.append(S1+S2)
		R.append(R1+R2)
		I.append(I1+I2)

	#plot(S,I,R,name,N)
	plot2(S1l,S2l,I1l,I2l,R1l,R2l,name,N)



def plot(S,I,R,name,N): 
	plt.ylim(-N/20,N)
	plt.plot(S)
	plt.plot(I)
	plt.plot(R)
	#plt.plot(total_list)
	plt.title(name)
	plt.legend(['Susceptible','Infected','Recovered'],loc='upper right', shadow=True)
	plt.show()

def plot2(S1,S2,I1,I2,R1,R2,name,N): 
	plt.ylim(-N/20,N)
	plt.plot(S1)
	plt.plot(I1)
	plt.plot(R1)
	plt.plot(S2)
	plt.plot(I2)
	plt.plot(R2)
	plt.title(name)
	plt.legend(['HLA-A Susceptible','HLA-A Infected','HLA-A Recovered','HLA-B Susceptible','HLA-B Infected','HLA-B Recovered'],loc='upper right', shadow=True)
	plt.show()


def main():
	days=100
	ratio_A_to_B=0.3
	starting_infected =0.01
	susceptibility_A=0.4
	susceptibility_B=0.3
	recovery_A=0.1
	recovery_B=0.1
	infectivity_A=1
	infectivity_B=0.8

	simulate(days,ratio_A_to_B,starting_infected,susceptibility_A,susceptibility_B,recovery_A,recovery_B,infectivity_A,infectivity_B,'Heterogenous population with two HLA types')


	#simulate(0.5,0.01,a,a,b,b,'Homogenous population')
	#simulate(0.7,0.01,a-da,a+da,b+db,b-db,'Heterogenous population with two HLA types')

main()
