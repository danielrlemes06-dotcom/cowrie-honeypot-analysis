import json
from collections import Counter
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt

arquivo = Path("var/log/cowrie/cowrie.json")

tentativas_por_hora = Counter()

with arquivo.open("r", encoding="utf-8") as log:
    for linha in log:
        try:
            evento = json.loads(linha)
        except json.JSONDecodeError:
            continue

        tipo = evento.get("eventid")

        if tipo not in (
            "cowrie.login.success",
            "cowrie.login.failed"
        ):
            continue

        timestamp = evento.get("timestamp")

        if not timestamp:
            continue

        momento = datetime.fromisoformat(
            timestamp.replace("Z", "+00:00")
        )

        hora = momento.strftime("%Y-%m-%d %H:00")
        tentativas_por_hora[hora] += 1

if not tentativas_por_hora:
    print("Nenhuma tentativa de login encontrada.")
else:
    horarios = sorted(tentativas_por_hora)
    quantidades = [
        tentativas_por_hora[horario]
        for horario in horarios
    ]

    plt.figure(figsize=(10, 5))
    plt.bar(horarios, quantidades)

    plt.title("Tentativas de login no Cowrie por horário")
    plt.xlabel("Horário")
    plt.ylabel("Número de tentativas")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.savefig("relatorio_horario.png", dpi=150)
    plt.show()

    print("Gráfico salvo em relatorio_horario.png")
