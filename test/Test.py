#!/usr/bin/env python
# Copyright (c) 2011, Joerg Raedler (Berlin, Germany)
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this list
# of conditions and the following disclaimer. Redistributions in binary form must
# reproduce the above copyright notice, this list of conditions and the following
# disclaimer in the documentation and/or other materials provided with the
# distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


import DyMat, DyMat.Export, random

files = ('DoublePendulum_Dymola-7.4.mat', 
         'DoublePendulum_OpenModelica-1.8.mat',
         'DoublePendulum_Dymola-2012.mat',
         'DoublePendulum_Dymola-2012-SaveAs.mat',
         'DoublePendulum_Dymola-2012-SaveAsPlotted.mat')

formats = DyMat.Export.formats.keys()


for fi in files:
    # open file
    df = DyMat.DyMatFile(fi)
    
    # pick a maximum of 30 random variable names
    n = df.names()
    x = min(len(n), 30)
    va = random.sample(df.names(), x)
    print(va)
    
    # do export
    for fo in formats:
        print('Exporting %s to %s' % (fi, fo))
        try:
            DyMat.Export.export(fo, df, va)
        except Exception as e:
            print(e)
