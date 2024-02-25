import torch, os, time
import nibabel as nib
from totalsegmentator.python_api import totalsegmentator

input_folder = "LOLA11_NII/"
output_folder = "LOLA11_GT/"

def lobes_segmentation(input_path, output_path):
    start_time = time.time()
    totalsegmentator(input_path, output_path, ml=True, task="total", roi_subset=["lung_upper_lobe_left", "lung_lower_lobe_left", "lung_upper_lobe_right", "lung_middle_lobe_right", "lung_lower_lobe_right"])
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    print(f"Segmentação concluída para {input_path}. Tempo total: {elapsed_time:.2f} segundos")

def main():
    print("Torch using CUDA:", torch.cuda.is_available())

    os.makedirs(output_folder, exist_ok=True)
    input_files = os.listdir(input_folder)

    for input_file in input_files:
        if input_file.endswith(".nii"):
            input_path = os.path.join(input_folder, input_file)
            output_path = os.path.join(output_folder, input_file.replace(".nii", "-GT.nii"))

            lobes_segmentation(input_path, output_path)

    print("Segmentação concluída para todos os exames na pasta.")

if __name__ == "__main__":
    main()