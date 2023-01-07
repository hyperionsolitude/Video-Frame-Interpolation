#!/bin/bash
rm -r outputs;mkdir outputs
rm -r imgs;mkdir imgs
rm -r res_frames;mkdir res_frames
rm -r compare_frames;mkdir compare_frames
offset=0
pathofsample="./samples/sample1.mp4"
framenumber=$(python3 vid2img.py $pathofsample)
maxframe="$((framenumber-1))"
demo="$((framenumber-2))"
comp="$((maxframe/4))"
for ((i=1; i <= $demo; i++));
do
    python3 demo_24to30.py $i $offset
done
python3 reconstruction.py $maxframe $offset
for ((j=1; j <= $comp; j++)); 
do
    python3 performance_test.py $j $offset
done

python3 per_pixel_loss.py $comp
python3 log_edit.py perframeloss.txt | tee statistics.txt