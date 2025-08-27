## LCV Schedule Creater
Electric LCV schedule tool

**LCVScheduleCreater** is a Python-based tool designed for the creation of schedules for electric light commercial vehicles (LCV)

## Installation
**1.** Create a new environment with the requirements described in "requirements.txt" file.
For example, in Python (Windows) write in the terminal:
    Python -m venv schedule
    schedule\Scripts\activate
    pip install -r requirements.txt

For example, in python (macOS / Linux) write in the terminal:
    Python -m venv schedule
    source schedule/bin/activate
    pip install -r requirements.txt


## How to use the tool
You can use the entire tool by running the notebook:
- notebooks/Schedule Generation Module.ipynb for Module 1, to create schedules for an electric LCV fleet
- notebooks/optimisation Module.ipynb for Module 2, to run the optimisation model

## Configurations

The software configuration is structured around four sections that manage the generation of schedules and the operation of the optimisation function:

1.1 Schedule generator configurations: Define the parameters required to generate the travel and charging patterns for each vehicle in the LCV fleet.

1.2. Fleet parameters configurations: Define the characteristics of the fleet used for schedule generation.

## Citation
If you use , please cite:
