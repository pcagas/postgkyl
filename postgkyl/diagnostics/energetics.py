#!/usr/bin/env python
"""
Postgkyl module for separating different components of energy
"""
import numpy as np
from .. import diagnostics as diag

def energetics(dataElc, dataIon, dataField, overwrite=False, stack=False):
    """Function to separate components of the energy of each species and EM fields into
    constituent parts (species energy -> thermal + kinetic, field energy -> electric + magnetic)

    Parameters:
    dataElc -- input GData object for electrons
    dataIon -- input GData object for ions
    dataField -- input GData object for EM fields

    Notes:
    Assumes two-species plasma
    """
    if stack:
        overwrite = stack
        print("Deprecation warning: The 'stack' parameter is going to be replaced with 'overwrite'")
    #end
    # Grid is the same for each of the input objects 
    grid = dataField.getGrid()
    valuesField = dataField.getValues()
    # Output array is a seven component field
    # 1) Electron thermal, 2) Electron kinetic, 3) Ion thermal, 4) Ion kinetic
    # 5) Electric, 6) Magnetic, 7) Total
    out = np.zeros(valuesField[...,0:7].shape)

    grid, pre = diag.primitive.getP(dataElc, gasGamma)
    grid, kee = diag.primitive.getKE(dataElc)
    grid, pri = diag.primitive.getP(dataIon, gasGamma)
    grid, kei = diag.primitive.getKE(dataIon)
    # Can compute magnitude squared of electric and magnetic fields with magsq diagnostic
    grid, esq = diag.magsq(dataField, coords='0:3')
    grid, bsq = diag.magsq(dataField, coords='3:6')

    out[..., 0] = np.squeeze(pre/(gasGamma-1))
    out[..., 1] = np.squeeze(kee)
    out[..., 2] = np.squeeze(pri/(gasGamma-1))
    out[..., 3] = np.squeeze(kei)
    out[..., 4] = np.squeeze(esq/2.0)
    out[..., 5] = np.squeeze(bsq/2.0)
    out[..., 6] = np.squeeze(pre/(gasGamma-1)+kee+pri/(gasGamma-1)+kei+esq/2.0+bsq/2.0)
    if overwrite:
        data.push(grid, out)
    else:
        return grid, out
    #end
#end
