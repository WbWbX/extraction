# -*- coding: utf-8 -*-

"""
Run as script to produce datacards, requires environment with
`CombineHarvester <https://cms-analysis.github.io/CombineHarvester/python-interface.html>`_.
View arguments with ``python2 python/build_cards.py -h``.
"""

import argparse

import ROOT
import CombineHarvester.CombineTools.ch as ch
# see https://cms-analysis.github.io/CombineHarvester/python-interface.html

from config.general import general
from helpers import histopath
from config.datasets import signal, background
from config.systematics import systematics

era = '13TeV'


def buildcard(outpath, year, region, shape):
    """
    builds datacard

    :param outpath: output path for datacard
    :param year: year to build card for
    :param region: region to build card for
    :param shape: shape to build card for
    """
    bins = [(0, region + '_' + year)]

    parser = ch.CombineHarvester()

    # add observation
    #parser.AddObservations(era=[era], bin=bins) FIXME uncomment when obs shape is added

    # add MC
    parser.AddProcesses(procs=signal.keys(), era=[era], bin=bins, signal=True)
    parser.AddProcesses(procs=background.keys(), era=[era], bin=bins, signal=False)

    # fill with shapes
    def setShape(p):
        f = ROOT.TFile(histopath(year=year, region=region, dataset=p.process(), systematic='nominal'), 'read')
        s = f.Get(general['Histodir'] + '/' + shape)

        p.set_shape(s, True)

    parser.ForEachProc(setShape)


    # add systematics
    for syst in systematics:
        systematic = systematics[syst]

        if syst == 'nominal' or year not in systematic['years']:
            continue

        processes = parser.process_set()
        if 'datasets' in systematic.keys():
            processes = systematic['datasets']

        if systematic['type'] == 'shape':
            for process in processes:
                print('adding systematic: ', process, syst)

                s = ch.Systematic()
                s.set_bin(bins[0][1])
                s.set_process(process)
                s.set_era(era)
                if process in signal.keys():
                    s.set_signal(True)

                s.set_name(syst)
                s.set_type('shape')

                # fill shapes
                f_nominal = ROOT.TFile(histopath(year=year, dataset=process,
                                                 region=region, systematic='nominal'), 'read')
                nominalinal = f_nominal.Get(general['Histodir'] + '/' + shape)

                f_up = ROOT.TFile(histopath(year=year, dataset=process,
                                            region=region, systematic=syst + 'UP'), 'read')
                up = f_up.Get(general['Histodir'] + '/' + shape)

                f_down = ROOT.TFile(histopath(year=year, dataset=process,
                                              region=region, systematic=syst + 'DOWN'), 'read')
                down = f_down.Get(general['Histodir'] + '/' + shape)

                s.set_shapes(up, down, nominalinal)
                parser.InsertSystematic(s)
        elif systematic['type'] == 'lnN':
            parser.cp().process(processes).AddSyst(parser, syst, 'lnN', ch.SystMap()(systematic['value']))
        else:
            raise Exception('Unkown systematics type "{}"'.format(syst['type']))



    # AutoMCStats
    parser.SetAutoMCStats(parser, 10, False, 1)



    # TODO fill observation

    parser.PrintAll()
    ch.CardWriter(outpath, outpath.replace('.txt', '.root')).CreateDirectories(True).WriteCards('none', parser)




if __name__ == '__main__':
    argparser = argparse.ArgumentParser()

    argparser.add_argument('--outpath', type=str, default='./cards/datacard.txt',
                           help='output path of datacard')

    argparser.add_argument('--year', type=str, default='2016',
                           help='year of the datacard')

    argparser.add_argument('--region', type=str, default='muon',
                           help='region of the datacard')

    argparser.add_argument('--shape', type=str, default='Reco_Wb',
                           help='shape name')


    args = argparser.parse_args()
    print(args)

    buildcard(outpath=args.outpath,
              year=args.year,
              region=args.region,
              shape=args.shape)
