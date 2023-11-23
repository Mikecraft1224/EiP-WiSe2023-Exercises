for i in range(5):
    jobs = []

    with open(f"Blatt 04/fahrradwerkstatt{i}.txt") as f:
        for line in f.readlines():
            if line.strip() != "":
                # map(int, ["1", "2", "3"]) -> [int(s) for s in list] -> [1, 2, 3]
                jobs.append(list(map(int, line.strip().split(" "))))

    waitingTimes = []
    # currentTime = 0
    currentTime = 60*9

    for job in jobs:
        ##############################################
        # 5.1:
        #
        # if currentTime <= job[0]:
        #     currentTime = job[0] + job[1]
        # else:
        #     currentTime += job[1]
        #
        # waitingTimes.append(currentTime - job[0])
        ##############################################

        ##############################################
        # 5.2:
        # Set currenTime to the next possible time to start a job
        if currentTime <= job[0]:
            if job[0] % (24*60) in range(9*60, 17*60):
                currentTime = job[0]                                    # next possible time
            else:
                currentTime = (job[0]//(24*60) + 1) * (24*60) + 9*60    # next day 9:00

        # Now we can start the job
        # add 24h for every 8h of work since only 8h per day are possible
        # then add the remaining minutes
        currentTime += (job[1]//(8*60))*24*60 + job[1]%(8*60)           

        # If the job is finished after 17:00, add 16h to the current time to convert it to the next day
        if currentTime%(60*24) > 60*17:
            currentTime += 60*16

        # Calculate the waiting time for the current job
        waitingTimes.append(currentTime - job[0])
        ##############################################


    averageWaitingTime = sum(waitingTimes) / len(waitingTimes)
    print(f"Maximum waiting time for file {i}: {max(waitingTimes)}")
    print(f"Average waiting time for file {i}: {averageWaitingTime}", end="\n\n")