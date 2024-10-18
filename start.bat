@echo off

REM Установка зависимостей из requirements.txt
pip install -r requirements.txt

REM Проверка успешности установки
if %errorlevel% neq 0 (
    echo Ошибка при установке зависимостей из requirements.txt
    pause
    exit /b %errorlevel%
)

REM Запуск factory.py
python factory.py

REM Пауза, чтобы увидеть вывод перед закрытием окна
pause