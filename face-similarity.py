#Membuat Fungsi untuk Membandingkan Wajah
#install terlebih dahulu pip install face_recognition
#git clone https://github.com/cubiq/ComfyUI_FaceAnalysis.git


import face_recognition
import os

def load_and_encode_image(image_path):
    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)
    if len(encodings) > 0:
        return encodings[0]
    else:
        return None

def compare_faces(img1_path, img2_path):
    img1_encoding = load_and_encode_image(img1_path)
    img2_encoding = load_and_encode_image(img2_path)
    
    if img1_encoding is None or img2_encoding is None:
        return None  # Tidak ada wajah yang terdeteksi di salah satu gambar

    # Menghitung jarak antara dua embedding wajah (euclidean distance)
    distance = face_recognition.face_distance([img1_encoding], img2_encoding)
    
    # Konversi jarak ke skor kesamaan (semakin kecil jaraknya, semakin mirip)
    similarity_score = 1 - distance[0]
    return similarity_score

def compare_directories(dir1, dir2):
    for img1 in os.listdir(dir1):
        for img2 in os.listdir(dir2):
            img1_path = os.path.join(dir1, img1)
            img2_path = os.path.join(dir2, img2)
            
            similarity_score = compare_faces(img1_path, img2_path)
            if similarity_score is not None:
                print(f"Similarity between {img1} and {img2}: {similarity_score}")
            else:
                print(f"No face detected in {img1} or {img2}")

# Jalankan perbandingan
compare_directories('FOTO_SATU', 'FOTO_DUA')
