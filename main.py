from Counting import *
from Preprocess import *
from GenerateText import *

text_number = input('Write your text number which you want:\n')
tw, l = read_preprocess_files()
pd = simple_learner(tw, l)
generate(int(text_number), pd, l)