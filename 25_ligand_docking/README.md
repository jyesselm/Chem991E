## Ligand Docking with AutoDock 4

System: HIV Protease and inhibitor

![](img/01.jpg)



How to setup the protein and ligand files. There are command line tools that you can download here:

http://mgltools.scripps.edu/downloads/previous-releases/mgltools-1-5.4/mgltools-1-5.4

Useful links

http://autodock.scripps.edu/faqs-help/how-to/how-to-prepare-a-ligand-file-for-autodock4

http://autodock.scripps.edu/faqs-help/how-to/how-to-prepare-a-receptor-file-for-autodock4

http://autodock.scripps.edu/faqs-help/how-to/how-to-prepare-a-grid-parameter-files-for-autogrid4

http://autodock.scripps.edu/faqs-help/how-to/how-to-prepare-a-docking-parameter-file-for-autodock4-1

```shell
# using the mgltools python scripts we can create all the necessary docking files. I have provided these for you 
# in directory: mgltools_i86Darwin9_1.5.6/MGLToolsPckgs/AutoDockTools/Utilities24/
$ pythonsh prepare_ligand4.py -l ind.pdb
$ pythonsh prepare_receptor4.py -r hsg1.pdb
$ pythonsh prepare_gpf4.py -r hsg1.pdb -l ind.pdb 
$ pythonsh prepare_dpf4.py -r hsg1.pdb -l ind.pdb 
```

### running autodock4

What are the files?

Both hsg1.pdbqt and ind.pdbqt are basically enhanced pdb files with charge and atom types

```shell
$ cat hsg1.pdbqt
REMARK   4 XXXX COMPLIES WITH FORMAT V. 2.0                                          
ATOM      1  N   PRO A   1      -5.322 -15.656 -12.341  1.00 38.10    -0.062 N       
ATOM      2  HN1 PRO A   1      -4.966 -15.751 -11.390  1.00  0.00     0.278 HD      
ATOM      3  HN2 PRO A   1      -5.934 -16.471 -12.304  1.00  0.00     0.278 HD      
ATOM      4  CA  PRO A   1      -4.275 -15.710 -13.408  1.00 40.62     0.277 C       
ATOM      5  C   PRO A   1      -2.894 -15.457 -12.807  1.00 42.64     0.249 C       
ATOM      6  O   PRO A   1      -2.786 -15.054 -11.648  1.00 43.40    -0.271 OA      
ATOM      7  CB  PRO A   1      -4.563 -14.653 -14.478  1.00 37.87     0.044 C  
```

And hsg1.gpf is the parameters for making the grid 

```shell
cat hsg1.gpf 
npts 60 60 60                        # num.grid points in xyz                        
gridfld hsg1.maps.fld                # grid_data_file                                
spacing 0.375                        # spacing(A)                                    
receptor_types A C HD N OA SA        # receptor atom types                           
ligand_types A C HD N NA OA SA       # ligand atom types                             
receptor hsg1.pdbqt                  # macromolecule                                 
gridcenter 2.5 6.5 -7.5              # xyz-coordinates or auto                       
smooth 0.5                           # store minimum energy w/in rad(A)              
map hsg1.A.map                       # atom-specific affinity map                    
map hsg1.C.map                       # atom-specific affinity map                    
map hsg1.HD.map                      # atom-specific affinity map                    
map hsg1.N.map                       # atom-specific affinity map                    
map hsg1.NA.map                      # atom-specific affinity map                    
map hsg1.OA.map                      # atom-specific affinity map                    
map hsg1.SA.map                      # atom-specific affinity map                    
elecmap hsg1.e.map                   # electrostatic potential map                   
dsolvmap hsg1.d.map              # desolvation potential map                         
dielectric -0.1465                   # <0, AD4 distance-dep.diel;>0, constant   
```

Setup

```shell
vi ~/.bashrc 
# add 
module load autodock/4.2

# then source 
source ~/.bashrc

cd $WORK 
mkdir autodock
cd autodock

# copy hsg1.gpf hsg1.pdbqt ind.pdbqt to the cluster 
scp ind_hsg1.dpf hsg1.gpf hsg1.pdbqt ind.pdbqt jyesselm@crane.unl.edu:/work/yesselmanlab/jyesselm/autodock


```

Generating the grids

