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
|Database verification with background command runs|✅|

## Installation and Usage

Install my software PPA:
- `sudo add-apt-repository ppa:aahilshaikh/software`

Update APT cache:
- `sudo apt update`

Install `ufwmanager` package:
- `sudo apt install ufwmanager`

**NOTE: Package currently published only for Ubuntu 24.04 (Noble Numbat).**

### Requirements
- `Python 3.10+` for running the application.
- `json` python package for json handling.
- `os` python package for bash commands.
- `subprocess` for bash handling.

## Credits
- Made with
    - [![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#) [![Bash](https://img.shields.io/badge/Bash-4EAA25?logo=gnubash&logoColor=fff)](#)
- Made on
    - [![Visual Studio Code](https://custom-icon-badges.demolab.com/badge/Visual%20Studio%20Code-0078d7.svg?logo=vsc&logoColor=white)](#)
- Made for
    - [![Debian](https://img.shields.io/badge/Debian-A81D33?logo=debian&logoColor=fff)](#) [![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?logo=ubuntu&logoColor=white)](#)

## License
- Located [here](https://github.com/The007Programmer/UFW-Manager/blob/main/LICENSE.md).