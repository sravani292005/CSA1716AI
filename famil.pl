% Define the family relationships
father(john, alice).
father(john, bob).
mother(mary, alice).
mother(mary, bob).
sister(alice, bob).

% Define a predicate to find the father of someone
find_father(Person, Father) :- father(Father, Person).

% Define a predicate to find the sister of someone
find_sister(Person, Sister) :- sister(Sister, Person).

% Define a predicate to find the parents of someone
find_parents(Person, Father, Mother) :- father(Father, Person), mother(Mother, Person).

% Run the queries
run_queries :-
    find_father(alice, Father),
    write('Father of Alice: '), write(Father), nl,
    find_sister(bob, Sister),
    write('Sister of Bob: '), write(Sister), nl,
    find_parents(alice, Father, Mother),
    write('Parents of Alice: '), write(Father), write(' and '), write(Mother), nl.

% Run the program
:- run_queries.