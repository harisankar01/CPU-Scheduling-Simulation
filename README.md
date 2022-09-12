# CPU Scheduling Simulation

 CPU scheduling is used to determine which process or task must be done **first** when many 
process are waiting to be completed. In this project I have created a simulation of these three algorithms to understand them more easier.

  CPU use may algorithms such as 

  + First Come First Served(FCFS)
  + Shortest Job First(SJF)
  + Round robin

   Basically a process have a fixed execution time(time required to complete the process), waiting time(time the process has to wait to be processed).
These algorithms are designed to reduce waiting time and ensure that the CPU is continuously executing processes without being idle. 
## FCFS 

The first process which come will be processed by the CPU before processing the next process.

## SJF

The process which have least time of execution will be processed first.

## Round Robin

The process is processed in multiple steps hence giving an equal chance to all processes. This is the **most efficient** algorithm for cpu scheduling

# Install with pip
 You can easily install the simulations of these three algorithms using pip. The name of the package is **CpuSchedulingSimulation** 
 and the module used is **Cpu_scheduling_algorithms**. You can find the documentation [here](https://pypi.org/project/CpuSchedulingSimulation/#description)

```
pip install CpuSchedulingSimulation
```

> Note: This will also install pygame(version 2.1.2)

## Examples

Then just import the package and run the functions named as algorithms to see the simulation in action.
```python
import Cpu_scheduling_algorithms as css
css.FCFS()
```
```python
css.SJF()
```
```python
css.Round_Robin()
```


# Cloning the repo
Use the following command to clone the repo to your local system.

```commandline
git clone https://github.com/harisankar01/CPU-Scheduling-Simulation.git
```
Then go into the folder to execute the functions.
```commandline
cd CPU-Scheduling-Simulation
```
### Packages used 
  **Pygame** a popular game library in pyton is used in this project to create simulation of the scheduling process

```
pip install pygame
```

Then finally run the main file which is `FCFS.py` and understand CPU scheduling easily.

```commandline
python3 FCFS.py
```

> Note: These simulations can be used to understand CPU scheduling effectively, if you have basic knowledge of 
> CPU scheduling algorithms


# Images
![Screenshot (23)](https://user-images.githubusercontent.com/90249023/189670435-eab00400-89a6-4ef4-9629-833e7da80617.png)
![Screenshot (26)](https://user-images.githubusercontent.com/90249023/189670631-014b8d14-a996-4073-9dbd-282338000250.png)
![Screenshot (28)](https://user-images.githubusercontent.com/90249023/189670664-ce324ea6-b00b-4324-b6c3-75263a033af9.png)
