## Class assignment

Submit the autodock job 

You are going to parse the test.out

	- Having each MODEL as its own pdb
	- Model_1.pdb, Model_2.pdb for all 5 

Start of MODEL 

```shell
MODEL        1
USER    Run = 1
USER    Cluster Rank = 3
USER    Number of conformations in this cluster = 1
USER  
USER    RMSD from reference structure       = 6.130 A
USER  
USER    Estimated Free Energy of Binding    =   +2.88e+03 kcal/mol  [=(1)+(2)+(3)-(4)]
USER    
USER    (1) Final Intermolecular Energy     =   +2.77e+03 kcal/mol
USER        vdW + Hbond + desolv Energy     =   +2.77e+03 kcal/mol
USER        Electrostatic Energy            =   -1.04 kcal/mol
USER    (2) Final Total Internal Energy     = +102.56 kcal/mol
USER    (3) Torsional Free Energy           =   +4.18 kcal/mol
USER    (4) Unbound System's Energy         =   -2.60 kcal/mol
USER    
USER    
USER  
USER    DPF = ind_hsg1.dpf
USER    NEWDPF move	ind.pdbqt
USER    NEWDPF about	0.368900 -0.214800 -4.986500
USER    NEWDPF tran0	0.951195 5.387857 -12.132618
USER    NEWDPF axisangle0	0.896408 -0.076726 -0.436539 169.080748
USER    NEWDPF quaternion0	0.892341 -0.076378 -0.434558 0.095144
USER    NEWDPF dihe0	-72.84 -179.31 139.01 105.16 -96.54 -113.72 0.89 -31.40 180.00 -138.02 127.19 -158.25 -119.83 175.51 
USER 
ATOM      1  C11 IND I 201       2.280   5.245 -10.856 -0.26 -0.07    +0.136     6.130
ATOM      2  C10 IND I 201       1.530   5.610  -9.574 -0.28 -0.08    +0.149     6.130
ATOM      3  N3  IND I 201       2.381   5.778  -8.415 -0.05 +0.23    -0.395     6.130
ATOM      4  C8  IND I 201       3.665   6.390  -8.839 -0.29 -0.05    +0.148     6.130
ATOM      5  C9  IND I 201       4.768   6.494  -7.806 +0.44 -0.10    +0.292     6.130
ATOM      6  N1  IND I 201       4.846   5.457  -6.877 -0.32 -0.07    +0.096     6.130
ATOM      7  C1  IND I 201       3.459   5.156  -6.430 -0.19 -0.26    +0.307     6.130
ATOM      8  C2  IND I 201       2.407   4.664  -7.403 -0.28 -0.22    +0.200     6.130
ATOM      9  C31 IND I 201       5.864   5.640  -5.835 +7.72 -0.17    +0.312     6.130
ATOM     10  C32 IND I 201       5.637   6.593  -4.657 -0.30 +0.00    -0.013     6.130
ATOM     11  C33 IND I 201       6.593   6.811  -3.654 +0.15 -0.03    +0.125     6.130
ATOM     12  N5  IND I 201       6.466   7.681  -2.559 +0.15 +0.01    -0.273     6.130
ATOM     13  C34 IND I 201       5.233   8.330  -2.583 +0.28 +0.00    +0.116     6.130
ATOM     14  C35 IND I 201       4.237   8.160  -3.550 -0.41 -0.00    +0.020     6.130
ATOM     15  C36 IND I 201       4.442   7.276  -4.608 -0.45 -0.00    +0.012     6.130
ATOM     16  C3  IND I 201       1.107   4.513  -6.659 -0.28 -0.27    +0.242     6.130
ATOM     17  N2  IND I 201       0.348   3.485  -6.982 +2.98 +0.82    -0.351     6.130
ATOM     18  H4  IND I 201       0.755   2.849  -7.683 +4.43 -0.72    +0.163     6.130
ATOM     19  O1  IND I 201       0.798   5.316  -5.787 -0.19 +0.16    -0.271     6.130
ATOM     20  C4  IND I 201      -0.950   3.112  -6.517+22.47 -0.04    +0.022     6.130
ATOM     21  C5  IND I 201      -1.052   3.580  -5.053+99.99 -0.02    +0.037     6.130
ATOM     22  C6  IND I 201      -1.196   1.753  -6.609+99.99 -0.09    +0.037     6.130
ATOM     23  C7  IND I 201      -2.041   3.812  -7.203 +3.67 -0.04    +0.037     6.130
ATOM     24  O2  IND I 201       3.544   5.238 -10.264 -0.13 +0.21    -0.394     6.130
ATOM     25  H21 IND I 201       3.451   5.042  -9.258 +0.13 -0.15    +0.210     6.130
ATOM     26  C12 IND I 201       2.101   3.917 -11.613+25.84 -0.05    +0.047     6.130
ATOM     27  C13 IND I 201       1.227   2.796 -11.035+14.42 -0.09    +0.084     6.130
ATOM     28  C14 IND I 201      -0.229   3.242 -10.824 +0.85 -0.05    +0.052     6.130
ATOM     29  C15 IND I 201      -1.076   2.165 -10.251+11.42 +0.09    -0.057     6.130
ATOM     30  C16 IND I 201      -1.013   0.844 -10.695+99.99 -0.01    +0.007     6.130
ATOM     31  C17 IND I 201      -1.851  -0.123 -10.157+31.89 -0.00    +0.001     6.130
ATOM     32  C18 IND I 201      -2.758   0.250  -9.163+99.99 -0.00    +0.000     6.130
ATOM     33  C19 IND I 201      -2.819   1.573  -8.710+99.99 -0.00    +0.001     6.130
ATOM     34  C20 IND I 201      -1.970   2.535  -9.261+30.20 -0.01    +0.007     6.130
ATOM     35  C21 IND I 201       1.239   1.550 -11.912+69.84 -0.10    +0.222     6.130
ATOM     36  N4  IND I 201       1.974   1.638 -13.017+40.70 +0.24    -0.350     6.130
ATOM     37  H32 IND I 201       2.283   2.565 -13.343 -0.01 -0.15    +0.163     6.130
ATOM     38  O3  IND I 201       0.685   0.507 -11.533+62.53 +0.03    -0.273     6.130
ATOM     39  C22 IND I 201       2.355   0.457 -13.775 +0.12 -0.03    +0.147     6.130
ATOM     40  C23 IND I 201       1.268  -0.605 -13.757 +3.12 +0.01    +0.149     6.130
ATOM     41  C24 IND I 201       1.982  -1.908 -14.037+84.08 +0.02    +0.073     6.130
ATOM     42  C25 IND I 201       3.389  -1.869 -13.497+93.96 +0.02    -0.047     6.130
ATOM     43  C30 IND I 201       3.605  -0.340 -13.319 +5.55 +0.01    -0.027     6.130
ATOM     44  C26 IND I 201       4.361  -2.776 -13.143+99.99 +0.00    +0.008     6.130
ATOM     45  C29 IND I 201       4.811   0.029 -12.812+44.77 -0.00    +0.010     6.130
ATOM     46  C28 IND I 201       5.777  -0.908 -12.473+99.99 -0.00    +0.001     6.130
ATOM     47  C27 IND I 201       5.565  -2.288 -12.626+99.99 +0.00    +0.001     6.130
ATOM     48  O4  IND I 201       0.578  -0.581 -12.517 +3.55 +0.04    -0.393     6.130
ATOM     49  H35 IND I 201       1.069  -1.181 -11.838 +0.07 -0.05    +0.210     6.130
TER
ENDMDL
```



Submit your parsing file and the pdbs 

