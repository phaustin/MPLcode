To compile:

python setup_hist.py build_ext --inplace

or for python(x,y)

python setup_hist.py build_ext --inplace --compiler=mingw32


to test: 

python newtest.py


_________________________

Note on windows:  with 64 bit windows, running 32 bit anaconda produces
a doubled image.  To reproduce:

install 32 bit  anaconda  in c:\Anaconda32 (don't let it change
the system path)

install 64 bit anaconda in c:\Anaconda64  (ibid)

install rapidee, per the recommendation at

https://support.enthought.com/entries/23646538-Make-Canopy-s-User-Python-be-your-default-Python-i-e-on-the-PATH-


Use rapidee to switch between installations by overwriting the path variable using
one of these commands:

c:/Users/phil/bin/rapidee -S path c:/Users/phil/bin;c:/Anaconda64;c:/Anaconda64/Scripts;"c:\Program Files (x86)\Git\bin"

c:/Users/phil/bin/rapidee -S path c:/Users/phil/bin;c:/Anaconda32;c:/Anaconda32/Scripts;"c:\Program Files (x86)\Git\bin"

c:/Users/phil/bin/rapidee -S path c:/Users/phil/bin/;c:/Users/phil/AppData/Local/Enthought/Canopy32/User/Scripts
c:\Users\phil\bin\rapidee -S path c:\Users\phil\bin/;c:\Anaconda32;c:\Anaconda32\Scripts;"c:\Program Files (x86)\Git\bin"


start a new cmd.exe  to get the correct path

do 

python -v

to make sure you have the right python

then go to hist2d and do:

python setup_hist.py build_ext --inplace


When I run:

python newtest.py

the images look good with Anaconda64 bit and screw up with Anacond32.

 

