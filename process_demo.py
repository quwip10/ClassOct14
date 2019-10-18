
import subprocess


p1 = subprocess.run(['cmd', '/c', 'dir', 'c:\\class\\datassssss'],
                    capture_output=True, text=True)


if p1.returncode == 0:
    print(p1.stdout)
else:
    print("Problem")
    print(p1.stderr)
