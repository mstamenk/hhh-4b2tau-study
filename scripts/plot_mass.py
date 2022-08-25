# Script to plot mass of each Higgs bosons from output of the hhh4b2tauProducer

#import section
import os
import ROOT
import itertools

# global variables

# methods

# main 

# Step 1 retrieve file + info in file

#filename = '/isilon/data/users/mstamenk/eos-triple-h/samples-v1-4b2tau-nanoaod-4b2tau/GluGluToHHHTo4B2Tau_SM.root'
# on lxplus
filename = '/afs/cern.ch/work/m/mstamenk/public/forCaden/GluGluToHHHTo4B2Tau_SM.root'


tree = ROOT.TChain('Events') # tree events in the file
tree.AddFile(filename)

# Step 2: loop over events and retrieve informations for jets and taus
i = 0 # counter to just test up to a certain number of events
max_events = 100 # run on 100 events for testing, in total 500k events available

h1_hist = ROOT.TH1F('h1bb','h1bb',20, 0, 200) # 20 bins between 0 and 200 GeV
h2_hist = ROOT.TH1F('h2bb','h2bb',20, 0, 200)
h3_hist = ROOT.TH1F('htautau','htautau',20, 0, 200)

for event in tree:
    jets = []
    # retrieve jet 4 vectors
    # jet1: highest b-tagging score
    jet1 = ROOT.TLorentzVector()
    jet1.SetPtEtaPhiM(event.jet1Pt, event.jet1Eta, event.jet1Phi, event.jet1M)
    jet1.HadronFlavour = event.jet1HadronFlavour # simulated true flavour of the jet (5 = b-jet, 4 = c-jet, 0 = light-jet)
    jet1.HiggsMatched = event.jet1HiggsMatched # jet is matched to a b-quark coming from a Higgs boson (1 = matched, 0 = not matched)

     # jet2
    jet2 = ROOT.TLorentzVector()
    jet2.SetPtEtaPhiM(event.jet2Pt, event.jet2Eta, event.jet2Phi, event.jet2M)
    jet2.HadronFlavour = event.jet2HadronFlavour # simulated true flavour of the jet (5 = b-jet, 4 = c-jet, 0 = light-jet)
    jet2.HiggsMatched = event.jet2HiggsMatched # jet is matched to a b-quark coming from a Higgs boson (1 = matched, 0 = not matched)

     # jet3
    jet3 = ROOT.TLorentzVector()
    jet3.SetPtEtaPhiM(event.jet3Pt, event.jet3Eta, event.jet3Phi, event.jet3M)
    jet3.HadronFlavour = event.jet3HadronFlavour # simulated true flavour of the jet (5 = b-jet, 4 = c-jet, 0 = light-jet)
    jet3.HiggsMatched = event.jet3HiggsMatched # jet is matched to a b-quark coming from a Higgs boson (1 = matched, 0 = not matched)

      # jet4
    jet4 = ROOT.TLorentzVector()
    jet4.SetPtEtaPhiM(event.jet4Pt, event.jet4Eta, event.jet4Phi, event.jet4M)
    jet4.HadronFlavour = event.jet4HadronFlavour # simulated true flavour of the jet (5 = b-jet, 4 = c-jet, 0 = light-jet)
    jet4.HiggsMatched = event.jet4HiggsMatched # jet is matched to a b-quark coming from a Higgs boson (1 = matched, 0 = not matched)

    # jet5
    jet5 = ROOT.TLorentzVector()
    jet5.SetPtEtaPhiM(event.jet5Pt, event.jet5Eta, event.jet5Phi, event.jet5M)
    jet5.HadronFlavour = event.jet5HadronFlavour # simulated true flavour of the jet (5 = b-jet, 4 = c-jet, 0 = light-jet)
    jet5.HiggsMatched = event.jet5HiggsMatched # jet is matched to a b-quark coming from a Higgs boson (1 = matched, 0 = not matched)

    # jet6
    jet6 = ROOT.TLorentzVector()
    jet6.SetPtEtaPhiM(event.jet6Pt, event.jet6Eta, event.jet6Phi, event.jet6M)
    jet6.HadronFlavour = event.jet6HadronFlavour # simulated true flavour of the jet (5 = b-jet, 4 = c-jet, 0 = light-jet)
    jet6.HiggsMatched = event.jet6HiggsMatched # jet is matched to a b-quark coming from a Higgs boson (1 = matched, 0 = not matched)

    # jet7
    jet7 = ROOT.TLorentzVector()
    jet7.SetPtEtaPhiM(event.jet7Pt, event.jet7Eta, event.jet7Phi, event.jet7M)
    jet7.HadronFlavour = event.jet7HadronFlavour # simulated true flavour of the jet (5 = b-jet, 4 = c-jet, 0 = light-jet)
    jet7.HiggsMatched = event.jet7HiggsMatched # jet is matched to a b-quark coming from a Higgs boson (1 = matched, 0 = not matched)

    # jet8
    jet8 = ROOT.TLorentzVector()
    jet8.SetPtEtaPhiM(event.jet8Pt, event.jet8Eta, event.jet8Phi, event.jet8M)
    jet8.HadronFlavour = event.jet8HadronFlavour # simulated true flavour of the jet (5 = b-jet, 4 = c-jet, 0 = light-jet)
    jet8.HiggsMatched = event.jet8HiggsMatched # jet is matched to a b-quark coming from a Higgs boson (1 = matched, 0 = not matched)

    # jet9
    jet9 = ROOT.TLorentzVector()
    jet9.SetPtEtaPhiM(event.jet9Pt, event.jet9Eta, event.jet9Phi, event.jet9M)
    jet9.HadronFlavour = event.jet9HadronFlavour # simulated true flavour of the jet (5 = b-jet, 4 = c-jet, 0 = light-jet)
    jet9.HiggsMatched = event.jet9HiggsMatched # jet is matched to a b-quark coming from a Higgs boson (1 = matched, 0 = not matched)

    # jet10: lowest b-tagging score 
    jet10 = ROOT.TLorentzVector()
    jet10.SetPtEtaPhiM(event.jet10Pt, event.jet10Eta, event.jet10Phi, event.jet10M)
    jet10.HadronFlavour = event.jet10HadronFlavour # simulated true flavour of the jet (5 = b-jet, 4 = c-jet, 0 = light-jet)
    jet10.HiggsMatched = event.jet10HiggsMatched # jet is matched to a b-quark coming from a Higgs boson (1 = matched, 0 = not matched)

    jets.append(jet1)
    jets.append(jet2)
    jets.append(jet3)
    jets.append(jet4)
    jets.append(jet5)
    jets.append(jet6)
    jets.append(jet7)
    jets.append(jet9)
    jets.append(jet10)

    # apply event selection
    for j in jets:
        if j.Pt() < 20 or abs(j.Eta()) > 2.5: continue # go to next element in for loop if jets < 20 GeV or eta > 2.5

    # Once all jets stored, do all the permutations of jets 
    permutations = list(itertools.permutations(jets))
    permutations = [el[:4] for el in permutations] # keep only 4 first jets
    permutations = list(set(permutations)) # remove duplicates in the list

    min_chi2 = 10000000000 # put large value at first

    for permutation in permutations: # try to find Higgs from 2 jets that match their mass, goal is to reconstruct Hbb and Hbb
        h1_tmp = permutation[0] + permutation[1]
        h2_tmp = permutation[2] + permutation[3]
        
        chi2 = 0
        for h in [h1_tmp, h2_tmp]:
            chi2 += (h.M() - 125)**2 
        if chi2 < min_chi2:
            h1 = h1_tmp # first higgs
            j1 = permutation[0] # j1 from h1
            j2 = permutation[1] # j2 from h1

            h2 = h2_tmp # second higgs
            j3 = permutation[2] # j3 from h2
            j4 = permutation[3] # j4 from h2
    
    # reorder Higgs as a function of pT
    higgs = [h1,h2]
    higgs.sort(key=lambda x: x.Pt(), reverse = True)
    h1 = higgs[0]
    h2 = higgs[1]

    # taus
    # tau1: highest pT tau
    tau1 = ROOT.TLorentzVector()
    tau1.SetPtEtaPhiM(event.tau1Pt, event.tau1Eta, event.tau1Phi, event.tau1M)
    
    # tau1: highest pT tau
    tau2 = ROOT.TLorentzVector()
    tau2.SetPtEtaPhiM(event.tau1Pt, event.tau1Eta, event.tau1Phi, event.tau1M)

    h3 = tau1 + tau2 # Htautau

    print(h1.M(), h2.M(), h3.M())

    h1_hist.Fill(h1.M())
    h2_hist.Fill(h2.M())
    h3_hist.Fill(h3.M())

    i+=1
    if i > max_events: break # break for loop
 

