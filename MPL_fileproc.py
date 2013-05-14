import pandas as pan
import numpy as np
import os,sys
import MPLtools as mtools
import image_process_tools as imtools

#----------------------------------------------------------------------------
#Uses tools created in LNC_tools to open all files in a folder and resample
#them to a regular spacing in altitude/date the concatenates them into one
#pandas dataframe and plots it using LNC_plot
#July 05, 2012
#----------------------------------------------------------------------------

olddir = os.getcwd()

os.chdir('C:\Program Files (x86)\SigmaMPL\DATA')

newdir = mtools.set_dir('Select Event Folder')

os.chdir(newdir)

files = os.listdir(newdir)
rawfiles = []

#set altitude range and date step sizes

altrange = np.arange(150,10010,10)#meters
timestep = '120S' #seconds

#check to see if each file has been processed before and separate processed
#files into a new list

for f in files:
    if '.mpl' in f:
        rawfiles.append(f)

#open, altitude resample, and concatenate data and mask files


for r in rawfiles:
    MPLdat_temp = mtools.MPL()
    MPLdat_temp.fromfile(r)
    MPLdat_realt = mtools.alt_resample(MPLdat_temp,altrange)

    try:
        MPLdat_event.append(MPLdat_realt)
    except NameError:
        MPLdat_event = MPLdat_realt
   
#sort by index to make certain data is in order then set date ranges to match
for n in range(MPLdat_event.header.numchans):
    data = MPLdat_event.data[n]
    data = data.sort_index()

start = data.index[0]
end = data.index[-1]

MPLdat_event= mtools.time_resample(MPLdat_event,timestep, timerange = [start,end])

#d_filename = rawfiles[0].split('.')[0]+'-'+rawfiles[-1].split('.')[0]+'_raw'
#MPLdat_event.save(d_filename+'.pickle')

MPLdat_event = mtools.background_subtract(MPLdat_event)

MPLdat_event = mtools.range_cor(MPLdat_event)

#d_filename = rawfiles[0].split('.')[0]+'-'+rawfiles[-1].split('.')[0]+'_proc'
#MPLdat_event.save(d_filename+'.pickle')
for n in range(MPLdat_event.header.numchans):
    MPLdat_event.data[n] = imtools.blur_image(MPLdat_event.data[n],[12,24])

mtools.quicklook(MPLdat_event, (0,2e7))




