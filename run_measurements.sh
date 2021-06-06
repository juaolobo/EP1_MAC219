#! /bin/bash

set -o xtrace

MEASUREMENTS=10
ITERATIONS=10
INITIAL_SIZE=16

SIZE=$INITIAL_SIZE

NAMES=('mandelbrot_seq' 'mandelbrot_seq_SEM' 'mandelbrot_pth' 'mandelbrot_omp')

make
mkdir results

for NAME in ${NAMES[@]}; do
    mkdir results/$NAME

    if [ "$NAME" != "mandelbrot_seq" ] && [ "$NAME" != "mandelbrot_seq_SEM" ]
        then
            for ((j=1; j<=32; j=j*2)) do
                export OMP_NUM_THREADS=$j
                SIZE=$INITIAL_SIZE
                for ((i=1; i<=$ITERATIONS; i++)); do
                        sudo perf stat -r $MEASUREMENTS ./$NAME -2.5 1.5 -2.0 2.0 $SIZE >> full$j.log 2>&1
                        sudo perf stat -r $MEASUREMENTS ./$NAME -0.8 -0.7 0.05 0.15 $SIZE >> seahorse$j.log 2>&1
                        sudo perf stat -r $MEASUREMENTS ./$NAME 0.175 0.375 -0.1 0.1 $SIZE >> elephant$j.log 2>&1
                        sudo perf stat -r $MEASUREMENTS ./$NAME -0.188 -0.012 0.554 0.754 $SIZE >> triple_spiral$j.log 2>&1
                        SIZE=$(($SIZE * 2))
                done
            done
    else
        for ((i=1; i<=$ITERATIONS; i++)); do
            sudo perf stat -r $MEASUREMENTS ./$NAME -2.5 1.5 -2.0 2.0 $SIZE >> full.log 2>&1
            sudo perf stat -r $MEASUREMENTS ./$NAME -0.8 -0.7 0.05 0.15 $SIZE >> seahorse.log 2>&1
            sudo perf stat -r $MEASUREMENTS ./$NAME 0.175 0.375 -0.1 0.1 $SIZE >> elephant.log 2>&1
            sudo perf stat -r $MEASUREMENTS ./$NAME -0.188 -0.012 0.554 0.754 $SIZE >> triple_spiral.log 2>&1
            SIZE=$(($SIZE * 2))
        done
    fi

    SIZE=$INITIAL_SIZE

    mv *.log results/$NAME
    rm output.ppm
done