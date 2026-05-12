# Visão - Detecção de EPIs (versão 1)

> Projeto simples para detecção de Equipamentos de Proteção Individual (EPIs) em vídeo usando YOLO (ultralytics) e OpenCV.

## Estrutura
- `detector.py` - wrapper do modelo YOLO para inferência sobre frames.
- `especialista.py` - regras simples de avaliação/alerta sobre detecções (ex.: pessoa sem capacete).
- `main.py` - captura de vídeo (webcam), pipeline de inferência e exibição em tempo real.
- `requirements.txt` - dependências do projeto.

## Requisitos
- Python 3.8+
- GPU opcional (melhora desempenho da inferência)

Instale dependências:

```bash
pip install -r requirements.txt
```

Observação: recomenda-se fixar versões em um ambiente de produção (ex.: `ultralytics==8.x.x`, `opencv-python==4.x`).

## Uso
Execute com as opções disponíveis (modelo, câmera, limiar de confiança, redimensionamento opcional):

```bash
python main.py --model yolov8n.pt --camera 0 --conf 0.25 --width 640 --height 480
```

Pressione `ESC` para sair.

## Notas importantes
- O `detector.py` usa o pacote `ultralytics` (YOLOv8). Antes de usar, confirme que as classes esperadas existem no modelo (por exemplo, `helmet` pode não estar presente em modelos genéricos; você pode precisar adaptar o nome da classe ou treinar um modelo customizado).
- O pipeline atual é intencionalmente simples:
  - captura frame em BGR (OpenCV), passa direto para o modelo; recomenda-se converter para RGB e aplicar resize para melhorar desempenho.
  - filtrar detecções por confiança (`box.conf`) pode reduzir falsos positivos.
- `especialista.py` contém regras básicas. Para cenários reais, implemente associação pessoa↔EPI (tracking ou IoU por bbox) para avaliar se cada pessoa usa EPI.

## Melhorias sugeridas (próximos passos)
- O código atualizado já realiza conversão BGR→RGB, permite redimensionamento antes da inferência e filtra detecções por confiança.
- `main.py` agora aceita argumentos: `--model`, `--camera`, `--conf`, `--width`, `--height`.
- `especialista.py` aplica associação pessoa↔EPI via IoU para determinar se cada pessoa usa capacete.
- Criar testes e adicionar `README` de instalação com instruções CUDA/cuDNN se usar GPU.

## Licença
Projeto para fins educacionais — adapte conforme necessário.
