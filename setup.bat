@echo off

IF NOT EXIST venv (
    echo Python system interpreter:
    where python
    python --version || goto :error
    echo Creating new virtualenv...
    python -m venv venv || goto :error
)

pip install pyyaml
echo Checking variables configuration...
python src/check_config_vars.py || goto :error

echo Activating venv...
call deactivate >NUL 2>NUL
call venv\Scripts\activate.bat

echo installing requirements...
python -m pip install -U pip || goto :error
pip install -U -r requirements.txt || goto :error

:error
echo Failed with error #%error_level%.
exit /b %error_level%
