#!/usr/bin/env python

import DyMat, DyMat.Export, random

files = ('DoublePendulum_Dymola-7.4.mat', 'DoublePendulum_OpenModelica-1.8.mat')
formats = DyMat.Export.formats.keys()


for fi in files:
    # open file
    df = DyMat.DyMatFile(fi)
    
    # pick 20 random variable names
    va = random.sample(df.names(), 20)
    
    # do export
    for fo in formats:
        if not fo == 'Gnuplot':
            print('Exporting %s to %s' % (fi, fo))
            DyMat.Export.export(fo, df, va)
