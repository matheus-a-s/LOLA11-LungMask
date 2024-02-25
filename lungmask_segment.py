import numpy as np
import torch, os, time
import SimpleITK as sitk
from lungmask import LMInferer

input_folder = "LOLA11_NII/"
output_folder = "LOLA11_PRED2/"

inferer = LMInferer(modelname='LTRCLobes')

def lobes_segmentation(input_path):
    input_image = sitk.ReadImage(input_path)

    start_time = time.time()
    segmentation = inferer.apply(input_image)
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    print(f"Segmentação concluída para {input_path}. Tempo total: {elapsed_time:.2f} segundos")

    return sitk.GetImageFromArray(segmentation.astype(np.uint8))

def main():
    print("Torch using CUDA:", torch.cuda.is_available())

    os.makedirs(output_folder, exist_ok=True)
    input_files = os.listdir(input_folder)

    for input_file in input_files:
        if input_file.endswith(".nii"):
            input_path = os.path.join(input_folder, input_file)
            output_path = os.path.join(output_folder, input_file.replace(".nii", "-pred.nii"))

            pred_image = lobes_segmentation(input_path)
            sitk.WriteImage(pred_image, output_path)

    print("Segmentação concluída para todos os exames na pasta.")

if __name__ == "__main__":
    main()