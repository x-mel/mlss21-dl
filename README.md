# mlss21-dl


## Goal

Download Lectures from the Machine Learning Summer School 2021

## Requirements

- Linux (any distribution with Python3)
- curl (usually comes preinstalled with any linux distribution)
- pip
- selenium
- Google Chrome (stable version)


## Important Notes

- Change the `cred_email` and `cred_name` to fit your email and name credentials respectively


## Usage

- Run the script in a terminal shell:

```python mlss21-dl.py```

## Troubleshooting

- If you have problems loading chrome, make sure the variable `options.binary_location` points to the location of the binary of Chrome on your OS
- Possibility to work on windows, if you manage to fix the binary_location to point to the location of google_chrome.exe
