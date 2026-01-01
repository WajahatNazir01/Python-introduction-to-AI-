:- dynamic yes/1, no/1.

find :-
    retractall(yes(_)),
    retractall(no(_)),
    write('Welcome to Pet Recommendation System'), nl,
    pet(Pet),
    write('Your suitable pet is: '),
    write(Pet), nl,
    care(Pet).

% --------------------
% Pet Rules
% --------------------

pet('Dog') :-
    verify(has_place),
    verify(love_bark),
    !.

pet('Snake') :-
    verify(have_sand),
    verify(love_poison),
    !.

pet('No Pet') :-
    write('No suitable pet found.'), nl.

% --------------------
% Verification Logic
% --------------------

verify(Sym) :-
    ( yes(Sym) ->
        true
    ; no(Sym) ->
        fail
    ; ask(Sym)
    ).

ask(Sym) :-
    write('Answer in yes/no: '),
    write(Sym), write(' ? '),
    read(Response),
    nl,
    ( Response == yes ->
        assertz(yes(Sym))
    ; assertz(no(Sym)), fail
    ).

% --------------------
% Care Advice
% --------------------

care('Dog') :-
    write('Care: Take dog for walk and feed daily.'), nl.

care('Snake') :-
    write('Care: Handle carefully and provide proper habitat.'), nl.

care('No Pet') :-
    write('Advice: Improve lifestyle before adopting a pet.'), nl.

initialize :- find.