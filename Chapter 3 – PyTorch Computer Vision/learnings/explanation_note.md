### 🔸 [`torchvision`](https://www.learnpytorch.io/03_pytorch_computer_vision/)

* **What it is:** A library built on top of PyTorch for working with images (computer vision tasks).
* **Why it’s useful:** It gives you **ready-made tools** like datasets, models, and image transforms so you don’t have to build everything from scratch.

---

### 🔹 `torchvision.datasets`

* **What it does:** Lets you easily **download and load popular image datasets** (like MNIST, CIFAR10, ImageNet).
* **Why it’s useful:** Saves time—you don’t have to write code to fetch, clean, or organize image data. It's plug-and-play for training models.

---

### 🔹 `torchvision.models`

* **What it does:** Provides **pretrained models** (like ResNet, VGG, etc.) used in computer vision.
* **Why it’s useful:** You can use these models **as-is or fine-tune them** for your own problem, instead of training from scratch. Saves time, compute, and gets better results faster.

---

### 🔹 `torchvision.transforms`

* **What it does:** Lets you apply **image transformations** (e.g. resize, crop, rotate, normalize) to prepare your data for models.
* **Why it’s useful:** ML models need images to be in the right shape, size, and format. Transforms automate this, and they can also help models generalize better via augmentation.

---

### 🔹 `torch.utils.data.Dataset`

* **What it does:** A base class to create your **own custom datasets**.
* **Why it’s useful:** If your data isn't from `torchvision.datasets`, you can still organize and load it in a way PyTorch understands.

---

### 🔹 `torch.utils.data.DataLoader`

* **What it does:** Loads data from a dataset in **mini-batches** and optionally shuffles it.
* **Why it’s useful:** Instead of loading one image at a time, you can load batches (faster for training) and make training more efficient and scalable.

