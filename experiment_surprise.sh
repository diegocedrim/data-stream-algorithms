#!/usr/bin/env bash

for ((i=1;i<=10;i++)); do
    echo "Running exact method: $i"
    mprof run --python python surprise_number.py -e > "out_exact_$i.txt"
done

VARIABLES=(10 50 100 200 500 1000)
for v in ${VARIABLES[@]}; do
    for ((i=1;i<=20;i++)); do
        echo "Running AMS method with ${v} variables: ${i}"
        mprof run --python python surprise_number.py -n ${v} > "out_ams_n_${v}_execution_${i}.txt"
    done
done