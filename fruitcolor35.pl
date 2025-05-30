% Define the possible fruits and their colors 
fruit(apple, red).
fruit(banana, yellow). 
fruit(grape, purple). 
fruit(orange, orange). 
fruit(watermelon, green).
% Define a predicate to match a fruit with its color 
match_fruit_color(Fruit, Color) :-
fruit(Fruit, Color).
