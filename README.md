[![Github top language](https://img.shields.io/github/languages/top/FredHappyface/Python.ActiveGithub.svg?style=for-the-badge)](../../)
[![Codacy grade](https://img.shields.io/codacy/grade/1bf2f48795f2461bb742209f3cc5ae15.svg?style=for-the-badge)](https://www.codacy.com/manual/FredHappyface/Python.ActiveGithub)
[![Repository size](https://img.shields.io/github/repo-size/FredHappyface/Python.ActiveGithub.svg?style=for-the-badge)](../../)
[![Issues](https://img.shields.io/github/issues/FredHappyface/Python.ActiveGithub.svg?style=for-the-badge)](../../issues)
[![License](https://img.shields.io/github/license/FredHappyface/Python.ActiveGithub.svg?style=for-the-badge)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FredHappyface/Python.ActiveGithub.svg?style=for-the-badge)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FredHappyface/Python.ActiveGithub.svg?style=for-the-badge)](../../commits/master)

# Python.ActiveGithub

<img src="readme-assets/icons/proj-icon.png" alt="Project Icon" width="100">

Checks that a repo is active and gets a list of active forks

Turns out that I could have used https://github.com/PyGithub/PyGithub.

## ActiveGithub.py
### Input
- Set the repo lifespan (weeks - eg. 1 - default=36)>
- Enter the user and repo name in the form (user/repo - eg. fredhappyface/python.activegithub)>
### Output
- Identify if the source repo is alive and look for forks that are active and newer
## UserReposActive.py
### Input
- Set the repo lifespan (weeks - eg. 1 - default=36)>
- User repos, watched or starred (R/w/s)>
### Output
- Identify if the selected repos are active
## UserReposTraffic.py
### Input
- Set the repo lifespan (weeks - eg. 1 - default=36)>
- Set the organisation name (hit enter if not applicable)>
### Output
- Ranks your repos and stores the traffic history in userReposTraffic.json


## Language information
### Built for
This program has been written for Python 3 and has been tested with
Python version 3.8.0 <https://www.python.org/downloads/release/python-380/>.

Install with chocolatey
```powershell
choco install python
```
### Other versions
To install Python, go to <https://www.python.org/> and download the latest
version.
## How to run
1. Open the .py file in vscode
2. Ensure a python 3.8 interpreter is selected (Ctrl+Shift+P > Python:Select Interpreter > Python 3.8)
3. Run by pressing Ctrl+F5 (if you are prompted to install any modules, accept)


## Changelog
See the [CHANGELOG](/CHANGELOG.md) for more information.


## Download
### Clone
#### Using The Command Line
1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to
clone to
4. Type 'git clone' followed by URL in step 2
```bash
$ git clone https://github.com/FredHappyface/Python.ActiveGithub
```

More information can be found at
<https://help.github.com/en/articles/cloning-a-repository>

#### Using GitHub Desktop
1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at
<https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop>

### Download Zip File

1. Download this GitHub repository
2. Extract the zip archive
3. Copy/ move to the desired location


## Licence
BSD-2-CLAUSE-PATENT License
Copyright (c) FredHappyface
(See the [LICENSE](/LICENSE.md) for more information.)
