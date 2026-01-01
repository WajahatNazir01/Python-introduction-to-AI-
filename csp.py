
# Jobs = ['J1', 'J2', 'J3']
# Workers = ['W1', 'W2', 'W3']
# Constraints = {
#     'W1': ['J3'],
#     'W2': ['J1'],
#     'W3': []
# }

# # FIX 2: Corrected signature to accept 'worker'
# def is_valid(assignment, worker, job):
#     # FIX 1: Used .get() on Constraints and the correct 'worker' variable
#     if job in Constraints.get(worker, []):
#         return False
#     if job in assignment.values():
#         return False
#     # Simplified the logic, 'else' is redundant here
#     return True

# # FIX 7: Retained global Workers reference for simplicity, but corrected variable names
# def back_track(assignment, workers_list, jobs, solutions):
#     if len(assignment) == len(Workers): # Using the global list 'Workers' for length check
#         solutions.append(assignment.copy())
#         return 
    
#     # FIX 3: Used square bracket notation [] for list access
#     worker = Workers[len(assignment)]
    
#     for job in jobs:
#         # FIX 4: Passed the single 'job' string instead of the list 'jobs'
#         if is_valid(assignment, worker, job):
#             # FIX 5: Used assignment operator '=' instead of comparison operator '=='
#             assignment[worker] = job
            
#             # Passed the correct arguments to the recursive call
#             back_track(assignment, workers_list, jobs, solutions)
            
#             del assignment[worker]
    
   
# def all_solutions(workers, jobs):
#     soln = []
#     assignment = {}
#     # We pass the local 'soln' list, which will be filled by backtrack
#     back_track(assignment, workers, jobs, soln)
#     # FIX 6: Returned the list of solutions (soln) instead of the input list (workers)
#     return soln

# # --- Execution ---
# solutions = all_solutions(Workers, Jobs)

# if solutions:
#     print("All possible solutions:")
#     for sol in solutions:
#         print(sol)
# else:
#     print("No solution exist")

WORKER = ['W1', 'W2', 'W3']
JOBS = ['J1', 'J2', 'J3']

CONSTRAINTS = {
    'W1': ['J3'],
    'W2': ['J1'],
    'W3': []
}

def assign_jobs(assignment):
    # If all workers are assigned jobs
    if len(assignment) == len(WORKER):
        print("Solution:", assignment)
        return

    # Select next worker
    worker = WORKER[len(assignment)]

    for job in JOBS:
        # Check job is not already assigned and not forbidden
        if job not in assignment.values() and job not in CONSTRAINTS[worker]:
            assignment[worker] = job
            assign_jobs(assignment)   # Recursive call
            del assignment[worker]    # Backtrack

# Start with empty assignment
assign_jobs({})
