import subprocess
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [line.split(':')[1][1:-1] for line in data if 'Perfil de todos los usuarios' in line]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', 'ignore').split('\n')
    password = [line.split(':')[1][1:-1] for line in results if 'Contenido de la clave' in line]
    try:
        print(f"La clave del wifi {i} es: {password[0]}")
    except IndexError:
        print(f"Para el wifi: {i}, no hay contraseña")
