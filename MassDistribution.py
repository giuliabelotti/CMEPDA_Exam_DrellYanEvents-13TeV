
import ROOT
import ParticleSelection

def MassDistribution(file_name, Tree_name, particle):
    """ Mass distribution in three representative bins in rapidity
    
        Parameters:
            file_name : string
                The name of the file '.root'
            Tree_name : string
                The name of the TTree 
            particle : string
                The name of the particle 
                
        Returns:
            Three histograms, one for each rapidity region    
    """
    df = ROOT.RDataFrame(Tree_name, file_name)
    
    ROOT.gInterpreter.ProcessLine('#include "Vector_Library.h"')
  
    if(particle == 'Muon'): 
        df = df.Define("p1","Vector(Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_mass[0])")
        df = df.Define("p2","Vector(Muon_pt[1], Muon_eta[1], Muon_phi[1], Muon_mass[1])")
        df = df.Define("DiMuon_Mass", "invMass(p1,p2)")
        df = df.Define("y", "Rapidity(p1,p2)")
        
    elif(particle == 'Electron'):
        df = df.Define("p1","Vector(Electron_pt[0], Electron_eta[0], Electron_phi[0], Electron_mass[0])")
        df = df.Define("p2","Vector(Electron_pt[1], Electron_eta[1], Electron_phi[1], Electron_mass[1])")       
        df = df.Define("DiElectron_Mass", "invMass(p1,p2)")
        df = df.Define("y", "Rapidity(p1,p2)")       

    
    df_0_y_04 = df.Filter("abs(y)>0 && abs(y)<0.4", "Range Rapidity")
    df_08_y_12 = df.Filter("abs(y)>0.8 && abs(y)<1.2", "Range Rapidity")
    df_16_y_2 = df.Filter("abs(y)>1.6 && abs(y)<2.0", "Range Rapidity") 

    
    if(particle == 'Muon'): 
        h_0_y_04 = df_0_y_04.Histo1D(("DiMuon_Mass1","Invariant Mass",60,60,120),"DiMuon_Mass")
        h_08_y_12 = df_08_y_12.Histo1D(("DiMuon_Mass2","Invariant Mass",60,60,120),"DiMuon_Mass")
        h_16_y_2 = df_16_y_2.Histo1D(("DiMuon_Mass3","Invariant Mass",60,60,120),"DiMuon_Mass")
    
    elif(particle == 'Electron'):
        h_0_y_04 = df_0_y_04.Histo1D(("DiElectron_Mass","Invariant Mass",60,60,120),"DiElectron_Mass")
        h_08_y_12 = df_08_y_12.Histo1D(("DiElectron_Mass","Invariant Mass",60,60,120),"DiElectron_Mass")
        h_16_y_2 = df_16_y_2.Histo1D(("DiELectron_Mass","Invariant Mass",60,60,120),"DiElectron_Mass")
    
    
    return h_0_y_04, h_08_y_12, h_16_y_2















