input_data=open("input.txt","r")#data=data.split()n=int(data[0])
data =input_data.read()
output_data=open("output.txt","a")
def factorial(n):
        if(n==0):
                return 1
        else: return n*factorial(n-1)
        output_data.write(str(n))
input_data.close()
output_data.close()