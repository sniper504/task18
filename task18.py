input_data=open("input.txt","r")
data =input_data.read()
output_data=open("output.txt","a")
data=data.split()
n=int(data[0])
f=int(data[1])
for i in range(0,1000):
    f=f*i
output_data.write(str(f))
input_data.close()
output_data.close()