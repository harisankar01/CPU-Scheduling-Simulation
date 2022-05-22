from setuptools import setup

with open("./Cpu_scheduling_algorithms/README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(name='Cpu_scheduling_simulation',
version='0.2',
description='See live simulation of FCFS, SJF, Round Robin algorithms in CPU scheduling',
url='https://github.com/harisankar01/CPU-Scheduling-Simulation',
author='Hari Hara Sankar',
author_email='hariharasankar.k.a@gmail.com',
license="MIT",
classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
long_description = long_description,
long_description_content_type = "text/markdown",
keywords = "CPU Scheduling algorithms Simulation",
packages=['Cpu_scheduling_algorithms'],
install_requires=['pygame==2.1.2'],
zip_safe=False
      )