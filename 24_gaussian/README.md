##      Gaussian and Calculating Electronic Structure  

log on to the cluster 

```shell
$ vi ~/.bashrc 

# add the following lines which will allow you to run gaussian 16

module load gaussian/16/RevA                                                         
source ${g16root}/g16/bsd/g16.profile 


```

`source ~/.bashrc`

Afterwards you should be able to access `g16` 

```shell
$ cd $WORK
$ mkdir gaussian
$ cd gaussian 
```

Open another terminal and copy required files 

```shell
$ scp h2o.com coords/* jyesselm@crane.unl.edu:/work/yesselmanlab/jyesselm/gaussian
```

go back to the cluster and run 

```shell
$ g16 < h20.com 
```

if the job ran successfully you should see at the bottom, your quote will be different

```shell
 Leave Link  601 at Mon Nov 18 13:21:24 2019, MaxMem=   104857600 cpu:               0.2 elap:               0.2
 (Enter /util/opt/gaussian/16/RevA/g16/l9999.exe)
 1\1\GINC-LOGIN\FOpt\RHF\6-31G\H2O1\JYESSELM\18-Nov-2019\0\\#p HF/6-31G
  opt\\job title\\0,1\O,-0.4531017092,0.1847446206,0.\H,-0.4702379852,1
 .1342244838,0.\H,0.4363396944,-0.1479691044,0.\\Version=ES64L-G16RevA.
 03\State=1-A'\HF=-75.9853592\RMSD=2.133e-09\RMSF=3.352e-06\Dipole=0.80
 33032,0.5679777,0.\Quadrupole=0.2211144,0.8171336,-1.038248,-0.8427023
 ,0.,0.\PG=CS [SG(H2O1)]\\@


 WE SHOULD BE CAREFUL TO GET OUT OF AN EXPERIENCE ONLY THE WISDOM
 THAT IS IN IT -- AND STOP THERE;
 LEST WE BE LIKE THE CAT THAT SITS DOWN ON A HOT STOVE-LID.
 SHE WILL NEVER SIT DOWN ON A HOT STOVE LID AGAIN;
 BUT ALSO SHE WILL NEVER SIT DOWN ON A COLD ONE ANY MORE.

                                                     -- MARK TWAIN
 Job cpu time:       0 days  0 hours  0 minutes  6.6 seconds.
 Elapsed time:       0 days  0 hours  0 minutes  6.0 seconds.
 File lengths (MBytes):  RWF=      6 Int=      0 D2E=      0 Chk=      1 Scr=      1
 Normal termination of Gaussian 16 at Mon Nov 18 13:21:24 2019.
```

