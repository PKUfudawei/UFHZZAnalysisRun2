import FWCore.ParameterSet.Config as cms

from UFHZZAnalysisRun2.SVFlavourTag.pfSVFlavourTagInfos_cfi import pfSVFlavourTagInfos
# from RecoBTag.ONNXRuntime.boostedJetONNXJetTagsProducer_cfi import boostedJetONNXJetTagsProducer
from UFHZZAnalysisRun2.SVFlavourTag.pfSVFlavourONNXTagsProducer_cfi import pfSVFlavourONNXTagsProducer


genBCHadrons = cms.EDProducer('HadronAndPartonSelector',
    src = cms.InputTag("generator"),
    particles = cms.InputTag("prunedGenParticles"),
    partonMode = cms.string("Auto"),
    fullChainPhysPartons = cms.bool(True),
)

pfParticleNetSVFlavourTagInfos = pfSVFlavourTagInfos.clone(
    deltar_match_sv_pfcand = 0.4,
    pf_candidates = cms.InputTag("packedPFCandidates"),
    secondary_vertices = cms.InputTag("slimmedSecondaryVertices"),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    bHadrons = cms.InputTag("genBCHadrons", "bHadrons"),
    cHadrons = cms.InputTag("genBCHadrons", "cHadrons"),
    debugMode = False,
)

pfParticleNetSVFlavourTagsPhantomJets =  pfSVFlavourONNXTagsProducer.clone(
    src = cms.InputTag('pfParticleNetSVFlavourTagInfos'),
    phantom_jets = cms.InputTag('pfParticleNetSVFlavourTagInfos', 'svPhantomJets'), # a dummy jet collection for easy implementation
    preprocess_json = 'UFHZZAnalysisRun2/SVFlavourTag/data/ParticleNetSV/V02/preprocess_corr.json',
    model_path = 'UFHZZAnalysisRun2/SVFlavourTag/data/ParticleNetSV/V02/model.onnx',
    flav_names = ['probb', 'probbb', 'probc', 'probcc', 'probunmat'],
    debugMode = False,
)