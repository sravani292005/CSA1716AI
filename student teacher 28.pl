% Define some facts about teachers and their subject codes
teaches(john, math).
teaches(jane, english).
teaches(bob, science).
teaches(sue, history).
teaches(tom, art).

% Define some facts about students and the subjects they are taking
takes(alice, math).
takes(alice, science).
takes(bob, english).
takes(bob, science).
takes(carol, history).
takes(carol, art).
takes(dave, math).
takes(dave, english).
takes(dave, art).

% Define a predicate to look up the subject codes taught by a teacher
teaching_subjects(Teacher, Subjects) :- findall(Subject, teaches(Teacher, Subject), Subjects).

% Define a predicate to look up the students taking a given subject
taking_students(Subject, Students) :- findall(Student, takes(Student, Subject), Students).