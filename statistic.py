import psutil
psutil.PROCFS_PATH='/proc_h'
cpu=psutil.cpu_times()
mem = psutil.virtual_memory()
swmem = psutil.swap_memory()
sum = 0
for i in range(0, len(cpu)):
    sum = sum + cpu[i]
print ('idle =', round (cpu[3] * 100 / sum, 1))
print ('user =', round (cpu[0] * 100 / sum, 1))
print ('guest =', round (cpu[8] * 100 / sum, 1))
print ('iowait =', round (cpu[4] * 100 / sum, 1))
print ('stolen =', round (cpu[7] * 100 / sum, 1))
print ('system =', round (cpu[2] * 100 / sum, 1))
print ('virtual total', mem[0] )
print ('virtual used', mem[3] )
print ('virtual free', mem[4] )
print ('swap total', swmem[0] )
print ('swap used', swmem[1] )
print ('swap free', swmem[2] )
