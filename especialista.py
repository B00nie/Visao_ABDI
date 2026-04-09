def avaliar_epi(detections):
    tem_pessoa = any(d["classe"] == "person" for d in detections)
    tem_capacete = any(d["classe"] == "helmet" for d in detections)

    if tem_pessoa and not tem_capacete:
        return "ALERTA: Sem capacete", (0, 0, 255)  # vermelho

    elif tem_pessoa and tem_capacete:
        return "OK: EPI presente", (0, 255, 0)  # verde

    else:
        return "Nenhuma pessoa", (255, 255, 255)  # branco