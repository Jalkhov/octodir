<div align="center">
    <img src="logo.png">
</div>

Download individual directorys from GitHub repository

# Installation
1. Download latest release [HERE](https://github.com/Jalkhov/octodir/releases/latest)
2. Extract the file and enter the directory
3. Now in the console type
    ```
    $ pip3 setup.py install
    ```
4. And press Enter

# Use

## From the console

```
$ octodir
```

**You will be asked for the following data:**

* **Full folder url:** Direct url to the target folder
  * **Example:** `https://github.com/Jalkhov/octodir/tree/stable/octodir`
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

<a href="https://www.buymeacoffee.com/Jalkhov" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
