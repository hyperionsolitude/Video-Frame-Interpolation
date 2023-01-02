#!/bin/bash
rm -r outputs;mkdir outputs
rm -r imgs;mkdir imgs
rm -r res_frames;mkdir res_frames
rm -r compare_frames;mkdir compare_frames
offset=0
maxframe=883 # Total Frame Number of the video
comp=220
python3 vid2img.py
for n in {1..882} # 0 to Total Frame Number of the video -1
do
    python3 demo_24to30.py $n $offset
done
python3 reconstruction.py $maxframe $offset
for n in {1..220} 
do
    python3 performance_test.py $n $offset
done

python3 per_pixel_loss.py $comp