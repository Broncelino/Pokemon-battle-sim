# Pokemon-battle-sim
A basic simulator of a pokemon battle in python

#how to play
Start by typing the name of the pokemon each player would like to use.
Pokemon choices and their moves will appear when the program first runs.
The faster pokemon goes first, the player will then type the name of the move they want to use.
Effectiveness, damage, and opponent's remaining health will all be displayed.
The other player takes their turn and then it repeats until one pokemon's health is reduced to 0.

#how it works
There are 2 class types that the game is based around called Pokemon and Move.
The Pokemon class contains the name, stats, types, and moves of the Pokemon.
The move class contains the name of the move, its damage, its accuracy, its elemental type, and whether it's a physical or special move.
After the players choose their pokemon the speed stats are checked and the faster pokemon is declared as first.
The damage calculation uses the attack stat of the attacking pokemon and the defence stat of the defending one
along with a number of other bonuses like a random damage modifier roll of .85-1, a buff of 1.5x increase if the pokemon has the same type as the move,
and a 1/16 chance to get a critcal hit and do 1.5x damage.
