# -*- coding: utf-8 -*-

import os


general = {
    'MCPath': '/ceph/mlink/Wb/mc/',
    'DataPath': '/ceph/mlink/Wb/data/',
    'Suffix': '.root',
    'Tree': 'Friends',
    'Histodir': 'Histograms',
    'GlobalDefaultValue': -999,
    'Pi': 3.141,
    'DeltaR': 0.4,
    'Lumi': {
        '2016': 35.9,
        '2017': -1,
        '2018': -1,
    },
}


def samplepath(isMC, year=None, filename=None):
    if isMC:
        return general['MCPath'] + year + '/' + filename + general['Suffix']

    else:
        raise Exception('samplepath not defined for data yet!')
        #return general['DataPath'] + year + '/' + run + '/'


def histopath(isMC, year=None, filename=None, region=None, systematic=None):
    histodir = ''

    if isMC:
        histodir = f'{general["MCPath"]}/{year}/{region}/{systematic}/'

    else:
        raise Exception('histopath not defined for data yet!')
        #return general['DataPath'] + year + '/' + run + '/'

    if not os.path.exists(histodir):
        os.makedirs(histodir)

    return histodir + filename + general['Suffix']