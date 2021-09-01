<div align="center">
    <img src="logo.png">
</div>

Tool to download complete directories from a Github repository.

# Installation

```
$ git clone https://github.com/Jalkhov/Octodir.git
$ cd Octodir
$ pip3 setup.py install
```

# Use

## From the console

```
$ octodir
```

**You will be asked for the following data:**

* **Full folder url:** Direct url to the target folder
  * **Example:** https://github.com/Jalkhov/octodir/tree/stable/octodir
* **Output folder**: Absolute path of the output directory
  * You can enter a dot to download in the current working directory

## In code

```python
from octodir import Octodir

target = 'https://github.com/Jalkhov/Octodir/tree/stable/octodir'
folder = '.' # Current working directory

Octo = Octodir(target, folder)
Octo.dowload_folder()
```

# Support me <3

<a href="https://www.buymeacoffee.com/Jalkhov" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
