import time 
import os

def readdir(basedir):
    fname = []
    for root,d_names,f_names in os.walk(basedir):
        for f in f_names:
            fname.append(os.path.join(root, f))
    #print("fname = %s" %fname)
    return fname 
  
#recursive version only listing folders 
def scanRecurse(basedir):
    fname = []
    for root,d_names,f_names in os.walk(basedir):
        for d in d_names:
            fname.append(os.path.join(root, d))
    return fname

fldr = 'c:\\temp'

filenames = next(os.walk(fldr))[2]
print(filenames)

fldr = 'K:\\Fortuna 4 Calculation Agent ILS 2019 onwards\\Working Files\\csvFiles\\swissLotto' #0.02s 85files
fldr = 'K:\\Fortuna 4 Calculation Agent ILS 2019 onwards\\Working Files\\csvFiles\\german6aus49'

fldr99 = 'K:\\Fortuna 4 Calculation Agent ILS 2019 onwards\\Working Files\\csvFiles\\german6aus49\\2023\\8'
li = os.listdir(fldr99)
#print(li)

print(scanRecurse(fldr))


subfolders = [ f.path for f in os.scandir(fldr) if f.is_dir() ]
print(subfolders)

#fldr = '\\\\mill-zur-fs2\\Lottoland\\Fortuna 4 Calculation Agent ILS 2019 onwards\\Working Files\\csvFiles\\swissLotto'
#fldr = '\\network_drive\$k\Fortuna 4 Calculation Agent ILS 2019 onwards\Working Files\csvFiles\swissLotto'
#print(os.listdir(fldr))

t = time.time()
itr = readdir(fldr) #scanRecurse(fldr)
elapsed = time.time() - t
print(f'elapsed: {elapsed}')

t = time.time()
out_list = [n for n in itr]
elapsed2 = time.time() - t
print(f'elapsed2: {elapsed2}')

#print length 
print(len(out_list))
#print(out_list)