```shell
# hsg1.glg is the log file
$ autogrid4 -p hsg1.gpf -l hsg1.glg

$ tail hsg1.glg
 6       OA        -1.05         2.00e+05
 7       e        -39.67         1.47e+01       Electrostatic Potential
 8       d          0.00         1.46e+00       Desolvation Potential


 * Note:  Every pairwise-atomic interaction was clamped at 100000.00


autogrid4: Successful Completion.
Real= 3.57s,  CPU= 3.43s,  System= 0.11s

$ls 
hsg1.A.map  hsg1.C.map  hsg1.d.map  hsg1.e.map  hsg1.glg  hsg1.gpf  hsg1.HD.map  hsg1.maps.fld  hsg1.maps.xyz  hsg1.NA.map  hsg1.N.map  hsg1.OA.map  hsg1.pdb  hsg1.pdbqt  ind.pdbqt
```

Running autodock

```shell
# test.out is the log file
autodock4 -p ind_hsg1.dpf -l test.out

cat test.out
USER                              x       y       z    vdW   Elec        q     RMS
ATOM      1  C11 IND I 201      -0.399   2.207  -9.380+99.99 -0.70    +0.136     4.544
ATOM      2  C10 IND I 201       0.978   2.155  -8.718+99.99 -0.73    +0.149     4.544
ATOM      3  N3  IND I 201       0.985   2.562  -7.328+35.42 +1.62    -0.395     4.544
ATOM      4  C8  IND I 201       2.027   3.599  -7.131 -0.40 -0.27    +0.148     4.544
ATOM      5  C9  IND I 201       2.319   4.040  -5.711 -0.26 -0.35    +0.292     4.544
ATOM      6  N1  IND I 201       2.219   3.058  -4.725+14.81 -0.13    +0.096     4.544
ATOM      7  C1  IND I 201       0.984   2.275  -5.003+99.99 -0.44    +0.307     4.544
ATOM      8  C2  IND I 201       0.823   1.487  -6.287+99.99 -0.80    +0.200     4.544
ATOM      9  C31 IND I 201       2.413   3.542  -3.354+99.99 -0.41    +0.312     4.544
ATOM     10  C32 IND I 201       2.421   5.041  -3.029 -0.26 +0.01    -0.013     4.544
ATOM     11  C33 IND I 201       1.820   5.578  -1.881 -0.23 -0.04    +0.125     4.544
ATOM     12  N5  IND I 201       1.803   6.931  -1.507 -0.12 +0.07    -0.273     4.544
ATOM     13  C34 IND I 201       2.480   7.711  -2.444 +0.04 -0.03    +0.116     4.544
ATOM     14  C35 IND I 201       3.099   7.242  -3.606 -0.33 -0.00    +0.020     4.544
ATOM     15  C36 IND I 201       3.071   5.882  -3.906 -0.28 -0.00    +0.012     4.544
ATOM     16  C3  IND I 201      -0.546   0.863  -6.292+99.99 -0.63    +0.242     4.544
ATOM     17  N2  IND I 201      -0.775  -0.074  -7.192+99.99 +0.39    -0.351     4.544
ATOM     18  H4  IND I 201       0.039  -0.324  -7.771+99.99 -0.51    +0.163     4.544
ATOM     19  O1  IND I 201      -1.389   1.217  -5.476+99.99 +0.22    -0.271     4.544
ATOM     20  C4  IND I 201      -1.971  -0.795  -7.491+99.99 -0.00    +0.022     4.544
ATOM     21  C5  IND I 201      -1.830  -1.313  -8.935+99.99 -0.01    +0.037     4.544
ATOM     22  C6  IND I 201      -3.119  -0.031  -7.362+26.81 -0.03    +0.037     4.544
ATOM     23  C7  IND I 201      -2.144  -2.004  -6.681+99.99 -0.03    +0.037     4.544
ATOM     24  O2  IND I 201      -1.006   2.930  -8.353+99.99 +2.31    -0.394     4.544
ATOM     25  H21 IND I 201      -0.369   3.674  -8.034 +0.02 -0.63    +0.210     4.544
ATOM     26  C12 IND I 201      -0.694   2.928 -10.708 +4.73 -0.05    +0.047     4.544
ATOM     27  C13 IND I 201       0.129   4.152 -11.134 -0.41 -0.05    +0.084     4.544
ATOM     28  C14 IND I 201      -0.405   5.457 -10.520 -0.37 -0.02    +0.052     4.544
```





