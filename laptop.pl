:- dynamic yes/1, no/1.

diagnose :-
    retractall(yes(_)),
    retractall(no(_)),
    problem(Problem),
    write('Diagnosis: '), write(Problem), nl,
    solution(Problem).

problem('Battery Issue') :-
    verify(battery_drains_fast),
    verify(not_charging),
    !.

problem('Overheating') :-
    verify(laptop_gets_hot),
    verify(fan_noise),
    !.

problem('Software Crash') :-
    verify(program_crashes),
    verify(system_freezes),
    !.

problem('Hardware Failure') :-
    verify(screen_flicker),
    verify(no_power),
    !.

problem('Unknown Problem') :-
    write('Unable to diagnose the problem.'), nl.

verify(Symptom) :-
    ( yes(Symptom) ->
        true
    ; no(Symptom) ->
        fail
    ; ask(Symptom)
    ).

ask(Symptom) :-
    write('Does the laptop have this symptom: '),
    write(Symptom), write('? (yes/no): '),
    read(Response),
    nl,
    ( Response == yes ->
        assertz(yes(Symptom))
    ; assertz(no(Symptom)), fail
    ).

solution('Battery Issue') :-
    write('Solution: Replace battery or use original charger.'), nl.

solution('Overheating') :-
    write('Solution: Clean fan, apply thermal paste, use cooling pad.'), nl.

solution('Software Crash') :-
    write('Solution: Update OS, reinstall software, scan for malware.'), nl.

solution('Hardware Failure') :-
    write('Solution: Consult technician or replace faulty hardware.'), nl.

solution(_) :-
    write('No solution available.'), nl.
    
:- initialization(diagnose).
