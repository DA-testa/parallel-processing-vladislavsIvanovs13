# python3

def parallel_processing(n, m, runtimes):
    output = []
    elapsed_time = 0
    i = 0
    thread = 0
    time_array = []
    
    for job in range(m):
        output.append((thread, elapsed_time))
        time_array.append(elapsed_time)
        thread += 1
        if len(time_array) >= n:
            if len(time_array) > n:
                i += 1
            elapsed_time = time_array[len(time_array)-n] + runtimes[i]
        if thread == n:
            thread = 0

    return output

def main():
    first_line = input()
    second_line = input()
    
    splitted_first_line = first_line.split()
    runtimes = list(map(int, second_line.split()))
    
    n = int(splitted_first_line[0])
    m = int(splitted_first_line[1])
    
    # assert(m == len(runtimes))
    
    # n - thread count 
    # m - job count

    result = parallel_processing(n,m,runtimes)
    
    for thread, time_moment in result:
        print(thread, time_moment)


if __name__ == "__main__":
    main()
