1. when trying to time a program there are multiple different factors to consider:
  - background apps using CPU resources
  - variables in memory

  timeit.timeit tries to solve these issues by running the code multiple times and 
summing the execution time. through this approach it reduces random outliers by averaging everything out over multiple runs.

  timeit.repeat runs multiple independant sets of trials to try and capture these outliers. Each independant trail consists of a number of executions allowing to capture variations and fluctuations in performance.

  use timeit.timeit when the variability is not of concern or expected to be minimal
use timeit.repeat when testing consistency across multiple runs

2. - you should be taking the average when using timeit.timeit. because the executions occur within a continuous block taking the average helps reduce noise
   - for timeit.repeat the minimum should be used. because repeat captures independant trials it is best if the miniumum is used as that should represent the run with the least number of variables affecting performance

