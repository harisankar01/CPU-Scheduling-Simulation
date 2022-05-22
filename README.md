# CPU Scheduling Simulation
  CPU use may algorithms such as 
  + First Come First Served(FCFS)
  + Shortest Job First(SJF)
  + Round robin

  These are used to schedule which process or task must be done **first** when many 
process are waiting. In this project I have created a simulation of these three algorithms to understand them more easier.

## FCFS 

The fisrt process which come will be processed by the CPU before processing the next process.

## SJF

The process which have least time of execution will be processed first.

## Round Robin

The process is processed in multiple steps hence giving a equal chance to all processes

# Install with pip
 You can easily install this using pip,
```
pip install Cpu-scheduling-simulation
```
## Examples

Then just import the package and run the functions named as algorithms to see the simulation in action
```python
import CpuSchedulingSimulation as css
css.FCFS()
css.SJF()
css.Round_Robin()
```


# Packages used 
  **Pygame** a popular game library in pyton is used in this project to create simulation of the scheduling process

```
pip install pygame
```
You can also clone the repository and run the command to see the simulation in action 
```commandline
python3 FCFS.py
```

> Note: These simultaion can be used to understand CPU scheduling effectively, if you have basic knowledge of 
> CPU scheduling algorithms
