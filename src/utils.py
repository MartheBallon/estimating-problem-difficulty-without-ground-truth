import json
from typing import Dict, List
import numpy as np
import pandas as pd


def write_jsonl(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        for item in data:
            json.dump(item, f, ensure_ascii=False)
            f.write('\n')


def load_jsonl(filepath) -> List[Dict]:
    with open(filepath, 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f]
    

def assign_random_score(df_entry):
    label = np.random.randint(1, 11)
    return int(label)

def flip_score(df_entry):
    if df_entry == 1:
        return 0
    elif df_entry == 0:
        return 1
    
