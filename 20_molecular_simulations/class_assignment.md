## class assignment 

Goal: Run 5 production run jobs using a submission script 

1) write a submission script that will create a runs/ directory and individal job directories which you can take from last assignment 

2) Have each job run for a max of 12 hours

3) each job must run:

```shell
gmx grompp -f md.mdp -c npt.gro -t npt.cpt -p topol.top -o md_0_1.tpr
gmx mdrun -deffnm md_0_1
```

but remember that you will be two directories deeper so you need to change the above commands to reflect that. 