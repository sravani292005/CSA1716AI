% Allow dynamic modification of facts
:- dynamic fact/1.

% Facts: Initial known truths
fact(raining).
fact(cloudy).

% Rules: New facts derived from existing ones
rule(wet_ground, raining).
rule(take_umbrella, cloudy).

infer(Fact) :- 
    rule(Fact, Condition), 
    fact(Condition), 
    assertz(fact(Fact)),  % Add new fact dynamically
    write('Derived new fact: '), writeln(Fact).

% Example Queries:
% ?- infer(wet_ground).
% ?- infer(take_umbrella).
% ?- infer(sunny). % Will fail since no rule supports it