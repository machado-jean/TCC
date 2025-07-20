import subprocess 
requirements = subprocess.check_output(["pip", "freeze"]).decode("utf-8") 
with open("requirements.txt", "w") as file: 
    file.write(requirements) 
print("Arquivo requirements.txt gerado com sucesso.") 
