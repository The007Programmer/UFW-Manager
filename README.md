![UFWManagerLogo](ufwmanager.png)

<p align="center">
    <img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" alt="Maintainence">
    <img src="https://img.shields.io/github/last-commit/The007Programmer/UFW-Manager" alt="Last Commit">
    <img src="https://img.shields.io/github/v/tag/The007Programmer/UFW-Manager" alt="Version">
    <img src="https://img.shields.io/github/contributors/The007Programmer/UFW-Manager" alt="Contributors">
    <img src="https://img.shields.io/github/issues/The007Programmer/UFW-Manager" alt="Issues">
    <img src="https://img.shields.io/github/issues-pr/The007Programmer/UFW-Manager" alt="Pull Requests">
    <img src="https://img.shields.io/badge/Read%20the%20Docs-8CA1AF?logo=readthedocs&logoColor=fff" alt="Docs">
</p>

## What is it?
A simple tool for IP management on servers. Currently this python file is executable exclusively on Debian-based servers, as the bash commands are specific to the filepath and syntax of Debian architecture.

## TOC
> [Description](#what-is-it)<br>
> [Features](#features)<br>
> [Usage](#installation-and-usage)<br>
> [Package Requirements](#requirements)<br>
> [Credits](#credits)<br>
> [License](#license)<br>
> [Understanding Commits](#commits-key)<br>

## Features
| Feature    | Implemented? |
| -------- | ------- |
|Can allow all IPs listed|✅|
|Stores and recieves IPs from JSON file|✅|
|Status commands (who is currently whitelisted)|✅|
|Interactive IP addition/removal|✅|
|Windows Server support|✅|

## Installation and Usage
1. Download the ZIP file.
2. Extract contents to desired run folder (move to server if downloaded on computer).
3. Open or `cd` to the project directory in a terminal.
4. Run `python3 tool.py` to open the tool.

### Requirements
- `Python 3.10+` for running the application.
- `json` python package for json handling.
- `os` python package for bash commands.
- `subprocess` for bash handling.

## Credits
- No external sources.
- Made with
    - [![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#) [![Bash](https://img.shields.io/badge/Bash-4EAA25?logo=gnubash&logoColor=fff)](#)
- Made on
    - [![Visual Studio Code](https://custom-icon-badges.demolab.com/badge/Visual%20Studio%20Code-0078d7.svg?logo=vsc&logoColor=white)](#)
- Made for
    - [![Debian](https://img.shields.io/badge/Debian-A81D33?logo=debian&logoColor=fff)](#) [![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?logo=ubuntu&logoColor=white)](#)

## License
- Located [here](https://github.com/The007Programmer/UFW-Manager/blob/master/LICENSE.md).

### Commits Key
- SAFE: Stable and production-ready code; can be safely deployed.
- TEST: Code meant for testing or experimental changes; safe but does not affect the main program directly; stable for version control.
- UNST: Unstable commit with potential issues; not suitable for production, used for backup or testing phases.
- HTFX: Hotfix for critical issues.
- REFA: Refactor or restructure code for improved readability, maintainability, or efficiency, with no changes to core functionality.
- RESD: Revert previous changes due to instability or issues encountered during testing; restores the code to a prior stable state.
- BUGF: Bug fix or issue resolution, fixing known problems in the code without adding new functionality.
- DOCS: Documentation update, including comments, README files, or other forms of documentation to improve clarity and understanding.