import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
from sip_tpv.sip_to_pv import sip_to_pv

def test():
    sipheader = fits.Header.fromtextfile('data/IRAC_3.6um_sip.txt')
    myheader = sipheader.copy()
    sip_to_pv(myheader)
    wsip = WCS(sipheader)
    wtpv = WCS(myheader)
    world1 = wsip.all_pix2world([[1, 1]], 1)
    world2 = wtpv.all_pix2world([[1, 1]], 1)
