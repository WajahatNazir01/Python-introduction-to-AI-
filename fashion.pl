:- dynamic yes/1, no/1.

/* ===== START SYSTEM ===== */

go :-
    hypotheses(Outfit),
    write('==================================='), nl,
    write(' Recommended Outfit: '), nl,
    write('==================================='), nl,
    write(Outfit), nl,
    undo.

/* ===== POSSIBLE CONCLUSIONS ===== */

hypotheses('Formal Shirt + Trousers + Leather Shoes') :-
    formal_male_hot, !.

hypotheses('Kurta Shalwar + Waistcoat') :-
    wedding_male, !.

hypotheses('T-Shirt + Jeans + Sneakers') :-
    casual_young, !.

hypotheses('Abaya / Long Dress') :-
    formal_female, !.

hypotheses('No suitable outfit found. Try changing preferences.').

/* ===== RULES ===== */

formal_male_hot :-
    verify(male),
    verify(formal),
    verify(hot_weather),
    verify(medium_budget).

wedding_male :-
    verify(male),
    verify(wedding),
    verify(traditional).

casual_young :-
    verify(casual),
    verify(young),
    verify(low_budget).

formal_female :-
    verify(female),
    verify(formal),
    verify(elegant).

/* ===== VERIFY FACTS ===== */

verify(S) :-
    ( yes(S) ->
        true
    ; no(S) ->
        fail
    ; ask(S)
    ).

ask(Question) :-
    write('Is the following true? '), nl,
    write('-> '), write(Question), write(' ? (y/n) '),
    read(Response), nl,
    ( Response == y ->
        assert(yes(Question))
    ; assert(no(Question)), fail
    ).

/* ===== CLEAR MEMORY ===== */

undo :-
    retract(yes(_)), fail.
undo :-
    retract(no(_)), fail.
undo.
