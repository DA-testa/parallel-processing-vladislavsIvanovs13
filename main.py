# python3

def parallel_processing(n, m, data):
    output = []
    
    for thread in n:
        output.append((thread, time_moment))
    
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    first_line = input()
    second_line = input()
    
    splitted_first_line = first_line.split()
    data = second_line.split()
    
    n = splitted_first_line[0]
    m = splitted_first_line[1]
    
    assert(jobs == len(data))
    
    # n - thread count 
    # m - job count

    data = []

    result = parallel_processing(n,m,data)
    
    for thread, time in data:
        print(thread, time)


if __name__ == "__main__":
    main()
