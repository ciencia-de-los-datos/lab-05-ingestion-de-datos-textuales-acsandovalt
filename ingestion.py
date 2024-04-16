import zipfile
import os
import pandas as pd

def generate_csv_files(zip_file_path, folder_names):
    # Descomprimir el archivo zip
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall()

    # Leer archivos de texto y obtener sus sentimientos
    train_data = []
    test_data = []
    for folder_name in folder_names:
        folder_path = os.path.join(os.getcwd(), folder_name)
        for subfolder_name in os.listdir(folder_path):
            subfolder_path = os.path.join(folder_path, subfolder_name)
            if os.path.isdir(subfolder_path):
                sentiment = subfolder_name
                for file_name in os.listdir(subfolder_path):
                    if file_name.endswith('.txt'):
                        file_path = os.path.join(subfolder_path, file_name)
                        with open(file_path, 'r', encoding='utf-8') as file:
                            text = file.read()
                            if folder_name == 'train':
                                train_data.append({'phrase': text, 'target': sentiment})
                            elif folder_name == 'test':
                                test_data.append({'phrase': text, 'target': sentiment})

    # Crear DataFrames
    train_df = pd.DataFrame(train_data)
    test_df = pd.DataFrame(test_data)

    # Guardar DataFrames como archivos CSV
    train_df.to_csv('train_dataset.csv', index=False)
    test_df.to_csv('test_dataset.csv', index=False)

    # Contar las ocurrencias de "positive", "negative" y "neutral" en cada archivo CSV
    train_counts = train_df['target'].value_counts().to_dict()
    test_counts = test_df['target'].value_counts().to_dict()

    return train_counts, test_counts

# Llamada a la función
train_counts, test_counts = generate_csv_files('data.zip', ['train', 'test'])

print(train_counts)
print(test_counts)


