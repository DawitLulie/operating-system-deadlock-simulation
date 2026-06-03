def calculate_need(max_matrix, allocation_matrix):
    n = len(max_matrix) # number of process
    m = len(max_matrix[0]) # number of resources

    need = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(max_matrix[i][j] - allocation_matrix[i][j])
        need.append(row)

    return need


def is_safe(available, max_matrix, allocation_matrix):
    n = len(max_matrix)
    m = len(available)

    need = calculate_need(max_matrix, allocation_matrix)

    finish = [False] * n
    safe_sequence = []
    work = available.copy()

    while len(safe_sequence) < n:
        found = False

        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(m)):
                    for j in range(m):
                        work[j] += allocation_matrix[i][j]

                    safe_sequence.append(i)
                    finish[i] = True
                    found = True

        if not found:
            return False, []

    return True, safe_sequence


def request_resources(process_id, request, available, max_matrix, allocation_matrix):
    need = calculate_need(max_matrix, allocation_matrix)

    # check validity
    if any(request[j] > need[process_id][j] for j in range(len(request))):
        print("Error: Request exceeds process maximum need")
        return

    if any(request[j] > available[j] for j in range(len(request))):
        print("Resources not available, process must wait")
        return

    # pretend allocation
    for j in range(len(request)):
        available[j] -= request[j]
        allocation_matrix[process_id][j] += request[j]
        need[process_id][j] -= request[j]

    # safety check
    safe, sequence = is_safe(available, max_matrix, allocation_matrix)

    if safe:
        print("Request GRANTED")
        print("Safe sequence:", ["P" + str(i) for i in sequence])
    else:
        # rollback
        for j in range(len(request)):
            available[j] += request[j]
            allocation_matrix[process_id][j] -= request[j]

        print("Request DENIED (would lead to unsafe state)")

available = [3, 3, 2]
# max request each process may request for each resources
max_matrix = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]
# the number of resources currently assigned to each process
allocation_matrix = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

# Example request: P1 requests [1,0,2] success case
request_resources(1, [1, 0, 2], available, max_matrix, allocation_matrix)


available = [1, 0, 0]

max_matrix = [
    [2, 1, 1],
    [1, 1, 0]
]

allocation_matrix = [
    [1, 0, 1],
    [0, 1, 0]
]

# Request: p0 requests [1, 0, 0] -> a faild case
request_resources(0, [1, 0, 0], available, max_matrix, allocation_matrix)