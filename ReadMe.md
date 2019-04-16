### Project: This is a code interview

**Problem：**

Agu is a cursed place with conflicts of sources between tribes. To avoid the  invasion of another tribe, every tribe starts to build their moat. 

- What is a tribe like.

  Agu is a square of $n*m$ grids. Every tribe occupys several grids, for example:

  ​	. . a b . .

  ​	. . c . d .	

  ​	. . .  . . .

  $abcd$ compose a tribe, where $a$ and $b$ is connected horizontally, $a$ and $c$ is connected vertically, and $b$ and $d$ is connected diagonally. More importantly, there's no such tribe of which grids have unoccupied grids

​	surrounded, such as:

​		. . a b c . . . 

​		. d . .  e . . . 	

​		. . f  g .  . . . 

- The length of the moat

  In principle, every tribe would build their moat as short as possiple for those exposed sides of grids, which means no gird share side with it. For example:

  ​	.  .  . . . .

  ​	. a b . . .

  ​	. c . d . . 

  ​	.  . . .  . .

  $abcd$ is a tribe with 16 sides($a$, $b$, $c$, $d$ have four sides), in which the number of exposed is 12. Each exposed side need 1 unit length of moat, therefore the length of the moat needed is 12.

**Function Description:**

Given the coordinate of a gride$(a, b)$, compute the length of the tribe's moat that the grid belongs to.

**Input Format:**

The firt line contains 4 integers $n, m, a, b$,  the size of Agu and the coordinates of given grid.

Following is an $n*m$ array that represents Agu, in which "." means an unoccupied grid, "#" means an occupied grid.

Constrains

- $n \geq 1​$
- $m\leq 100$
- $1\leq a \leq n$
- $1 \leq b\leq n$

**Output Format:**

Return the integer minimum length of the moat.

**Sample Input:** 

- Sample 1

  4  6  3  4

  . .  .  . . . 

  . # # . . .

  . # . # . .	

  . . .  . . .

- Sample 2

  6  4  2  3

  . # # #

  . # # #

  . # # #

  . .  .  #

  . .  # .

  \# . . .

- Sample 3

  5  6  1  3

  . # # # # .

  \# . .  .  . #

  . . # #  . #

  . # . .   . #

  . . # # # .



**Sample Output:**

- Sample 1

  12

- Sample 2

  18

- Sample 3

  40

### Install 

This project requires python 3 with scikit-learn, scipy, numpy installed.

