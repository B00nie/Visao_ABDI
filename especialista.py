def _iou(boxA, boxB):
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    interW = max(0, xB - xA)
    interH = max(0, yB - yA)
    interArea = interW * interH

    boxAArea = max(0, boxA[2] - boxA[0]) * max(0, boxA[3] - boxA[1])
    boxBArea = max(0, boxB[2] - boxB[0]) * max(0, boxB[3] - boxB[1])

    if boxAArea + boxBArea - interArea == 0:
        return 0.0

    return interArea / (boxAArea + boxBArea - interArea)


def avaliar_epi(detections, iou_threshold: float = 0.15):
    persons = [d for d in detections if d.get("classe") == "person"]
    helmets = [d for d in detections if d.get("classe") == "helmet"]

    if not persons:
        return "Nenhuma pessoa", (255, 255, 255)

    pessoas_sem_capacete = 0

    for p in persons:
        bbox_p = p.get("bbox")
        has_helmet = False
        for h in helmets:
            bbox_h = h.get("bbox")
            if _iou(bbox_p, bbox_h) >= iou_threshold:
                has_helmet = True
                break

        if not has_helmet:
            pessoas_sem_capacete += 1

    if pessoas_sem_capacete > 0:
        return f"ALERTA: {pessoas_sem_capacete} sem capacete", (0, 0, 255)

    return "OK: EPI presente", (0, 255, 0)