# CAFNet: Circular Attention for Medical Image Segmentation

CAFNet applies circular attention mechanisms to enhance the segmentation of medical images.

## Experimental Setup (Using CVC-ClinicDB as an Example)

### 0. Environment Setup
- Ensure all dependencies in `requirements.txt` are met. It is recommended to create a virtual environment using the `requirements.txt`.

### 1. Data Preparation
- Download the original dataset and extract it to the `./data` folder.
- Run `random.division.py` to randomly split the dataset into training, validation, and test sets.
- Execute `process.py` to preprocess all data. This will generate `data_{train, val, test}.npy` and `mask_{train, val, test}.npy`.

### 2. Training
- Download the DeiT-base model from the DeiT repository and save it to the `./pretrained` folder.
- Download the ResNet-34 model from the timm PyTorch repository and save it to the `./pretrained` folder.
- Run `train.py`. You may need to adjust some parameters based on your specific settings.

### 3. Testing
- Run `test_isic.py` with the following command:
`python test_isic.py --ckpt_path='path_to_your_check_point.pth`
