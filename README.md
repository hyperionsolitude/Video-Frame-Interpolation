# Video Frame Interpolation (24 to 30 fps)

Authors: [Utku Acar](https://github.com/hyperionsolitude)

## Highlights
This project based on [IFRNET](https://github.com/ltkong218/IFRNet)

## YouTube Demos
[[4K60p] うたわれるもの 偽りの仮面 OP フレーム補間+超解像 (IFRnetとReal-CUGAN)](https://www.youtube.com/watch?v=tV2imgGS-5Q)

[[4K60p] 天神乱漫 -LUCKY or UNLUCKY!?- OP (IFRnetとReal-CUGAN)](https://www.youtube.com/watch?v=NtpJqDZaM-4)

[RIFE IFRnet 比較](https://www.youtube.com/watch?v=lHqnOQgpZHQ)

[IFRNet frame interpolation](https://www.youtube.com/watch?v=ygSdCCZCsZU)

## Preparation
1. Install Ubuntu (tested on 22.04.1).
2. Install git.
<pre>
<code>$ sudo apt update</code>
<code>$ sudo apt install git</code>
</pre>
3. Checkout this repo to your machine.
<pre>
<code>$ git clone https://github.com/hyperionsolitude/Video-Frame-Interpolation</code>
</pre>
4. Install Anaconda with following steps at [this link](https://www.hostinger.com/tutorials/how-to-install-anaconda-on-ubuntu/).
<pre>
<code>$ sudo apt-get update</code>
<code>$ cd /tmp</code>
<code>$ sudo apt-get install wget</code>
<code>$ wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh</code>
<code>$ bash Anaconda3-2022.05-Linux-x86_64.sh</code>
<code>$ source ~/.bashrc</code>
</pre>
5. Create an Anaconda environment with Python 3.6.13 named as vidint.
<pre>
<code>$ conda create -n vidint python=3.6 -y</code>
</pre>
6. Activate Anaconda environment named as vidint previous step.
<pre>
<code>$ conda activate vidint</code>
</pre>
7. Install required python libraries from requirements.txt
<pre>
<code>$ cd ./Video-Frame-Interpolation</code>
<code>$ pip install -r requirements.txt</code>
</pre>
8. Install cupy library.
<pre>
<code>$ conda install -c conda-forge cupy</code>
</pre>
## Download Pre-trained Models and Play with Demos

1. Download our pre-trained models in this [link](https://www.dropbox.com/sh/hrewbpedd2cgdp3/AADbEivu0-CKDQcHtKdMNJPJa?dl=0), and then put file <code> checkpoints</code> into the root dir.
2. Change directory to the path of Video-Frame-Interpolation.
<pre>
<code>$ cd ~/Video-Frame-Interpolation</code>
</pre>
3. Create a sample of 30 fps video with processing 24 fps video via running test.sh.
<pre>
<code>$ ./test.sh</code>
</pre>
## Training on Vimeo90K Triplet Dataset for 2x Frame Interpolation
1. Download training and test datasets: [Vimeo90K](http://toflow.csail.mit.edu/), [UCF101](https://liuziwei7.github.io/projects/VoxelFlow), [SNU-FILM](https://myungsub.github.io/CAIN/), [Middlebury](https://vision.middlebury.edu/flow/data/), [GoPro](https://seungjunnah.github.io/Datasets/gopro.html) and [Adobe240](http://www.cs.ubc.ca/labs/imager/tr/2017/DeepVideoDeblurring/).
2. Set the right dataset path on your machine.
3. Run this script to generate optical flow pseudo label
<pre><code>$ python generate_flow.py</code></pre>

4. Then, start training by executing one of the following commands with selected model
<pre><code>$ python -m torch.distributed.launch --nproc_per_node=4 train_vimeo90k.py --world_size 4 --model_name 'IFRNet' --epochs 300 --batch_size 6 --lr_start 1e-4 --lr_end 1e-5</code>
<code>$ python -m torch.distributed.launch --nproc_per_node=4 train_vimeo90k.py --world_size 4 --model_name 'IFRNet_L' --epochs 300 --batch_size 6 --lr_start 1e-4 --lr_end 1e-5</code>
<code>$ python -m torch.distributed.launch --nproc_per_node=4 train_vimeo90k.py --world_size 4 --model_name 'IFRNet_S' --epochs 300 --batch_size 6 --lr_start 1e-4 --lr_end 1e-5</code></pre>

## Benchmarks for 2x Frame Interpolation
To test running time and model parameters, you can run
<pre><code>$ python benchmarks/speed_parameters.py</code></pre>

To test frame interpolation accuracy on Vimeo90K, UCF101 and SNU-FILM datasets, you can run
<pre><code>$ python benchmarks/Vimeo90K.py</code>
<code>$ python benchmarks/UCF101.py</code>
<code>$ python benchmarks/SNU_FILM.py</code></pre>

## Training on GoPro Dataset for 8x Frame Interpolation
1. Start training by executing one of the following commands with selected model
<pre><code>$ python -m torch.distributed.launch --nproc_per_node=4 train_vimeo90k.py --world_size 4 --model_name 'IFRNet' --epochs 300 --batch_size 6 --lr_start 1e-4 --lr_end 1e-5</code>
<code>$ python -m torch.distributed.launch --nproc_per_node=4 train_vimeo90k.py --world_size 4 --model_name 'IFRNet_L' --epochs 300 --batch_size 6 --lr_start 1e-4 --lr_end 1e-5</code>
<code>$ python -m torch.distributed.launch --nproc_per_node=4 train_vimeo90k.py --world_size 4 --model_name 'IFRNet_S' --epochs 300 --batch_size 6 --lr_start 1e-4 --lr_end 1e-5</code></pre>

Since inter-frame motion in 8x interpolation setting is relatively small, task-oriented flow distillation loss is omitted here. Due to the GoPro training set is a relatively small dataset, we suggest to use your specific datasets to train slow-motion generation for better results.

## ncnn Implementation of IFRNet

[ifrnet-ncnn-vulkan](https://github.com/nihui/ifrnet-ncnn-vulkan) uses [ncnn project](https://github.com/Tencent/ncnn) as the universal neural network inference framework. This package includes all the binaries and models required. It is portable, so no CUDA or PyTorch runtime environment is needed.

## Citation
<pre><code>@InProceedings{Kong_2022_CVPR, 
  author = {Kong, Lingtong and Jiang, Boyuan and Luo, Donghao and Chu, Wenqing and Huang, Xiaoming and Tai, Ying and Wang, Chengjie and Yang, Jie}, 
  title = {IFRNet: Intermediate Feature Refine Network for Efficient Frame Interpolation}, 
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)}, 
  year = {2022}
}</code></pre>
