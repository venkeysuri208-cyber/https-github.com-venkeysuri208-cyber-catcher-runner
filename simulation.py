"""Minimal 2D Catcher-vs-Runner benchmark simulation."""
from dataclasses import dataclass
import math
import random


@dataclass
class SimulationConfig:
    dt: float = 0.05
    max_time: float = 60.0
    arena_width: float = 10.0
    arena_height: float = 10.0
    catcher_speed: float = 1.2
    runner_speed: float = 0.65
    capture_radius: float = 0.30
    catcher_start: tuple[float, float] = (1.0, 1.0)
    runner_start: tuple[float, float] = (8.5, 8.0)
    seed: int = 7


def clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))


def unit_vector(dx: float, dy: float) -> tuple[float, float]:
    norm = math.hypot(dx, dy)
    return (0.0, 0.0) if norm == 0 else (dx / norm, dy / norm)


def run_trial(config: SimulationConfig | None = None) -> dict:
    """Run one trial; return capture status, time, and final positions."""
    cfg = config or SimulationConfig()
    rng = random.Random(cfg.seed)
    cx, cy = cfg.catcher_start
    rx, ry = cfg.runner_start
    heading = rng.uniform(0, 2 * math.pi)
    elapsed = 0.0

    while elapsed <= cfg.max_time:
        distance = math.hypot(rx - cx, ry - cy)
        if distance <= cfg.capture_radius:
            return {
                "captured": True, "capture_time": round(elapsed, 4),
                "distance": distance, "catcher": (cx, cy), "runner": (rx, ry),
            }

        # Baseline Catcher: steer directly toward the current Runner position.
        ux, uy = unit_vector(rx - cx, ry - cy)
        cx = clamp(cx + ux * cfg.catcher_speed * cfg.dt, 0, cfg.arena_width)
        cy = clamp(cy + uy * cfg.catcher_speed * cfg.dt, 0, cfg.arena_height)

        # Baseline Runner: persistent, gently changing heading; reflect at boundaries.
        heading += rng.uniform(-0.45, 0.45)
        nrx = rx + math.cos(heading) * cfg.runner_speed * cfg.dt
        nry = ry + math.sin(heading) * cfg.runner_speed * cfg.dt
        if nrx < 0 or nrx > cfg.arena_width:
            heading = math.pi - heading
        if nry < 0 or nry > cfg.arena_height:
            heading = -heading
        rx = clamp(rx + math.cos(heading) * cfg.runner_speed * cfg.dt, 0, cfg.arena_width)
        ry = clamp(ry + math.sin(heading) * cfg.runner_speed * cfg.dt, 0, cfg.arena_height)
        elapsed = round(elapsed + cfg.dt, 10)

    return {
        "captured": False, "capture_time": None,
        "distance": math.hypot(rx - cx, ry - cy),
        "catcher": (cx, cy), "runner": (rx, ry),
    }


def main() -> None:
    result = run_trial()
    if result["captured"]:
        print(f'CAPTURED in {result["capture_time"]:.2f} seconds')
    else:
        print("NOT CAPTURED before timeout")
    print(f'Final separation: {result["distance"]:.3f} m')
    print(f'Catcher: {result["catcher"]}; Runner: {result["runner"]}')


if __name__ == "__main__":
    main()
