@echo off
echo 🔍 Генерация requirements.in из импортов...
pipreqs ./src --force --savepath requirements.in

echo 🔧 Компиляция requirements.txt из requirements.in...
pip-compile requirements.in

echo ✅ Готово! requirements.txt обновлён.
pause
