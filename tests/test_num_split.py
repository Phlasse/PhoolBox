# -*- coding: UTF-8 -*-

# Import from standard library
import os
import mlproject
import pandas as pd
# Import from our lib
from PhoolBox.PrePhooling import num_split
import pytest


def test_num_split():
    stri_1 = "43 65 87 34 12 55 77"
    stri_2 = "66 77 88 99"
    exp_1 = ([34, 12],[43, 65, 87, 55, 77],[])
    exp_2 = ([66, 88], [77, 99], [])
    assert num_split(stri_1)== exp_1
    assert num_split(stri_2)== exp_2

# 48.865070 2.380009 48.235070 2.393409 ->70.00789153218594
