bfs(Start, Goal, Path) :-
bfs([Start], Goal, Path, []).

bfs([[Node|Nodes]|_], Node, [Node|Nodes], _) :-
!.

bfs([Path|Paths], Goal, NewPath, Visited) :-
findall(Next, (arc(Path, Next), + member(Next, Visited)), NextNodes),
(   NextNodes = [],
fail
;   append(Paths, NextNodes, NewPaths),
bfs(NewPaths, Goal, NewPath, [Path|Visited])
).

arc(0, 1).
arc(0, 2).
arc(0, 3).
arc(1, 4).
arc(1, 5).
arc(2, 6).
arc(2, 7).
arc(3, 8).
arc(8, 9).
arc(8, 10).
arc(9, 11).
arc(9, 12).
arc(9, 13).

?- bfs(0, 13, Path).