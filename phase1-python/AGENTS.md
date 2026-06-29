# AGENTS.md — Agent instructions for this workspace

Project: CS-Prep / phase1-python

Purpose: Help AI coding agents quickly understand and work on this small, exercise-focused workspace.

Key notes for agents
- Project type: single-file Python exercises. Primary file: [day1.py](day1.py#L1-L7).
- How to run: `python day1.py` (interactive script — prompts for user input).
- Testing: no tests present. If you add testable code, prefer `pytest` and convert interactive code into functions.
- Conventions: keep changes minimal and preserve interactive prompts unless converting the script into functions for testability.

When editing
- For automated runs or CI, refactor interactive blocks into functions guarded by `if __name__ == "__main__":`.
- Avoid adding heavy dependencies without justification.

Useful next customizations
- Add `.github/copilot-instructions.md` to document repo-specific workflows and CI commands for humans/agents.
- Add a simple `README.md` describing the exercise goals and Python version requirement.

Contact: no maintainers listed — open a PR with changes and include rationale in the description.
