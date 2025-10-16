Install the following VScode extension

- vscode-icons-team.vscode-icons
- ms-python.python
- ms-python.vscode-pylance
- ms-python.pylint
- ms-python.debugpy
- ms-python.black-formatter

Setup python environemnt

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m ensurepip --upgrade
    python -m pip install --upgrade pip

Install the required packages

    pip install -r requirements.txt

Select the python intepreter with

- Ctrl+Shift+P
- Select Python: Select intepreter"
- Select Python x.y.z ('.venv':venv) Recommended

The Lauch settings contains the argument used when starting debugging with F5

    {
        // Use IntelliSense to learn about possible attributes.
        // Hover to view descriptions of existing attributes.
        // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python Debugger: Current File",
                "type": "debugpy",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal"
            }
        ]
    }

Start with

    .\.venv\Scripts\Activate.ps1
    python app.py

In the browser open http://127.0.0.1:8000

To deactivate the virtual environment call
