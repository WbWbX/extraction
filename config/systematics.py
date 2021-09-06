# -*- coding: utf-8 -*-
systematics = {

    # Nominal
    'nom': {
        'type': 'shape',
        'years': ['2016', '2017', '2018'],
    },



    #FIXME only test systematics!


    'CMS_Muon_id': {
        'type': 'shape',

        'Reweightonly': True,
        'EventWeights': {'UP': ['tightMuons_weight_id_up/tightMuons_weight_id_nominal'],
                         'DOWN': ['tightMuons_weight_id_down/tightMuons_weight_id_nominal']},
        'years': ['2016', '2017', '2018'],
    },


    'lumi_13TeV': {
        'type': 'lnN',
        'value': 1.01, #TODO
        'years': ['2016', '2017', '2018'],
    },


    'QCDscale': {
        'type': 'lnN',
        'value': (0.908, 1.058), #TODO
        'samples': ['TT_Semileptonic'],
        'years': ['2016', '2017', '2018'],
    },



    ### REWEIGHTING ONLY SYSTEMATICS

    #'lepton_sfUp': {
        #'Name': 'Lepton SF Up',
        #'RootPlotName': 'Lepton efficiencies',
        #'LatexName': 'Lepton efficiencies',
        #'Color': 'KITgreen100',
        #'Reweightonly': True,
        #'EventWeights': ['lepton_sfUp/lepton_sf'],
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'lepton_sfDown': {
        #'Name': 'Lepton SF Down',
        #'RootPlotName': 'Lepton SF Down',
        #'LatexName': 'Lepton SF Down',
        #'Color': 'KITblue100',
        #'Reweightonly': True,
        #'EventWeights': ['lepton_sfDown/lepton_sf'],
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'btag_weight_mediumUp': {
        #'Name': 'B Tag Weight Up',
        #'RootPlotName': 'b tagging efficiency',
        #'LatexName': 'b tagging efficiency',
        #'Color': 'KITgreen100',
        #'Reweightonly': True,
        #'EventWeights': ['btag_weight_mediumUp/btag_weight_medium'],
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'btag_weight_mediumDown': {
        #'Name': 'B Tag Weight Down',
        #'RootPlotName': 'B Tag Weight Down',
        #'LatexName': 'B Tag Weight Down',
        #'Color': 'KITblue100',
        #'Reweightonly': True,
        #'EventWeights': ['btag_weight_mediumDown/btag_weight_medium'],
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'toptag_weightUp': {
        #'Name': 'Top Tag Weight Up',
        #'RootPlotName': 'top tagging efficiency',
        #'LatexName': 'top tagging efficiency',
        #'Color': 'KITgreen100',
        #'Reweightonly': True,
        #'EventWeights': ['toptag_weightUp/toptag_weight'],
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'toptag_weightDown': {
        #'Name': 'Top Tag Weight Down',
        #'RootPlotName': 'Top Tag Weight Down',
        #'LatexName': 'Top Tag Weight Down',
        #'Color': 'KITblue100',
        #'Reweightonly': True,
        #'EventWeights': ['toptag_weightDown/toptag_weight'],
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'l1prefiring_weightUp': {
        #'Name': 'L1 Prefiring Weight Up',
        #'RootPlotName': 'L1 prefiring weight',
        #'LatexName': 'L1 prefiring weight',
        #'Color': 'KITgreen100',
        #'Reweightonly': True,
        #'EventWeights': ['L1PreFiringWeight_Up/L1PreFiringWeight_Nom'],
        #'years': ['2016', '2017'],
        #'correlation': {
        #'20162017': 0,
        #},
    #},
    #'l1prefiring_weightDown': {
        #'Name': 'L1 Prefiring Weight Down',
        #'RootPlotName': 'L1 prefiring weight',
        #'LatexName': 'L1 prefiring weight',
        #'Color': 'KITblue100',
        #'Reweightonly': True,
        #'EventWeights': ['L1PreFiringWeight_Dn/L1PreFiringWeight_Nom'],
        #'years': ['2016', '2017'],
        #'correlation': {
        #'20162017': 0,
        #},
    #},
    #'puWeightUp': {
        #'Name': 'PileUp Weight Up',
        #'RootPlotName': 'Pileup',
        #'LatexName': 'Pileup',
        #'Color': 'KITgreen100',
        #'Reweightonly': True,
        #'EventWeights': ['puWeightUp/puWeight'],
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'puWeightDown': {
        #'Name': 'PileUp Weight Down',
        #'RootPlotName': 'PileUp Weight Down',
        #'LatexName': 'PileUp Weight Down',
        #'Color': 'KITblue100',
        #'Reweightonly': True,
        #'EventWeights': ['puWeightDown/puWeight'],
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'isrUp': {
        #'Name': 'ISR Weight Up',
        #'RootPlotName': 'ISR',
        #'LatexName': 'ISR',
        #'Color': 'KITgreen100',
        #'Reweightonly': True,
        #'EventWeights': ['PSWeight[2]'],
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'isrDown': {
        #'Name': 'ISR Weight Down',
        #'RootPlotName': 'ISR Weight Down',
        #'LatexName': 'ISR Weight Down',
        #'Color': 'KITblue100',
        #'Reweightonly': True,
        #'EventWeights': ['PSWeight[0]'],
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'fsrUp': {
        #'Name': 'FSR Weight Up',
        #'RootPlotName': 'FSR',
        #'LatexName': 'FSR',
        #'Color': 'KITgreen100',
        #'Reweightonly': True,
        #'EventWeights': ['PSWeight[3]'],
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'fsrDown': {
        #'Name': 'FSR Weight Down',
        #'RootPlotName': 'FSR Weight Down',
        #'LatexName': 'FSR Weight Down',
        #'Color': 'KITblue100',
        #'Reweightonly': True,
        #'EventWeights': ['PSWeight[1]'],
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'luminosityUp': {
        #'Name': 'Luminosity Up',
        #'RootPlotName': 'Luminosity',
        #'LatexName': 'Luminosity',
        #'Color': 'KITgreen100',
        #'Reweightonly': True,
        #'EventWeights': ['1.025'],
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'luminosityDown': {
        #'Name': 'Luminosity Down',
        #'RootPlotName': 'Luminosity Down',
        #'LatexName': 'Luminosity Down',
        #'Color': 'KITblue100',
        #'Reweightonly': True,
        #'EventWeights': ['0.975'],
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},

    #### VARIABLE CHANGING SYSTEMATICS


    #'unclustEnUp': {
        #'Name': 'UE Up',
        #'RootPlotName': 'Unclustered Energy',
        #'LatexName': 'Unclustered Energy',
        #'Color': 'KITgreen100',
        #'metbranchsuffix': '_unclustEnUp',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'unclustEnDown': {
        #'Name': 'UE Down',
        #'RootPlotName': 'UE Down',
        #'LatexName': 'UE Down',
        #'Color': 'KITblue100',
        #'metbranchsuffix': '_unclustEnDown',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},

    #'jerUp': {
        #'Name': 'JER Up',
        #'RootPlotName': 'JER',
        #'LatexName': 'JER',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jerUp',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jerDown': {
        #'Name': 'JER Down',
        #'RootPlotName': 'JER Down',
        #'LatexName': 'JER Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jerDown',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},

    #'jesTotalUp': {
        #'Name': 'JES Up',
        #'RootPlotName': 'JES',
        #'LatexName': 'JES',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesTotalUp',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesTotalDown': {
        #'Name': 'JES Down',
        #'RootPlotName': 'JES Down',
        #'LatexName': 'JES Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesTotalDown',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesAbsoluteMPFBiasUp': {
        #'Name': 'JES AbsoluteMPFBias Up',
        #'RootPlotName': 'JES AbsoluteMPFBias Up',
        #'LatexName': 'JES AbsoluteMPFBias',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesAbsoluteMPFBiasUp',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesAbsoluteMPFBiasDown': {
        #'Name': 'JES AbsoluteMPFBias Down',
        #'RootPlotName': 'JES AbsoluteMPFBias Down',
        #'LatexName': 'JES AbsoluteMPFBias Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesAbsoluteMPFBiasDown',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesAbsoluteSampleUp': {
        #'Name': 'JES AbsoluteSample Up',
        #'RootPlotName': 'JES AbsoluteSample Up',
        #'LatexName': 'JES AbsoluteSample',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesAbsoluteSampleUp',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesAbsoluteSampleDown': {
        #'Name': 'JES AbsoluteSample Down',
        #'RootPlotName': 'JES AbsoluteSample Down',
        #'LatexName': 'JES AbsoluteSample Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesAbsoluteSampleDown',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesAbsoluteScaleUp': {
        #'Name': 'JES AbsoluteScale Up',
        #'RootPlotName': 'JES AbsoluteScale Up',
        #'LatexName': 'JES AbsoluteScale',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesAbsoluteScaleUp',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesAbsoluteScaleDown': {
        #'Name': 'JES AbsoluteScale Down',
        #'RootPlotName': 'JES AbsoluteScale Down',
        #'LatexName': 'JES AbsoluteScale Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesAbsoluteScaleDown',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesAbsoluteStatUp': {
        #'Name': 'JES AbsoluteStat Up',
        #'RootPlotName': 'JES AbsoluteStat Up',
        #'LatexName': 'JES AbsoluteStat',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesAbsoluteStatUp',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesAbsoluteStatDown': {
        #'Name': 'JES AbsoluteStat Down',
        #'RootPlotName': 'JES AbsoluteStat Down',
        #'LatexName': 'JES AbsoluteStat Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesAbsoluteStatDown',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesFlavorQCDUp': {
        #'Name': 'JES FlavorQCD Up',
        #'RootPlotName': 'JES FlavorQCD Up',
        #'LatexName': 'JES FlavorQCD',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesFlavorQCDUp',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesFlavorQCDDown': {
        #'Name': 'JES FlavorQCD Down',
        #'RootPlotName': 'JES FlavorQCD Down',
        #'LatexName': 'JES FlavorQCD Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesFlavorQCDDown',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesFragmentationUp': {
        #'Name': 'JES Fragmentation Up',
        #'RootPlotName': 'JES Fragmentation Up',
        #'LatexName': 'JES Fragmentation',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesFragmentationUp',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesFragmentationDown': {
        #'Name': 'JES Fragmentation Down',
        #'RootPlotName': 'JES Fragmentation Down',
        #'LatexName': 'JES Fragmentation Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesFragmentationDown',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesPileUpDataMCUp': {
        #'Name': 'JES PileUpDataMC Up',
        #'RootPlotName': 'JES PileUpDataMC Up',
        #'LatexName': 'JES PileUpDataMC',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesPileUpDataMCUp',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesPileUpDataMCDown': {
        #'Name': 'JES PileUpDataMC Down',
        #'RootPlotName': 'JES PileUpDataMC Down',
        #'LatexName': 'JES PileUpDataMC Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesPileUpDataMCDown',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesPileUpPtBBUp': {
        #'Name': 'JES PileUpPtBB Up',
        #'RootPlotName': 'JES PileUpPtBB Up',
        #'LatexName': 'JES PileUpPtBB',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesPileUpPtBBUp',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesPileUpPtBBDown': {
        #'Name': 'JES PileUpPtBB Down',
        #'RootPlotName': 'JES PileUpPtBB Down',
        #'LatexName': 'JES PileUpPtBB Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesPileUpPtBBDown',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesPileUpPtEC1Up': {
        #'Name': 'JES PileUpPtEC1 Up',
        #'RootPlotName': 'JES PileUpPtEC1 Up',
        #'LatexName': 'JES PileUpPtEC1',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesPileUpPtEC1Up',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesPileUpPtEC1Down': {
        #'Name': 'JES PileUpPtEC1 Down',
        #'RootPlotName': 'JES PileUpPtEC1 Down',
        #'LatexName': 'JES PileUpPtEC1 Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesPileUpPtEC1Down',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesPileUpPtEC2Up': {
        #'Name': 'JES PileUpPtEC2 Up',
        #'RootPlotName': 'JES PileUpPtEC2 Up',
        #'LatexName': 'JES PileUpPtEC2',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesPileUpPtEC2Up',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesPileUpPtEC2Down': {
        #'Name': 'JES PileUpPtEC2 Down',
        #'RootPlotName': 'JES PileUpPtEC2 Down',
        #'LatexName': 'JES PileUpPtEC2 Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesPileUpPtEC2Down',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesPileUpPtHFUp': {
        #'Name': 'JES PileUpPtHF Up',
        #'RootPlotName': 'JES PileUpPtHF Up',
        #'LatexName': 'JES PileUpPtHF',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesPileUpPtHFUp',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesPileUpPtHFDown': {
        #'Name': 'JES PileUpPtHF Down',
        #'RootPlotName': 'JES PileUpPtHF Down',
        #'LatexName': 'JES PileUpPtHF Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesPileUpPtHFDown',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesPileUpPtRefUp': {
        #'Name': 'JES PileUpPtRef Up',
        #'RootPlotName': 'JES PileUpPtRef Up',
        #'LatexName': 'JES PileUpPtRef',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesPileUpPtRefUp',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesPileUpPtRefDown': {
        #'Name': 'JES PileUpPtRef Down',
        #'RootPlotName': 'JES PileUpPtRef Down',
        #'LatexName': 'JES PileUpPtRef Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesPileUpPtRefDown',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesRelativeBalUp': {
        #'Name': 'JES RelativeBal Up',
        #'RootPlotName': 'JES RelativeBal Up',
        #'LatexName': 'JES RelativeBal',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesRelativeBalUp',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesRelativeBalDown': {
        #'Name': 'JES RelativeBal Down',
        #'RootPlotName': 'JES RelativeBal Down',
        #'LatexName': 'JES RelativeBal Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesRelativeBalDown',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesRelativeFSRUp': {
        #'Name': 'JES RelativeFSR Up',
        #'RootPlotName': 'JES RelativeFSR Up',
        #'LatexName': 'JES RelativeFSR',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesRelativeFSRUp',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesRelativeFSRDown': {
        #'Name': 'JES RelativeFSR Down',
        #'RootPlotName': 'JES RelativeFSR Down',
        #'LatexName': 'JES RelativeFSR Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesRelativeFSRDown',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesRelativeJEREC1Up': {
        #'Name': 'JES RelativeJEREC1 Up',
        #'RootPlotName': 'JES RelativeJEREC1 Up',
        #'LatexName': 'JES RelativeJEREC1',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesRelativeJEREC1Up',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesRelativeJEREC1Down': {
        #'Name': 'JES RelativeJEREC1 Down',
        #'RootPlotName': 'JES RelativeJEREC1 Down',
        #'LatexName': 'JES RelativeJEREC1 Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesRelativeJEREC1Down',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesRelativeJEREC2Up': {
        #'Name': 'JES RelativeJEREC2 Up',
        #'RootPlotName': 'JES RelativeJEREC2 Up',
        #'LatexName': 'JES RelativeJEREC2',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesRelativeJEREC2Up',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesRelativeJEREC2Down': {
        #'Name': 'JES RelativeJEREC2 Down',
        #'RootPlotName': 'JES RelativeJEREC2 Down',
        #'LatexName': 'JES RelativeJEREC2 Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesRelativeJEREC2Down',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesRelativeJERHFUp': {
        #'Name': 'JES RelativeJERHF Up',
        #'RootPlotName': 'JES RelativeJERHF Up',
        #'LatexName': 'JES RelativeJERHF',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesRelativeJERHFUp',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesRelativeJERHFDown': {
        #'Name': 'JES RelativeJERHF Down',
        #'RootPlotName': 'JES RelativeJERHF Down',
        #'LatexName': 'JES RelativeJERHF Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesRelativeJERHFDown',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesRelativePtBBUp': {
        #'Name': 'JES RelativePtBB Up',
        #'RootPlotName': 'JES RelativePtBB Up',
        #'LatexName': 'JES RelativePtBB',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesRelativePtBBUp',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesRelativePtBBDown': {
        #'Name': 'JES RelativePtBB Down',
        #'RootPlotName': 'JES RelativePtBB Down',
        #'LatexName': 'JES RelativePtBB Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesRelativePtBBDown',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesRelativePtEC1Up': {
        #'Name': 'JES RelativePtEC1 Up',
        #'RootPlotName': 'JES RelativePtEC1 Up',
        #'LatexName': 'JES RelativePtEC1',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesRelativePtEC1Up',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesRelativePtEC1Down': {
        #'Name': 'JES RelativePtEC1 Down',
        #'RootPlotName': 'JES RelativePtEC1 Down',
        #'LatexName': 'JES RelativePtEC1 Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesRelativePtEC1Down',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesRelativePtEC2Up': {
        #'Name': 'JES RelativePtEC2 Up',
        #'RootPlotName': 'JES RelativePtEC2 Up',
        #'LatexName': 'JES RelativePtEC2',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesRelativePtEC2Up',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesRelativePtEC2Down': {
        #'Name': 'JES RelativePtEC2 Down',
        #'RootPlotName': 'JES RelativePtEC2 Down',
        #'LatexName': 'JES RelativePtEC2 Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesRelativePtEC2Down',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesRelativePtHFUp': {
        #'Name': 'JES RelativePtHF Up',
        #'RootPlotName': 'JES RelativePtHF Up',
        #'LatexName': 'JES RelativePtHF',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesRelativePtHFUp',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesRelativePtHFDown': {
        #'Name': 'JES RelativePtHF Down',
        #'RootPlotName': 'JES RelativePtHF Down',
        #'LatexName': 'JES RelativePtHF Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesRelativePtHFDown',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesRelativeStatECUp': {
        #'Name': 'JES RelativeStatEC Up',
        #'RootPlotName': 'JES RelativeStatEC Up',
        #'LatexName': 'JES RelativeStatEC',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesRelativeStatECUp',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesRelativeStatECDown': {
        #'Name': 'JES RelativeStatEC Down',
        #'RootPlotName': 'JES RelativeStatEC Down',
        #'LatexName': 'JES RelativeStatEC Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesRelativeStatECDown',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesRelativeStatFSRUp': {
        #'Name': 'JES RelativeStatFSR Up',
        #'RootPlotName': 'JES RelativeStatFSR Up',
        #'LatexName': 'JES RelativeStatFSR',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesRelativeStatFSRUp',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesRelativeStatFSRDown': {
        #'Name': 'JES RelativeStatFSR Down',
        #'RootPlotName': 'JES RelativeStatFSR Down',
        #'LatexName': 'JES RelativeStatFSR Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesRelativeStatFSRDown',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesRelativeStatHFUp': {
        #'Name': 'JES RelativeStatHF Up',
        #'RootPlotName': 'JES RelativeStatHF Up',
        #'LatexName': 'JES RelativeStatHF',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesRelativeStatHFUp',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesRelativeStatHFDown': {
        #'Name': 'JES RelativeStatHF Down',
        #'RootPlotName': 'JES RelativeStatHF Down',
        #'LatexName': 'JES RelativeStatHF Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesRelativeStatHFDown',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesSinglePionECALUp': {
        #'Name': 'JES SinglePionECAL Up',
        #'RootPlotName': 'JES SinglePionECAL Up',
        #'LatexName': 'JES SinglePionECAL',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesSinglePionECALUp',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesSinglePionECALDown': {
        #'Name': 'JES SinglePionECAL Down',
        #'RootPlotName': 'JES SinglePionECAL Down',
        #'LatexName': 'JES SinglePionECAL Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesSinglePionECALDown',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesSinglePionHCALUp': {
        #'Name': 'JES SinglePionHCAL Up',
        #'RootPlotName': 'JES SinglePionHCAL Up',
        #'LatexName': 'JES SinglePionHCAL',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesSinglePionHCALUp',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesSinglePionHCALDown': {
        #'Name': 'JES SinglePionHCAL Down',
        #'RootPlotName': 'JES SinglePionHCAL Down',
        #'LatexName': 'JES SinglePionHCAL Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesSinglePionHCALDown',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesTimePtEtaUp': {
        #'Name': 'JES TimePtEta Up',
        #'RootPlotName': 'JES TimePtEta Up',
        #'LatexName': 'JES TimePtEta',
        #'Color': 'KITgreen100',
        #'branchsuffix': '_jesTimePtEtaUp',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'jesTimePtEtaDown': {
        #'Name': 'JES TimePtEta Down',
        #'RootPlotName': 'JES TimePtEta Down',
        #'LatexName': 'JES TimePtEta Down',
        #'Color': 'KITblue100',
        #'branchsuffix': '_jesTimePtEtaDown',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},

    ### SPECIFIC SAMPLE SYSTEMATICS

    #'hdampUp': {
        #'Name': 'HDamp Up',
        #'RootPlotName': '#it{h}_{damp}',
        #'LatexName': '\\hdamp',
        #'Color': 'KITgreen100',
        #'Samples': {
        #'TTToHadronic': {
            #'2016': {
            #'KFactor': 1.00447625769,
            #'Entries': 28695100,
            #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/TTToHadronic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2017': {
            #'KFactor': 1.00543808808,
            #'Entries': 27203920,
            #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/TTToHadronic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2018': {
            #'KFactor': 1.00495880094,
            #'Entries': 24965000,
            #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8.root',
            #},
        #},
        #'TTTo2L2Nu': {
            #'2016': {
            #'KFactor': 1.00419353954,
            #'Entries': 14889100,
            #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2017': {
            #'KFactor': 1.00429236095,
            #'Entries': 3288128,
            #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2018': {
            #'KFactor': 1.00429764544,
            #'Entries': 15163000,
            #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8.root',
            #},
        #},
        #'TTToSemilepton': {
            #'2016': {
            #'KFactor': 1.0041611867,
            #'Entries': 29671200,
            #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/TTToSemiLeptonic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2017': {
            #'KFactor': 1.00424912606,
            #'Entries': 23977012,
            #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/TTToSemiLeptonic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2018': {
            #'KFactor': 1.0042918434,
            #'Entries': 26964000,
            #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8.root',
            #},
        #},
        #'TTToSemileptonResolved': {
            #'2016': {
            #'KFactor': 1.0041611867,
            #'Entries': 29671200,
            #},
            #'2017': {
            #'KFactor': 1.00424912606,
            #'Entries': 23977012,
            #},
            #'2018': {
            #'KFactor': 1.0042918434,
            #'Entries': 26964000,
            #},
        #},
        #'TTToSemileptonHT250': {
            #'2016': {
            #'KFactor': 1.0041611867*10.55, #FIXME Corrected for XS
            #'Entries': 29671200,
            #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/TTToSemiLeptonic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2017': {
            #'KFactor': 1.00424912606*10.55, #FIXME Corrected for XS
            #'Entries': 23977012,
            #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/TTToSemiLeptonic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2018': {
            #'KFactor': 1.01222198867,
            #'Entries': 23673196,
            #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/TTToSemiLeptonic_AK8HT250_hdampUP_TuneCP5_13TeV-powheg-pythia8.root',
            #},
        #},
        #'TTToSemileptonHT250Boosted': {
            #'2016': {
            #'KFactor': 1.0041611867*10.55, #FIXME Corrected for XS
            #'Entries': 29671200,
            #},
            #'2017': {
            #'KFactor': 1.00424912606*10.55, #FIXME Corrected for XS
            #'Entries': 23977012,
            #},
            #'2018': {
            #'KFactor': 1.01222198867,
            #'Entries': 23673196,
            #},
        #},
        #},
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'hdampDown': {
        #'Name': 'HDamp Down',
        #'RootPlotName': 'HDamp Down',
        #'LatexName': 'HDamp Down',
        #'Color': 'KITblue100',
        #'Samples': {
        #'TTToHadronic': {
            #'2016': {
            #'KFactor': 1.01932108429,
            #'Entries': 28900700,
            #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/TTToHadronic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2017': {
            #'KFactor': 1.0190080839,
            #'Entries': 27117982,
            #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/TTToHadronic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2018': {
            #'KFactor': 1.01870579084,
            #'Entries': 26425000,
            #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8.root',
            #},
        #},
        #'TTTo2L2Nu': {
            #'2016': {
            #'KFactor': 1.01616014021,
            #'Entries': 14908700,
            #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2017': {
            #'KFactor': 1.01653446529,
            #'Entries': 5476459,
            #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2018': {
            #'KFactor': 1.0163094261,
            #'Entries': 15410000,
            #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8.root',
            #},
        #},
        #'TTToSemilepton': {
            #'2016': {
            #'KFactor': 1.01616125336,
            #'Entries': 29818400,
            #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/TTToSemiLeptonic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2017': {
            #'KFactor': 1.01646215478,
            #'Entries': 26849863,
            #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/TTToSemiLeptonic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2018': {
            #'KFactor': 1.01636868281,
            #'Entries': 25904000,
            #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8.root',
            #},
        #},
        #'TTToSemileptonResolved': {
            #'2016': {
            #'KFactor': 1.01616125336,
            #'Entries': 29818400,
            #},
            #'2017': {
            #'KFactor': 1.01646215478,
            #'Entries': 26849863,
            #},
            #'2018': {
            #'KFactor': 1.01636868281,
            #'Entries': 25904000,
            #},
        #},
        #'TTToSemileptonHT250': {
            #'2016': {
            #'KFactor': 1.01615979422*10.55, #FIXME Corrected for XS
            #'Entries': 29770400,
            #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/TTToSemiLeptonic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2017': {
            #'KFactor': 1.01646889273*10.55, #FIXME Corrected for XS
            #'Entries': 26367765,
            #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/TTToSemiLeptonic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2018': {
            #'KFactor': 1.03221841343,
            #'Entries': 20673194,
            #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/TTToSemiLeptonic_AK8HT250_hdampDOWN_TuneCP5_13TeV-powheg-pythia8.root',
            #},
        #},
        #'TTToSemileptonHT250Boosted': {
            #'2016': {
            #'KFactor': 1.01615979422*10.55, #FIXME Corrected for XS
            #'Entries': 29770400,
            #},
            #'2017': {
            #'KFactor': 1.01646889273*10.55, #FIXME Corrected for XS
            #'Entries': 26367765,
            #},
            #'2018': {
            #'KFactor': 1.03221841343,
            #'Entries': 20673194,
            #},
        #},
        #},
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'tuneUp': {
        #'Name': 'Tune Up',
        #'RootPlotName': 'Underlying event',
        #'LatexName': 'Underlying event',
        #'Color': 'KITgreen100',
        #'Samples': {
        #'TTToHadronic': {
            #'2016': {
            #'KFactor': 1.00868697785,
            #'Entries': 27939400,
            #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/TTToHadronic_TuneCP5up_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2017': {
            #'KFactor': 1.0093499955,
            #'Entries': 27108792,
            #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/TTToHadronic_TuneCP5up_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2018': {
            #'KFactor': 1.00862868433,
            #'Entries': 23488000,
            #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8.root',
            #},
        #},
        #'TTTo2L2Nu': {
            #'2016': {
            #'KFactor': 1.00762972782,
            #'Entries': 14838600,
            #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2017': {
            #'KFactor': 1.00777182749,
            #'Entries': 5500000,
            #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2018': {
            #'KFactor': 1.00782718939,
            #'Entries': 15414000,
            #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8.root',
            #},
        #},
        #'TTToSemilepton': {
            #'2016': {
            #'KFactor': 1.00770902901,
            #'Entries': 29239200,
            #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/TTToSemiLeptonic_TuneCP5up_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2017': {
            #'KFactor': 1.00783560957,
            #'Entries': 20007920,
            #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/TTToSemiLeptonic_TuneCP5up_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2018': {
            #'KFactor': 1.00774973266,
            #'Entries': 26948000,
            #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8.root',
            #},
        #},
        #'TTToSemileptonResolved': {
            #'2016': {
            #'KFactor': 1.00770902901,
            #'Entries': 29239200,
            #},
            #'2017': {
            #'KFactor': 1.00783560957,
            #'Entries': 20007920,
            #},
            #'2018': {
            #'KFactor': 1.00774973266,
            #'Entries': 26948000,
            #},
        #},
        #'TTToSemileptonBoosted': {
            #'2016': {
            #'KFactor': 1.00770902901,
            #'Entries': 29239200,
            #},
            #'2017': {
            #'KFactor': 1.00783560957,
            #'Entries': 20007920,
            #},
            #'2018': {
            #'KFactor': 1.00774973266,
            #'Entries': 26948000,
            #},
        #},
        #'TTToSemileptonHT250': {
            #'2016': {
            #'KFactor': 1.00770037845*10.55, #FIXME Corrected for XS
            #'Entries': 21697600,
            #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/TTToSemiLeptonic_TuneCP5up_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2017': {
            #'KFactor': 1.00784009147*10.55, #FIXME Corrected for XS
            #'Entries': 20122010,
            #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/TTToSemiLeptonic_TuneCP5up_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2018': {
            #'KFactor': 1.01877927059,
            #'Entries': 13791270,
            #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/TTToSemiLeptonic_AK8HT250_TuneCP5up_13TeV-powheg-pythia8.root',
            #},
        #},
        #'TTToSemileptonHT250Boosted': {
            #'2016': {
            #'KFactor': 1.00770037845*10.55, #FIXME Corrected for XS
            #'Entries': 21697600,
            #},
            #'2017': {
            #'KFactor': 1.00784009147*10.55, #FIXME Corrected for XS
            #'Entries': 20122010,
            #},
            #'2018': {
            #'KFactor': 1.01877927059,
            #'Entries': 13791270,
            #},
        #},
        #},
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'tuneDown': {
        #'Name': 'Tune Down',
        #'RootPlotName': 'Tune Down',
        #'LatexName': 'Tune Down',
        #'Color': 'KITblue100',
        #'Samples': {
        #'TTToHadronic': {
            #'2016': {
            #'KFactor': 1.00851810096,
            #'Entries': 27921200,
            #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/TTToHadronic_TuneCP5down_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2017': {
            #'KFactor': 1.00975087061,
            #'Entries': 27252808,
            #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/TTToHadronic_TuneCP5down_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2018': {
            #'KFactor': 1.00826677876,
            #'Entries': 26675000,
            #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8.root',
            #},
        #},
        #'TTTo2L2Nu': {
            #'2016': {
            #'KFactor': 1.00753048789,
            #'Entries': 14366800,
            #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2017': {
            #'KFactor': 1.00777463614,
            #'Entries': 5500000,
            #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2018': {
            #'KFactor': 1.00778209007,
            #'Entries': 14770000,
            #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8.root',
            #},
        #},
        #'TTToSemilepton': {
            #'2016': {
            #'KFactor': 1.00762373773,
            #'Entries': 28951700,
            #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/TTToSemiLeptonic_TuneCP5down_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2017': {
            #'KFactor': 1.00782568672,
            #'Entries': 22911672,
            #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/TTToSemiLeptonic_TuneCP5down_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2018': {
            #'KFactor': 1.00777005803,
            #'Entries': 20483000,
            #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8.root',
            #},
        #},
        #'TTToSemileptonResolved': {
            #'2016': {
            #'KFactor': 1.00762373773,
            #'Entries': 28951700,
            #},
            #'2017': {
            #'KFactor': 1.00782568672,
            #'Entries': 22911672,
            #},
            #'2018': {
            #'KFactor': 1.00777005803,
            #'Entries': 20483000,
            #},
        #},
        #'TTToSemileptonBoosted': {
            #'2016': {
            #'KFactor': 1.00762373773,
            #'Entries': 28951700,
            #},
            #'2017': {
            #'KFactor': 1.00782568672,
            #'Entries': 22911672,
            #},
            #'2018': {
            #'KFactor': 1.00777005803,
            #'Entries': 20483000,
            #},
        #},
        #'TTToSemileptonHT250': {
            #'2016': {
            #'KFactor': 1.00762883849*10.55, #FIXME Corrected for XS
            #'Entries': 23359000,
            #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/TTToSemiLeptonic_TuneCP5down_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2017': {
            #'KFactor': 1.00777024731*10.55, #FIXME Corrected for XS
            #'Entries': 27104055,
            #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/TTToSemiLeptonic_TuneCP5down_PSweights_13TeV-powheg-pythia8.root',
            #},
            #'2018': {
            #'KFactor': 1.01886301657,
            #'Entries': 13509281,
            #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/TTToSemiLeptonic_AK8HT250_TuneCP5down_13TeV-powheg-pythia8.root',
            #},
        #},
        #'TTToSemileptonHT250Boosted': {
            #'2016': {
            #'KFactor': 1.00762883849*10.55, #FIXME Corrected for XS
            #'Entries': 23359000,
            #},
            #'2017': {
            #'KFactor': 1.00777024731*10.55, #FIXME Corrected for XS
            #'Entries': 27104055,
            #},
            #'2018': {
            #'KFactor': 1.01886301657,
            #'Entries': 13509281,
            #},
        #},
        #},
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},


    ### OTHER FANCY SHIT...

    #'qcdscaleUp': {
        #'Name': 'ME QCD Scale Up',
        #'RootPlotName': '#mu_{R}/#mu_{F} scale',
        #'LatexName': '$\\mur/\\muf$ scale',
        #'Color': 'KITgreen100',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'qcdscaleDown': {
        #'Name': 'ME QCD Scale Down',
        #'RootPlotName': 'ME QCD Scale Down',
        #'LatexName': 'ME QCD Scale Down',
        #'Color': 'KITblue100',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},

    #'pdfalphasUp': {
        #'Name': 'PDF alpha s Up',
        #'RootPlotName': 'PDF+#alpha_{s}',
        #'LatexName': 'PDF+\\as',
        #'Color': 'KITgreen100',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},
    #'pdfalphasDown': {
        #'Name': 'PDF alpha s Down',
        #'RootPlotName': 'PDF alpha s Down',
        #'LatexName': 'PDF alpha s Down',
        #'Color': 'KITblue100',
        #'years': ['2016', '2017', '2018'],
        #'correlation': {
        #'20162017': 0,
        #'20162018': 0,
        #'20172018': 0,
        #'201620172018': 0,
        #},
    #},


    #'xsec_EWKFGUp': {
        #'Name': '$\\sigma$(V + V/Jets)   ',
        #'RootPlotName': '$\\sigma$(V + V/Jets)   ',
        #'LatexName': '$\\sigma$(V + V/Jets)',
    #},
    #'xsec_OtherFGUp': {
        #'Name': '$\\sigma$(QCD, TT + X)   ',
        #'RootPlotName': '$\\sigma$(QCD, TT + X)   ',
        #'LatexName': '$\\sigma$(QCD, TT + X)',
    #},
    #'xsec_STFGUp': {
        #'Name': '$\\sigma$(Single Top)   ',
        #'RootPlotName': '$\\sigma$(Single Top)   ',
        #'LatexName': '$\\sigma$(Single Top)',
    #},
    #'xsec_TTHT250FGUp': {
        #'Name': '$\\sigma$(TT Semilep HT250)   ',
        #'RootPlotName': '$\\sigma$(TT Semilep HT250)   ',
        #'LatexName': '$\\sigma$(TT Semilep HT250)',
    #},
    #'xsec_TTOtherFGUp': {
        #'Name': '$\\sigma$(TT FH + DL)   ',
        #'RootPlotName': '$\\sigma$(TT FH + DL)   ',
        #'LatexName': '$\\sigma$(TT FH + DL)',
    #},
    #'xsec_TTResolvedFGUp': {
        #'Name': '$\\sigma$(TT Semilep)   ',
        #'RootPlotName': '$\\sigma$(TT Semilep)   ',
        #'LatexName': '$\\sigma$(TT Semilep)',
    #},
    #'prop_binsemilepcombined_all_bin0Up': {
        #'Name': 'BB-lite (Bin 1)   ',
        #'RootPlotName': 'BB-lite (Bin 1)   ',
        #'LatexName': 'BB-lite (Bin 1)',
    #},
    #'prop_binsemilepcombined_all_bin1Up': {
        #'Name': 'BB-lite (Bin 2)   ',
        #'RootPlotName': 'BB-lite (Bin 2)   ',
        #'LatexName': 'BB-lite (Bin 2)',
    #},
    #'prop_binsemilepcombined_all_bin2Up': {
        #'Name': 'BB-lite (Bin 3)   ',
        #'RootPlotName': 'BB-lite (Bin 3)   ',
        #'LatexName': 'BB-lite (Bin 3)',
    #},

}
