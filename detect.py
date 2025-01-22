from ultralytics import YOLO
model = YOLO("yolo11s.pt")

import random
import cv2
import os
import matplotlib.pyplot as plt
import yaml

# Caminhos dos diretórios e arquivo YAML
image_dir = '/kaggle/input/guns-and-knifes-detection-in-cctv-videos/combined_gunsnknifes/train/images'
label_dir = '/kaggle/input/guns-and-knifes-detection-in-cctv-videos/combined_gunsnknifes/train/labels'
yaml_path = 'https://www.kaggle.com/code/myriamgam62/guns-and-knife-detection-yolov11-new/input/guns-and-knifes-detection-in-cctv-videos/combined_gunsnknifes/data.yaml'

# Carregar os nomes das classes do arquivo YAML
with open(yaml_path, 'r') as f:
    data = yaml.safe_load(f)
    class_names = data['names']
    print(f"Classes disponíveis: {class_names}")

# Selecionar 16 imagens aleatórias
image_files = os.listdir(image_dir)
random_images = random.sample(image_files, 16)

# Configuração do Matplotlib
fig, axs = plt.subplots(4, 4, figsize=(16, 16))

# Processar cada imagem selecionada
for i, image_file in enumerate(random_images):
    row = i // 4
    col = i % 4

    # Caminhos para a imagem e o rótulo correspondente
    image_path = os.path.join(image_dir, image_file)
    label_file = os.path.splitext(image_file)[0] + ".txt"
    label_path = os.path.join(label_dir, label_file)

    # Ler a imagem
    image = cv2.imread(image_path)

    # Verificar se o arquivo de rótulo existe
    if not os.path.exists(label_path):
        print(f"Rótulo não encontrado para {image_file}. Pulando...")
        continue

    # Ler o rótulo
    with open(label_path, "r") as f:
        labels = f.read().strip().split("\n")

    # Desenhar caixas delimitadoras para a classe "knife"
    for label in labels:
        if len(label.split()) != 5:
            continue
        class_id, x_center, y_center, width, height = map(float, label.split())
        class_id = int(class_id)

        # Verificar se a classe é "knife"
        if class_names[class_id] != "knife":
            continue

        # Calcular coordenadas da caixa delimitadora
        x_min = int((x_center - width / 2) * image.shape[1])
        y_min = int((y_center - height / 2) * image.shape[0])
        x_max = int((x_center + width / 2) * image.shape[1])
        y_max = int((y_center + height / 2) * image.shape[0])

        # Desenhar a caixa e o nome da classe
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 3)
        cv2.putText(image, "knife", (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2, cv2.LINE_AA)

    # Exibir a imagem
    axs[row, col].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axs[row, col].axis('off')

plt.tight_layout()
plt.show()
