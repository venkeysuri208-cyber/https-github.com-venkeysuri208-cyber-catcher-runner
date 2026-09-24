# Catcher vs Runner

A starter repository for a pursuit-and-capture competition in which a Catcher algorithm is evaluated against a moving Runner.

## Objective
Capture the Runner as quickly as possible. The primary metric is **elapsed time from trial start to first valid capture**.

## Included
- A simple 2D simulation with a moving Runner and a Catcher controller.
- A proportional pursuit controller.
- Capture-radius detection and trial timeout.
- CSV-ready trial results and basic command-line execution.

## Quick start
Requires Python 3.10+.

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python -m catcher.simulation
```

## Configuration
Edit `SimulationConfig` in `catcher/simulation.py` to change speeds, capture radius, time step, initial positions, and timeout.

## Metric
A trial is successful when the distance between Catcher and Runner is less than or equal to `capture_radius`. Reported capture time is the first simulation time at which this condition is true. Unsuccessful trials are marked `captured: false` and end at the configured time limit.

## Hardware / TurtleBot extension
The included simulator is a reproducible software baseline, not a certified robotics stack. For TurtleBot use, replace the simulation state source and motion command interface with ROS 2 topics/actions, add odometry and obstacle handling, and preserve the same capture criterion and timing definition. Test in simulation before operating physical robots.

## Repository layout
```
catcher-runner/
├── catcher/
│   ├── __init__.py
│   └── simulation.py
├── tests/
│   └── test_simulation.py
├── requirements.txt
└── README.md
```

## Competition considerations
Use the organizer's exact arena dimensions, target motion, safety rules, and capture definition when available. Record the random seed and configuration for every trial so results can be reproduced.
