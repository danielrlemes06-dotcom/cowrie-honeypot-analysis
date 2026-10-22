import json
from collections import Counter
from pathlib import Path

arquivo = Path("var/log/cowrie/cowrie.json")

tentativas = []
usuarios = Counter()
senhas = Counter()
ips = Counter()

with arquivo.open("r", encoding="utf-8") as log:
    for linha in log:
        try:
            evento = json.loads(linha)
        except json.JSONDecodeError:
            continue

        tipo = evento.get("eventid")

        if tipo in ("cowrie.login.success", "cowrie.login.failed"):
            tentativas.append(evento)

            usuario = evento.get("username", "desconhecido")
            senha = evento.get("password", "não registrada")
            ip = evento.get("src_ip", "desconhecido")

            usuarios[usuario] += 1
            senhas[senha] += 1
            ips[ip] += 1

print("=== RELATÓRIO DO HONEYPOT ===")
print(f"Total de tentativas: {len(tentativas)}")

print("\nUsuários mais tentados:")
for usuario, quantidade in usuarios.most_common(5):
    print(f"  {usuario}: {quantidade}")

print("\nSenhas mais tentadas:")
for senha, quantidade in senhas.most_common(5):
    print(f"  {senha}: {quantidade}")

print("\nIPs de origem:")
for ip, quantidade in ips.most_common(5):
    print(f"  {ip}: {quantidade}")
