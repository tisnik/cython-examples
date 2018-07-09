width="2048"

OUTFILE="cython_linear_scale.times"
PREFIX="cython_linear_scale"

rm $OUTFILE

for height in $(seq 0 100 3500)
do
    echo "${width} x ${height}"
    echo -n "${height} " >> $OUTFILE
    /usr/bin/time --output $OUTFILE --append --format "%e %M" python3 run.py $width $height 255 > "${PREFIX}_${width}_${height}.ppm"
done
