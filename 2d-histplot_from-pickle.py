# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 13:10:30 2013

@author: dashamstyr
"""

import site
site.addsitedir('/Users/phil/repos/MPLcode')
site.addsitedir('/Users/phil/lib/python')
import MPLtools as mtools
import os
import numpy as np
import pandas as pan
import matplotlib.pyplot as plt
import pickle
#from plot_fields import loadvars

## import fasthist as fh
## from binit import fastbin

from matplotlib.colors import Normalize
from matplotlib import cm

#os.chdir('C:\Program Files (x86)\SigmaMPL\DATA')
#
#filepath = mtools.get_files('Select MPL file', filetype = ('.h5', '*.h5'))
#
#MPLfile = mtools.MPL()
#
#MPLfile.fromHDF(filepath[0])
#
#altrange = np.arange(150,4000,10)
#
#MPLfile.alt_resample(altrange)

#copol = MPLfile.data[0]
#crosspol = MPLfile.data[1]

MPLdat = pickle.load(open('201304222100-201304222300_proc.pickle','rb'))

copol = MPLdat[0]
crosspol = MPLdat[1]

copolvals = np.hstack(copol.values).astype('float32')
crosspolvals = np.hstack(crosspol.values).astype('float32')

depolMPL = crosspolvals/copolvals

depolvals = depolMPL/(depolMPL+1)

copol_mean = np.mean(copolvals)
copol_std = np.std(copolvals)

copol_min = copol_mean-copol_std
copol_max = copol_mean+copol_std

fignum=1
fig=plt.figure(fignum)
fig.clf()
the_axis=fig.add_subplot(111)
the_axis.plot(depolvals,copolvals,'b+')
the_axis.set_xlabel('depolvals')
the_axis.set_ylabel('copolvals')
the_axis.set_title('raw scatterplot')
fig.savefig('plot1.png')
fig.canvas.draw()
plt.show()

import hist2d as h2d
depolhist=h2d.fullhist(depolvals,20,0.24,0.42,-9999.,8888.)
copolhist=h2d.fullhist(copolvals,20,0.,1.6e-3,-9999.,8888.)


## bin_copol=fastbin(0.,0.002,100.,-999,-888)
## bin_depol=fastbin(0.,0.5,100.,-999,-888)

## copol_centers=bin_copol.get_centers()
## depol_centers=bin_depol.get_centers()
## the_hist=fh.pyhist(depolvals,copolvals,bin_depol,bin_copol)

## counts=the_hist.get_hist2d()

## cmap=cm.RdBu_r
## cmap.set_over('y')
## cmap.set_under('k')
## counts=counts.astype(np.float32)
## vmin= 0.
## vmax= 4
## the_norm=Normalize(vmin=vmin,vmax=vmax,clip=False)
## hit= (counts <= 0)
## counts[hit] = 1.e-3
## log_counts=np.log10(counts)

## olddir = os.getcwd()

## try:
##     os.chdir('Plots')
## except WindowsError:
##     os.makedirs('Plots')
##     os.chdir('Plots')

## fig1=plt.figure(1)
## fig1.clf()
## axis1=fig1.add_subplot(111)
## im=axis1.pcolormesh(depol_centers,copol_centers,log_counts,cmap=cmap,norm=the_norm)
## cb=fig1.colorbar(im,extend='both')
## the_label=cb.ax.set_ylabel('histogram counts',rotation=270)
## #axis1.set_title('{} histogram'.format(granule_info))
## axis1.set_ylabel('Attenuated Backscatter')
## axis1.set_xlabel('Depol ratio')
## #fig1.savefig('{0:s}/{1:s}_hist2d.png'.format(dirname,granule_info))

## fig2 = plt.figure(2)
## fig2.clf()
## axis2 = fig2.add_subplot(111)
## hist = axis2.hist(depolvals, bins = 100)

## plt.show()

## os.chdir(olddir)
