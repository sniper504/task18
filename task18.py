input_data=open("input.txt","r")#def factorial(n):   if(n==0):   return 1     else: return n*factorial(n-1)
data =input_data.read()
data=data.split()
n=int(data[0])#
for f in range(1,n+1):
        if(f==0):
                n=1
else:
        n=f*(f-1)
        output_data=open("output.txt","w")
        output_data.write(str(n))
input_data.close()
output_data.close()