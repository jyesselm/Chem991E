## Rosetta and protein structure prediction

To get rosetta executables lets use module load again

```shell
# add this to .bashrc
module load rosetta/3.11
```

make sure to `source ~/.bashrc` afterwards. If you were successful when you hit tab after tpying `A` you should now see

```shell
[jyesselm@login.crane ~]$ A
AbinitioRelax.default.linuxgccrelease       AnchoredPDBCreator.default.linuxgccrelease
AnchoredDesign.default.linuxgccrelease      AnchorFinder.default.linuxgccrelease
```

All rosetta programs follow this naming scheme: program name followed by .default.linuxgccrelease 

Now lets go to $WORK and create a new directory 

```shell
$ cd $WORK
$ mkdir rosetta 
$ cd rosetta

# copy the pdb and the two fragment files from your computer to the cluster and put them in this directory
# make a new terminal on your home computer 
$ scp 1l2y.pdb aa1l2yA03_05.200_v1_3 aa1l2yA09_05.200_v1_3 jyesselm@crane.unl.edu:/work/yesselmanlab/jyesselm/rosetta

# after this my directory looks like this
[jyesselm@login.crane rosetta]$ ls
1l2y.pdb  aa1l2yA03_05.200_v1_3  aa1l2yA09_05.200_v1_3
[jyesselm@login.crane rosetta]$ pwd
/work/yesselmanlab/jyesselm/rosetta
```

How to run rosetta's ab initio prediction aglorithm 

```shell
# run of ab initio 3d prediction of this protein
# args 
# -in:file:native the location of the native protein useful for benchmarking the algorithm
# -in:file:frag3 the location of the 3 amino acid fragments 
# -in:file:frag9 the location of the 9 amino acid fragments 
# -out:nstruct the number of predicted structures, i.e. how many times to run prediction 
# -out:file:silent the name of the binary output file
AbinitioRelax.default.linuxgccrelease -in:file:native 1l2y.pdb -in:file:frag3 aa1l2yA03_05.200_v1_3 -in:file:frag9 aa1l2yA09_05.200_v1_3 -out:nstruct 1 -out:file:silent 1l2y_silent.out                                                                                                          
                                                                                            
                                                
   
```

