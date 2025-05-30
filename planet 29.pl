%Define some facts about planets and their properties
planet(mercury, rocky, small, hot, closest_to_sun).
planet(venus, rocky, small, hot, second_closest_to_sun).

% Define a predicate to look up a planet's properties by name
planet_properties(Name, Type, Size, Temperature, Position) :-
    planet(Name, Type, Size, Temperature, Position).

% Example query: Find the properties of Venus
?- planet_properties(venus, Type, Size, Temperature, Position).
