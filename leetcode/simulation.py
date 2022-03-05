import time
start_time = time.time()
##################################################
a = '11'
b = '1'
inta = int(a, 2)
intb = int(b, 2)
print(str(bin(inta + intb))[2:])
##################################################
end_time = time.time()
print('time: ', end_time - start_time)