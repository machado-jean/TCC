import subprocess 
try: 
    subprocess.check_call(["pip", "install", "-r", "requirements.txt"]) 
    print("Bibliotecas instaladas com sucesso a partir do arquivo requirements.txt.") 
except subprocess.CalledProcessError as e: 
    print("Erro ao instalar bibliotecas a partir do arquivo requirements.txt.") 
    print(f"Código de erro: {e.returncode}") 
