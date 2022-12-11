#!/bin/bash
rm -r outputs
rm -r imgs
rm -r res_frames
mkdir outputs
mkdir imgs
mkdir res_frames

offset=0
second=100
maxframe=101
python3 vid2img.py
for n in {1..100} 
do
    python3 demo_24to30.py $n $offset
done
python3 reconstruction.py $maxframe $offset