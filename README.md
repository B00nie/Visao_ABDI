# Visão - Detecção de EPIs

> Projeto para detecção de Equipamentos de Proteção Individual (EPIs) em vídeo usando YOLO (ultralytics) e OpenCV, com conversão BGR->RGB e associação pessoa↔EPI por IoU.

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
- O `detector.py` usa o pacote `ultralytics` (YOLOv8). Antes de usar, confirme que as classes esperadas existem no modelo; por exemplo, `helmet` pode não estar presente em modelos genéricos e pode exigir modelo customizado.
- O pipeline atual já converte a imagem de BGR para RGB antes da inferência e permite redimensionamento opcional para melhorar o desempenho.
- O `especialista.py` já faz a associação pessoa↔EPI usando IoU para verificar se cada pessoa está com capacete.
- O filtro por confiança (`box.conf`) ajuda a reduzir falsos positivos.

## Melhorias implementadas
- Conversão BGR->RGB antes de chamar o modelo.
- Redimensionamento opcional via `--width` e `--height`.
- Associação pessoa↔EPI por IoU para avaliação mais consistente.
- Parâmetros de execução em `main.py`: `--model`, `--camera`, `--conf`, `--width`, `--height`.

## Próximos passos
- Criar testes automatizados para a lógica de associação por IoU.
- Adicionar instruções de CUDA/cuDNN caso o projeto seja usado com GPU.

## Licença
Projeto para fins educacionais — adapte conforme necessário.
