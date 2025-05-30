% Define symptoms and diseases
symptom(headache).
symptom(fever).
symptom(cough).
symptom(rash).

disease(migraine, [headache, fever]).
disease(measles, [fever, cough, rash]).

% Define a rule to diagnose a disease
diagnose(Disease, Symptoms) :-
    disease(Disease, DiseaseSymptoms),
    subset(Symptoms, DiseaseSymptoms).

% Define a subset rule
subset([], _).
subset([H|T], L) :-
    member(H, L),
    subset(T, L).

% Test cases
test_case_1 :-
    Symptoms = [headache, fever],
    diagnose(Disease, Symptoms),
    write('Test Case 1: Disease is '), write(Disease), nl.

test_case_2 :-
    Symptoms = [fever, cough, rash],
    diagnose(Disease, Symptoms),
    write('Test Case 2: Disease is '), write(Disease), nl.

% Run test cases
run :-
    test_case_1,
    test_case_2.