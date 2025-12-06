# Repository Guidelines

This repository contains Python code for a 2025 FIRST LEGO League robot using a LEGO Spike Prime hub with v3 firmware.

## Project Structure & Modules

- `master.py` – main robot control code and motion helpers.
- `README.md` – robot overview, hardware mapping, and usage.
- `plan.md` – planned high-level API for driving, turning, attachments, and mission selection.
- `AGENTS.md` – this contributor guide.

Keep new mission or helper files in the repo root unless a clear folder structure is introduced later (e.g., `missions/`, `lib/`).

## Run, Build, and Development

- Code is deployed via the LEGO Spike app; there is no traditional build system.
- To test a change:
  - Load the updated `.py` file into the Spike app.
  - Download to the hub and run from the hub menu.

If you add helper scripts (e.g., simulations), put them in a dedicated folder and document usage in `README.md`.

## Coding Style & Naming

- Language: Python 3 (Spike v3 runtime).
- Indentation: 4 spaces, no tabs.
- Use descriptive function names (`drive_forward`, `spin_left`) and avoid one-letter variables except for simple loop counters.
- Prefer small, single-purpose functions and reuse shared helpers for motion logic.
- Keep ports and hardware assumptions clearly named and documented.

## Testing Guidelines

- Primary testing is on the physical robot field.
- When changing motion logic:
  - Test straight drives, pivots, and spins separately.
  - Record successful parameter sets (speeds, degrees) in `plan.md` or mission-specific comments.

## Commit & Pull Request Guidelines

- Use clear, imperative commit messages, e.g., `Add spin_left helper` or `Refine drive_forward gyro logic`.
- For pull requests:
  - Summarize high-level changes and impacted missions.
  - Note any new or changed parameters that require field re-tuning.
  - Update `README.md` and `plan.md` when public APIs or ports change.
