import click

# ---- Postgkyl imports ------------------------------------------------
from postgkyl.commands.util import verb_print
from postgkyl.data import GData, GInterpModal
from postgkyl.tools import laguerre_compose
from postgkyl.tools import transform_frame
# ----------------------------------------------------------------------

@click.command(help='Shortcut to load Gkeyll PKPM data, interpolate, and transform')
@click.option('--name', '-n', type=click.STRING, prompt=True,
              help="Set the root name for files")
@click.option('--species', '-s', type=click.STRING, prompt=True,
              help="Set species name")
@click.option('--idx', '-i', type=click.STRING, prompt=True,
              help="Set the file number")
@click.option('--poly_order', '-p', type=click.INT, prompt=True,
              help="Set the polynomial order")
@click.option('--tag', '-t',
              help='Optional tag for the resulting array')
@click.option('--label', '-l',
              help="Custom label for the result")
@click.pass_context
def pkpm(ctx, **kwargs):
  verb_print(ctx, 'Starting Gkyl PKPM')
  data = ctx.obj['data']

  gf = GData('{:s}-{:s}_{:s}.gkyl'.format(
    kwargs['name'], kwargs['species'], kwargs['idx']))
  gvars = GData('{:s}-{:s}_pkpm_vars_{:s}.gkyl'.format(
    kwargs['name'], kwargs['species'], kwargs['idx']))

  num_dims = gf.get_num_dims()
  c_dim = num_dims - 1

  dg = GInterpModal(gf, kwargs['poly_order'], 'pkpmhyb')
  dg.interpolate((0,1), overwrite=True)

  dg = GInterpModal(gvars, kwargs['poly_order'], 'ms')
  grid_and_T_m = dg.interpolate(3)
  grid_and_us = dg.interpolate((0,1,2))

  laguerre_compose(gf, grid_and_T_m, gf)
  transform_frame(gf, grid_and_us, c_dim, gf)

  gf.set_tag(kwargs['tag'])
  gf.set_label(kwargs['label'])
  data.add(gf)

  verb_print(ctx, 'Finishing Gkyl PKPM')
#end