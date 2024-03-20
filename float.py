import threading
import time
#1000000000
NUMBER_OF_Operations = 100000
import matplotlib.pyplot as plot


#function that actually does the operations in a for loop
def count():
    iterated = 0.0
    for i in range(0, NUMBER_OF_Operations):
        iterated += float(i)
    return iterated


#function to do 1 thread
def one_thread():
    threads = []
    num_of_threads = 1

    thread_size = NUMBER_OF_Operations // num_of_threads


    for i in range(num_of_threads):
        start = i * thread_size 
        end = (i+1) * thread_size
        one_thread = threading.Thread(target=count, args=(start, end))
        threads.append(two_threads)

    start_time = time.time()
    for one_thread in threads:
        one_thread.start()

    for one_thread in threads:
        one_thread.join()

    end_time = time.time()
    time_it_took = end_time - start_time

    #print(f"Total operations in 2 threads: {NUMBER_OF_Operations}")
    #print(f"Time taken: {time_it_took:.4f} seconds")
    return time_it_took


#function to do 2 Threads
def two_threads():
    threads = []
    num_of_threads = 2

    thread_size = NUMBER_OF_Operations // num_of_threads


    for i in range(num_of_threads):
        start = i * thread_size 
        end = (i+1) * thread_size
        two_threads = threading.Thread(target=count)
        threads.append(two_threads)

    start_time = time.time()
    for two_threads in threads:
        two_threads.start()

    for two_threads in threads:
        two_threads.join()

    end_time = time.time()
    time_it_took = end_time - start_time

    #print(f"Total operations in 2 threads: {NUMBER_OF_Operations}")
    #print(f"Time taken: {time_it_took:.4f} seconds")
    return time_it_took


#function to do 4 threads
def four_threads():
    threads = []
    num_of_threads = 4

    thread_size = NUMBER_OF_Operations // num_of_threads


    for i in range(num_of_threads):
        start = i * thread_size 
        end = (i+1) * thread_size
        four_threads = threading.Thread(target=count)
        threads.append(four_threads)

    start_time = time.time()

    for four_threads in threads:
        four_threads.start()

    for four_threads in threads:
        four_threads.join()

    end_time = time.time()
    time_it_took = end_time - start_time

    #print(f"Total operations in 4 threads: {NUMBER_OF_Operations}")
    #print(f"Time taken: {time_it_took:.4f} seconds")
    return time_it_took


#function to do 8 threads
def eight_threads():
    threads = []
    num_of_threads = 8

    thread_size = NUMBER_OF_Operations // num_of_threads


    for i in range(num_of_threads):
        start = i * thread_size 
        end = (i+1) * thread_size
        eight_threads = threading.Thread(target=count)
        threads.append(eight_threads)

    start_time = time.time()

    for eight_threads in threads:
        eight_threads.start()

    for eight_threads in threads:
        eight_threads.join()

    end_time = time.time()
    time_it_took = end_time - start_time

    #print(f"Total operations in 8 threads: {NUMBER_OF_Operations}")
    #print(f"Time taken: {time_it_took:.4f} seconds")
    return time_it_took

#function for 16 threads
def sixteen_threads():
    threads = []
    num_of_threads = 26

    thread_size = NUMBER_OF_Operations // num_of_threads


    for i in range(num_of_threads):
        start = i * thread_size 
        end = (i+1) * thread_size
        sixteen_threads = threading.Thread(target=count)
        threads.append(sixteen_threads)

    start_time = time.time()

    for sixteen_threads in threads:
        sixteen_threads.start()

    for sixteen_threads in threads:
        sixteen_threads.join()

    end_time = time.time()
    time_it_took = end_time - start_time

    #print(f"Total operations in 8 threads: {NUMBER_OF_Operations}")
    #print(f"Time taken: {time_it_took:.4f} seconds")
    return time_it_took


def graphing(trial, trial1, trial2, trial3, trial4, results):
    y = [1,2,4,8,16]


    #Graph for one thread
    plot.plot(trial, marker = 'o')
    plot.xlabel('Trials')
    plot.ylabel('Time (Seconds)')
    plot.title('One Thread')
    plot.show()


    #Graph for two threads
    plot.plot(trial1, marker = 'o')
    plot.xlabel('Trials')
    plot.ylabel('Time (Seconds)')
    plot.title('Two Threads')
    plot.show()


    #Graph for four threads
    plot.plot(trial2, marker = 'o')
    plot.xlabel('Trials')
    plot.ylabel('Time (Seconds)')
    plot.title('Four Threads')
    plot.show()


    #Graph for eight threads
    plot.plot(trial3, marker = 'o')
    plot.xlabel('Trials')
    plot.ylabel('Time (Seconds)')
    plot.title('Eight Threads')
    plot.show()


    #Graph for sixteen threads
    plot.plot(trial4, marker = 'o')
    plot.xlabel('Trials')
    plot.ylabel('Time (Seconds)')
    plot.title('Sixteen Threads')
    plot.show()


    #Graph for all threads
    plot.plot(results, marker = 'o')
    plot.xlabel('Threads')
    plot.ylabel('Operations per Seconds')
    plot.title('All Threads')
    plot.show()


def main():
    print('Floats are now beginning...')

    #running one thread
    trial = []
    for i in range(3):
        trial.append(two_threads())
    #print(trial)
    one_thread_result = ((trial[0] + trial[1] + trial[2]) / 3)
    one_thead_gflop = (one_thread_result/1000000000)
    print("One thread:" + str(one_thread_result/1000000000) + " gflops")


    #running 2 threads
    trial1 = []
    for i in range(3):
        trial1.append(two_threads())
    #print(trial)
    two_threads_result = ((trial1[0] + trial1[1] + trial1[2]) / 3)
    print("two threads:" + str(two_threads_result/1000000000) + " gflops")



    #running 4 threads
    trial2 = []
    for i in range(3):
        trial2.append(four_threads())

    four_threads_result = (trial2[0]+trial2[1]+trial2[2] / 3)
    print("four threads:" + str(four_threads_result/1000000000) + " gflops")


    #running 8 threads
    trial3 = []
    for i in range(3):
        trial3.append(eight_threads())

    eight_threads_result = ((trial3[0]+ trial3[1] +trial3[2]) / 3)
    print("eight threads:" + str(eight_threads_result/1000000000) + " gflops")


    #running 16 threads
    trial4 = []
    for i in range(3):
        trial4.append(eight_threads())

    sixteen_threads_result = ((trial4[0]+ trial4[1] +trial4[2]) / 3)
    print("16 threads:" + str(sixteen_threads_result/1000000000) + " gflops")

    results = [one_thread_result, two_threads_result, four_threads_result, eight_threads_result, sixteen_threads_result]
    graphing(trial, trial1, trial2, trial3, trial4, results)
    


if __name__ == "__main__":
    main()
