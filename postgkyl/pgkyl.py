#!/usr/bin/env python
import os
import base64
import sys
from glob import glob
from time import time

import click
import numpy as np

from postgkyl.data import GData
import postgkyl.commands as cmd
from postgkyl.commands.util import vlog

@click.group(chain=True)
@click.option('-v', '--verbose', is_flag=True,
              help='Turn on verbosity')
@click.option('--filename', '-f', multiple=True,
              help='Specify one or more file(s) to work with.')
@click.option('--savechain', '-c', is_flag=True,
              help='Save command chain for quick repetition')
@click.pass_context
def cli(ctx, filename, verbose, savechain):
    ctx.obj = {}

    ctx.obj['startTime'] = time()
    if verbose:
        ctx.obj['verbose'] = True
        vlog(ctx, 'This is postgkyl running in verbose mode!')
        vlog(ctx, 'Spam! Spam! Spam! Spam! Lovely Spam! Lovely Spam!')
        vlog(ctx, 'And now for something completelly different...')
    else:
        ctx.obj['verbose'] = False

    if savechain:
        ctx.obj['savechain'] = True
        fh = open('pgkylchain.dat', 'w')
        fh.close()
    else:
        ctx.obj['savechain'] = False

    ctx.obj['files'] = filename
    numFiles = len(filename)
    ctx.obj['dataSets'] = []

    cnt = 0
    for s in range(numFiles):
        if "*" not in filename[s]:
            ctx.obj['dataSets'].append(GData(filename[s]))
            vlog(ctx, "Loading '{:s}\' as data set #{:d}".
                 format(fh, cnt))
            cnt += 1
        else:
            files = glob(str(filename[s]))
            for fh in files:
                try:
                    vlog(ctx, "Loading '{:s}\' as data set #{:d}".
                         format(fh, cnt))
                    ctx.obj['dataSets'].append(GData(fh))
                    cnt += 1
                except:
                    pass

    if numFiles > 0 and cnt == 0:
        raise NameError("no files loaded")
    ctx.obj['numSets'] = cnt

    ctx.obj['hold'] = 'off'
    ctx.obj['fig'] = ''
    ctx.obj['ax'] = ''

    dirPath = os.path.dirname(os.path.realpath(__file__))
    if os.path.isfile(dirPath+'/output/postgkyl.mplstyle'): 
        ctx.obj['mplstyle'] = dirPath + '/output/postgkyl.mplstyle'
    else:
        ctx.obj['mplstyle']  = dirPath + '/../../../../data/postgkyl.mplstyle'

cli.add_command(cmd.util.rc)


#cli.add_command(cmd.agyro.agyro)
#cli.add_command(cmd.cglpressure.cglpressure)
#cli.add_command(cmd.diagnostics.growth)
#cli.add_command(cmd.euler.euler)
#cli.add_command(cmd.output.hold)
#cli.add_command(cmd.output.info)
#cli.add_command(cmd.output.plot)
#cli.add_command(cmd.output.write)
#cli.add_command(cmd.select.collect)
#cli.add_command(cmd.select.comp)
#cli.add_command(cmd.select.dataset)
#cli.add_command(cmd.select.fix)
#cli.add_command(cmd.select.pop)
#cli.add_command(cmd.tenmoment.tenmoment)
#cli.add_command(cmd.transform.abs)
#cli.add_command(cmd.transform.curl)
#cli.add_command(cmd.transform.div)
#cli.add_command(cmd.transform.fft)
#cli.add_command(cmd.transform.grad)
#cli.add_command(cmd.transform.integrate)
#cli.add_command(cmd.transform.interpolate)
#cli.add_command(cmd.transform.log)
#cli.add_command(cmd.transform.mask)
#cli.add_command(cmd.transform.mult)
#cli.add_command(cmd.transform.norm)
#cli.add_command(cmd.transform.pow)
#cli.add_command(cmd.transform.transpose)
#cli.add_command(rc)

if __name__ == '__main__':
    cli()


