import os
import subprocess


# ==============================
# FUNCION SEGURA PARA EJECUTAR COMANDOS
# ==============================
def callsh(command, allow_fail=False):
    print("\nEjecutando:", " ".join(command))

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    print(result.stdout)
    print(result.stderr)

    if not allow_fail:
        result.check_returncode()


print("=== INICIO GPU RUNNER TEST ===")


# ==============================
# CLONAR REPOSITORIO
# ==============================
REPO_URL = "https://github.com/junior7819/Pc_ubuntu.git"
REPO_NAME = "Pc_ubuntu"

if not os.path.exists(REPO_NAME):
    callsh(['git', 'clone', REPO_URL])
else:
    print("Repositorio ya existe.")

os.chdir(REPO_NAME)


# ==============================
# SETUP OPCIONAL
# ==============================
if os.path.exists("scripts/setup.sh"):
    callsh(['bash', 'scripts/setup.sh'], allow_fail=True)
else:
    print("setup.sh no encontrado, continuando...")


# ==============================
# CREAR ENTORNO CONDA
# ==============================
callsh([
    'conda', 'create',
    '-n', 'testenv',
    'python=3.8',
    '-y'
], allow_fail=True)


# ==============================
# INSTALAR REQUIREMENTS (OPCIONAL)
# ==============================
if os.path.exists("requirements.txt"):
    callsh([
        '/opt/conda/envs/testenv/bin/pip',
        'install',
        '-r',
        'requirements.txt'
    ], allow_fail=True)
else:
    print("requirements.txt no encontrado.")


# ==============================
# EJECUTAR TESTS (OPCIONAL)
# ==============================
if os.path.exists("tests"):
    callsh([
        '/opt/conda/envs/testenv/bin/pytest',
        'tests'
    ], allow_fail=True)
else:
    print("Carpeta tests no encontrada.")


# ==============================
# TEST GPU
# ==============================
print("\n=== TEST GPU ===")
callsh(['nvidia-smi'], allow_fail=True)


print("\nGPU RUNNER FINALIZADO CORRECTAMENTE")

# test
