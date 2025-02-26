import click

from postgkyl.commands.util import verb_print
from postgkyl.data import GData
import postgkyl.tools as diag

@click.command(help='Magnitude squared of an input array |A|^2 = sum_i A_i^2')
@click.option('--use', '-u', default=None,
              help="Specify the tag to integrate")
@click.option('--tag', '-t', default=None,
              help='Optional tag for the resulting array')
@click.option('--label', '-l',
              help="Custom label for the result")
@click.pass_context
def magsq(ctx, **kwargs):
  """Calculate the magnitude squared of an input array
  """
  verb_print(ctx, 'Starting magnitude squared computation')
  data = ctx.obj['data']

  for dat in data.iterator(kwargs['use']):
    if kwargs['tag']:
      out = GData(tag=kwargs['tag'],
                  label=kwargs['label'],
                  comp_grid=ctx.obj['compgrid'],
                  ctx=dat.ctx)
      grid, values = diag.magsq(dat)
      out.push(grid, values)
      data.add(out)
    else:
      diag.magsq(dat, overwrite=True)
    #end
  #end

  verb_print(ctx, 'Finishing magnitude squared computation')
#end
