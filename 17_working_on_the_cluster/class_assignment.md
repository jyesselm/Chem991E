# Class assignment

On the cluster submit the this job to the cluster 

```shell
$ cd $WORK 

$ cat test.sh
#!/bin/bash                                                                
#SBATCH -t 1:00:00
#SBATCH -o output.txt

cd $WORK
echo $RANDOM
hostname

$ sbatch test.sh

# check the jobs status with 
$ squeue -u your_user_name

# when job is complete 
$ cat output.txt 

# email me the contents of the file
```

