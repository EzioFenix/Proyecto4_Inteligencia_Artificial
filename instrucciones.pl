//Definir operaciones//

:-op(1,fx,neg).
:-op(2,xfy,or).
:-op(2,xfy,and).
:-op(2,xfy,imp).
:-op(2,xfy,dimp).

//Win Condition
sq(G,D):-
sq([F],[F]).

//Debilitamiento
sq([F|G],D):- atom(F),
sq(G,D).

sq(G,[F|D]):- atom(F),
sq(G,D).

//Negacion
sq([neg F|G],D):-
sq(G,[F|D]),
//write(Archivo,"\neg"+G).

sq(G,[neg F|D]):-
sq([F|G],D).

//Disyuncion
sq([F or R|G],D):-
sq([F|G],D),
sq([R|G],D).

sq(G,[F or R|D]):-
append([F,R],D,U),
sq(G,U).

//Conjuncion
sq([F and R|G],D):-
append([F,R],G,U),
sq(U,D).

sq(G,[F and R|D]):-
sq(G,[F|D]),
sq(G,[R|D]).

//Implicacion
sq([F imp R|G],D):-
sq(G,[F|D]),
sq([R|G],D).

sq(G,[F imp R|D]):-
sq([F|G],[R|D]).

//Doble Implicacion
sq([F dimp R|G],D):-
append([F,R],D,U),
sq(G,U),
append([F,R],G,U),
sq(U,D).

sq(G,[F dimp R|D]):-
sq([F|G],[R|D]),
sq([R|G],[F|D]).