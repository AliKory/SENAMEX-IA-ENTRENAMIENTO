import os
import pandas as pd
from mediapipe.python.solutions.holistic import Holistic
from helpers import get_keypoints, insert_keypoints_sequence
from constants import DATA_PATH, FRAME_ACTIONS_PATH, ROOT_PATH

def create_keypoints(frames_path, save_path):
    '''
    ### CREAR KEYPOINTS PARA UNA PALABRA
    Recorre la carpeta de frames de la palabra y guarda sus keypoints en `save_path`
    '''
    data = pd.DataFrame([])
    
    with Holistic() as model_holistic:
        for n_sample, sample_name in enumerate(os.listdir(frames_path), 1):
            sample_path = os.path.join(frames_path, sample_name)
            keypoints_sequence = get_keypoints(model_holistic, sample_path)
            data = insert_keypoints_sequence(data, n_sample, keypoints_sequence)

    data.to_hdf(save_path, key="data", mode="w")

if __name__ == "__main__":
    words_path = os.path.join(ROOT_PATH, FRAME_ACTIONS_PATH, "prueba")
    
    # GENERATE KEYPOINTS FOR ALL WORDS
    # for word_name in os.listdir(words_path):
    #     word_path = os.path.join(words_path, word_name)
    #     hdf_path = os.path.join(DATA_PATH, f"{word_name}.h5")
    #     print(f'Creating keypoints for "{word_name}"...')
    #     create_keypoints(word_path, hdf_path)
    #     print("Keypoints created!")
    
    # GENERATE KEYPOINTS FOR A SINGLE WORD
    word_name = "hola"
    word_path = os.path.join(words_path, word_name)
    hdf_path = os.path.join(DATA_PATH, f"{word_name}.h5")
    create_keypoints(word_path, hdf_path)
    print(f"Keypoints created!")
