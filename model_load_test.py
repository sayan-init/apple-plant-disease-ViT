import numpy as np
import tensorflow as tf

loaded_model = tf.keras.models.load_model('saved_model/vit_al9ee')
loaded_model.summary()

IMG_WIDTH = 120
IMG_HEIGHT = 120
BATCH_SIZE = 100

TESTING_DATASET_DIR = './AL9EE_DATASET/test'
dataset = tf.keras.utils.image_dataset_from_directory(
  TESTING_DATASET_DIR,
  image_size=(IMG_HEIGHT, IMG_WIDTH),
  batch_size=BATCH_SIZE
)

correctly_predicted = 0
total_images = 0         
for step, (images, labels) in enumerate(dataset):
  actual_results = labels.numpy()
  predictions = loaded_model(images)
  for j in range(len(predictions.numpy())):
    total_images += 1
    pd = predictions[j]
    max_i = 0
    for i in range(len(pd)):
        if pd[i] > pd[max_i]:
            max_i = i
    if max_i == actual_results[j]:
        correctly_predicted += 1

print(f"accuracy -> {correctly_predicted / total_images}")
