#!/bin/bash
mkdir tests
touch 0-lookup.py
touch 1-my_list.py && touch tests/1-my_list.txt
touch 2-is_same_class.py
touch 3-is_kind_of_class.py
touch 4-inherits_from.py
touch 5-base_geometry.py
touch 6-base_geometry.py
touch 7-base_geometry.py && touch tests/7-base_geometry.txt
touch 8-rectangle.py
touch 9-rectangle.py
touch 10-square.py
touch 11-square.py
for i in {0..11}
do
    touch $i-main.py
done
chmod u+x *.py