# Plot all histograms
# first make plot look a bit better
h1_hist.GetXaxis().SetTitle('m(H) [GeV]')
h1_hist.GetYaxis().SetTitle('Unweighted events')
h1_hist.SetTitle('')
h1_hist.SetStats(0) # remove stat box on the upper right set by default

maxi = 0
for h in [h1_hist,h2_hist,h3_hist]:
    maxi = max(maxi, h.GetMaximum())

for h in [h1_hist,h2_hist,h3_hist]:
    h.SetMaximum(1.8* maxi) # for plotting, make the max y of the plot higher

h1_hist.SetLineColor(ROOT.kRed)
h2_hist.SetLineColor(ROOT.kGreen)
h3_hist.SetLineColor(ROOT.kBlue)

legend = ROOT.TLegend(0.6,0.6,0.9,0.9) # Legend of the plot
legend.SetBorderSize(0)
legend.AddEntry(h1_hist, 'Leading p_{T} Hbb')
legend.AddEntry(h2_hist, 'Subleading p_{T} Hbb')
legend.AddEntry(h3_hist, 'Htautau')

c = ROOT.TCanvas()
h1_hist.Draw('hist e')
h2_hist.Draw('hist e same')
h3_hist.Draw('hist e same')
legend.Draw()
c.RedrawAxis()
c.Update()




