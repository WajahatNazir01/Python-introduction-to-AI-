:- dynamic yes/1, no/1.

% starting 

recommend :-
    retractall(yes(_)),
    retractall(no(_)),
    pet(Pet),
    write('Recommended Pet: '), write(Pet), nl,
    care(Pet).

% pet rules

pet('Dog') :-
    verify(likes_outdoors),
    verify(has_space),
    verify(has_time),
    !.

pet('Cat') :-
    verify(likes_indoors),
    verify(has_time),
    !.

pet('Bird') :-
    verify(likes_indoors),
    verify(moderate_time),
    !.

pet('Fish') :-
    verify(little_time),
    !.

pet('No Pet') :-
    write('Lifestyle not suitable for keeping a pet.'), nl.

% verification

verify(Condition) :-
    ( yes(Condition) ->
        true
    ; no(Condition) ->
        fail
    ; ask(Condition)
    ).

% Asking questions
ask(Condition) :-
    write('Do you have this condition: '),
    write(Condition),
    write('? (yes/no): '),
    read(Response),
    nl,
    ( Response == yes ->
        assertz(yes(Condition))
    ; assertz(no(Condition)), fail
    ).

% Caring advice
care('Dog') :-
    write('Care Advice: Daily walks, training, and attention required.'), nl.

care('Cat') :-
    write('Care Advice: Clean litter box, regular feeding, and affection.'), nl.

care('Bird') :-
    write('Care Advice: Clean cage, social interaction, and proper diet.'), nl.

care('Fish') :-
    write('Care Advice: Maintain clean tank and proper water temperature.'), nl.

care('No Pet') :-
    write('Advice: Consider improving lifestyle before adopting a pet.'), nl.
