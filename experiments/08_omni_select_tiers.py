import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
import numpy as np

# Sample 50 Tier 1 problems and 50 Tier 4 problems

df = pd.read_parquet("results/omni/omni_with_performance.parquet")
df['difficulty'] = pd.qcut(df['difficulty'], 4, labels=['Tier 1', 'Tier 2', 'Tier 3', 'Tier 4'])
df_tier1 = df[df['difficulty'] == 'Tier 1'].sample(n=50, random_state=42)
df_tier4 = df[df['difficulty'] == 'Tier 4'].sample(n=50, random_state=42)

# Compute characteristics 

# number of correct answers in tier 1
num_correct_tier1 = df_tier1['o3_score'].sum()
num_correct_tier1_gemini = df_tier1['gemini_score'].sum()
# number of total problems in tier 1
total_tier1 = len(df_tier1)
# number of correct answers in tier 4
num_correct_tier4 = df_tier4['o3_score'].sum()
num_correct_tier4_gemini = df_tier4['gemini_score'].sum()
# number of total problems in tier 4
total_tier4 = len(df_tier4)

print(f"Tier 1: {num_correct_tier1} correct out of {total_tier1} ({num_correct_tier1/total_tier1*100:.2f}%)")
print(f"Tier 1 Gemini: {num_correct_tier1_gemini} correct out of {total_tier1} ({num_correct_tier1_gemini/total_tier1*100:.2f}%)")

print(f"Tier 4: {num_correct_tier4} correct out of {total_tier4} ({num_correct_tier4/total_tier4*100:.2f}%)")
print(f"Tier 4 Gemini: {num_correct_tier4_gemini} correct out of {total_tier4} ({num_correct_tier4_gemini/total_tier4*100:.2f}%)")


df_merged = pd.concat([df_tier1, df_tier4])
#df_merged.to_parquet("results/omni/omni_tier1_tier4_sample.parquet", index=False)