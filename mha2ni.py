import SimpleITK as sitk

input_path = 'LOLA11'
output_path = 'LOLA11_NII'

mha_path = input_path + '/lola11-01.mha'
nii_path = output_path + '/lola11-01.nii'

img = sitk.ReadImage(mha_path)
sitk.WriteImage(img, nii_path)