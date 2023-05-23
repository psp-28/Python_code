import random

action = ['''           __,,,__
                ,-""-,-"       "-,-""-,
               /,-' , .-'-.7.-'-. , '-,\
               \(    /  _     _  \    )/
                '-,  { (0)   (0) }  ,-'
                 /    >  .---.  <    \
                |/ .-'   \___/   '-. \|
                {, /  ,_       _,  \ ,}
                \ {,    \     /    ,} /
                 ',\.    '---'    ./,'
             _.-""""""-._     _.-""""""-._
           .'            `._.`            '.
         _/_               _                \
      .'`   `\            | |                \
     /        |           | |                 ;
     |        /           |_|                 |
     \  ;'---'    _    ___  _  _  ___         ;
      '. ;       | |  /   \| || ||  _|     _ ;
        `-\      | |_ | | || |/ /|  _|   .' `,
           `\    |___|\___/ \__/ |___|  |     \
             \            _ _           \     |
            `\         | | |         /`   _/
    ,-""-.    .'`\       | | |       /`-,-'` .-""-,
   /      `\.'    `\     \___/     /`    './`      \
  ;  .--.   \       '\           /'       /   .--.  ;
  | (    \   |,       '\       /'        |   /    ) |
   \ ;    }             ;\   /;         `   {    ; /
    `;\   \         _.-'  \ /  `-._         /   /;`
      \ \__.'   _.-'       Y       `-._    '.__//
       '.___,.-'                       `-.,___.'

''', ''' @@@@@@@@@@@@@@@@@@@@@@@@@@@@@,""""""@@@@@@@@@@@@
          @@@@@@@@@@@@"-    "@@@@@@@@@@       "@@@@@@@@@@@
          @@@@@@@@@@@(   ^^^ )@@@@@@@@@      ' @@@@@@@@@@@
          @@@@@@@@@@@(  (    0@@@@@@@@@,      (@@@@@@@@@@@
          @@@@@@@@@@@)  )  _/@@@@@@@@@@@m       "@@@@@@@@@
          @@@@@@@@@@(__/  (@@@@@@@@@@@@@'         @@@@@@@@
          @@@@@@@@@@"       )@@@@@@@@@@'          @@@@@@@@
          @@@@@@@@@'         \@@@@@@@@'           @@@@@@@@
          @@@@@@@@@'          )@@@@@@'   A        @@@@@@@@
          @@@@@@@@@         ,@@@@@@@"  /@@        @@@@@@@@
          @@@@@@@@@,        @_____"  =,           @@@@@@@@
          @@@@@@@@@@               :',@@@@        `@@@@@@@
          @@@@@@@@@'       @@@@@@@@@@@@@@@         M@@@@@@
          @@@@@@@@'        `@@@@@@@@@@@@@"        ,@@@@@@@
          @@@@@@@@          @@@@@@@@@@@@"      /  @@@@@@@@
          @@@@@@@@          @@@@@@@@@@@"          @@@@@@@@
          @@@@@@@@|         @@@@@@@@@@"      /    @@@@@@@@
          @@@@@@@@|         @@@@@@@@@"     ,"    .@@@@@@@@
          @@@@@@@@|         @@@@@@@@'    .@@     `@@@@@@@@
          @@@@@@@@|         @@@@@@@@m    `@@@,    @@@@@@@@
          @@@@@@@@|        :@@@@@@@@@m    )@@.   )@@@@@@@@''', '''88                                     
88                                     
88                                     
88  ,adPPYba,  8b       d8  ,adPPYba,  
88 a8"     "8a `8b     d8' a8P_____88  
88 8b       d8  `8b   d8'  8PP"""""""  
88 "8a,   ,a8"   `8b,d8'   "8b,   ,aa  
88  `"YbbdP"'      "8"      `"Ybbd8"'  ''']





print(random.choice(action))



print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


concat = name1 + name2

lowercase = concat.lower()


#getting the occurance of the letter "true love" in the names using count()
t = lowercase.count("t")
r = lowercase.count("r")
u = lowercase.count("u")
e = lowercase.count("e")


l = lowercase.count("l")
o = lowercase.count("o")
v = lowercase.count("v")
e = lowercase.count("e")



true = t + r + u + e
love = l + o + v + e 


# add both the strings count
true_love = str(true)  + str(love) 

int_score = int(true_love)

if (int_score < 10) and (int_score > 90):
    print(f"Your score is {int_score}, you go together like coke and mentos.")

elif (int_score >= 40) and (int_score <= 50):
    print(f"Your score is {int_score}, you are alright together.")

else:
    print(f'Your score is {int_score}.')