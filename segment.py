import torch
import nibabel as nib
from totalsegmentator.python_api import totalsegmentator

input_path = "LOLA11_NII/lola11-01.nii"
output_path = "LOLA11_GT/lola11-01-GT.nii"

if __name__ == "__main__":
    print(torch.cuda.is_available())

    # option 1: provide input and output as file pathes
    totalsegmentator(input_path, output_path, task="lung_vessels")

    # option 2: provide input and output as nifti image objects
    # input_img = nib.load(input_path)
    # output_img = totalsegmentator(input_img, task="lung_vessels")
    # nib.save(output_img, output_path)