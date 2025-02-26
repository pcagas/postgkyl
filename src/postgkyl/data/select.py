import numpy as np

from postgkyl.utils import idxParser


def select(data, comp=None, overwrite=False,
           z0=None, z1=None, z2=None,
           z3=None, z4=None, z5=None):
  """Selects parts of the GData.

  Allows to select only a part of GData (both coordinates and
  components).  Allows for numpy slices, selecting multiple
  components, and using both indicies (integer) and values (float).

  Atributes:
    data (GData)
    z0-5 (index, value, or slice (e.g. '1:5')
    comp (index, slice (e.g. '1:5'), or multiple (e.g. '1,5')
  """
  zs = (z0, z1, z2, z3, z4, z5)
  grid = data.get_grid()
  grid = list(grid)  # copy the grid
  values = data.get_values()
  num_dims = data.get_num_dims()
  values_idx = [slice(0, values.shape[d]) for d in range(num_dims+1)]
  uniform_grid = (len(grid[0].shape) == 1)
  if not uniform_grid:
    grid_idx = [slice(0, grid[d].shape[d]) for d in range(num_dims)]
  #end

  # Loop for coordinates
  for d, z in enumerate(zs):
    if d < num_dims and z is not None:
      if uniform_grid:
        len_grid = grid[d].shape[0]
      else:
        len_grid = grid[d].shape[d]
      #end
      is_matching = (values.shape[d] == len_grid)
      idx = idxParser(z, grid[d], is_matching)
      if isinstance(idx, int):
        # when 'slice' is used instead of an integer
        # number, numpy array is not squeezed after
        # subselecting
        vIdx = slice(idx, idx+1)
        gIdx = slice(idx, idx+2) if not is_matching else slice(idx, idx+1)
      elif isinstance(idx, slice):
        vIdx = idx
        gIdx = slice(idx.start, idx.stop+1) if not is_matching else idx
      else:
        raise TypeError('The coordinate select can be only single index (int) or a slice')
      #end
      if uniform_grid:
        grid[d] = grid[d][gIdx]
      else:
        grid_idx[d] = gIdx
      #end
      values_idx[d] = vIdx
    #end
  #end

  # Select components
  if comp is not None:
    values_idx[-1] = idxParser(comp)
  #end
  valuesOut = values[tuple(values_idx)]
  if not uniform_grid:
    for d in range(num_dims):
      grid[d] = grid[d][tuple(grid_idx)]
    #end
  #end

  # Adding a dummy dimension indicies
  if num_dims == len(valuesOut.shape):
    valuesOut = valuesOut[..., np.newaxis]
  #end

  if overwrite:
    data.push(grid, valuesOut)
  else:
    return grid, valuesOut
  #end
#end
