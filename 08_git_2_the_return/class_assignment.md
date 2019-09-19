Create a **private** git repo and put board.txt from `Chem991E/08_git_2_the_return`

You and your partner are going to play two games of tic tac toe through git

the board starts like this

_ _ _                                                                                

_ _ _                                                                                

_ _ _                                                                                

​                                                                                     

_ _ _                                                                                

_ _ _                                                                                

_ _ _   



Player one will make a move on the top board and the other player will make a move on the botom board, i.e.



What is commited from player 1 

_ _ _                                                                                

X _ _                                                                                

_ _ _                                                                                

​                                                                                     

_ _ _                                                                                

_ _ _                                                                                

_ _ _   



What is commited by player 2

_ _ _                                                                                

_ _ _                                                                                

_ _ _                                                                                

​                                                                                     

_ _ _                                                                                

_ _ _                                                                                

_ _ X   



Each player will commit their move on their own branch and than merge it to master. When both players made a move the merged file should look like this:

_ _ _                                                                                

X _ _                                                                                

_ _ _                                                                                

​                                                                                     

_ _ _                                                                                

_ _ _                                                                                

_ _ X   



Continue until both boards are filled or one player wins