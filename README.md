# Estimating problem difficulty without ground truth using Large Language Model comparisons
This repository contains the code to 'Estimating problem difficulty without ground truth using Large Language Model comparisons' by Marthe Ballon, Andres Algaba, Brecht Verbeken and Vincent Ginis (https://arxiv.org/pdf/2512.14220). 

## System requirements
```bash
python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python experiments/01_cmcqrd_create_pairs.py
```

## Overview of the data
1. The original three datasets used in the paper are available at
   - JEE Advanced Maths 2024 by the Joint Implementation Committee 2024 (https://jeeadv.ac.in/archive.html) 
   - The Cambridge MCQ Reading Dataset by Mullooly et al. 2023 (https://englishlanguageitutoring.com/datasets/cambridge-multiple-choice-questions-reading-dataset)
   - Omni-Math by Gao et al. 2024 (https://huggingface.co/datasets/KbsdJames/Omni-MATH)
  
2. Omni-MATH-2 is available at (https://huggingface.co/datasets/martheballon/Omni-MATH-2) 
    
2. All data necessary to replicate the experiments is available at (https://zenodo.org/records/17523641)

data/

&nbsp;&nbsp;&nbsp;&nbsp;jee/
- jee.parquet

&nbsp;&nbsp;&nbsp;&nbsp;cmcqrd/
- cmcqrd.parquet 
  
&nbsp;&nbsp;&nbsp;&nbsp;omni/
   - omni.parquet (the subset of algebra questions from Omni-Math-2 that do not contain any proofs, estimations or images)

  
results/

&nbsp;&nbsp;&nbsp;&nbsp;jee/
   - jee_pairs_o3_results.jsonl
   - jee_pairs_gemini_results.jsonl

&nbsp;&nbsp;&nbsp;&nbsp;cmcqrd/
   - cmcqrd_pairs_o3_results.jsonl
   - cmcqrd_pairs_gemini_results.jsonl
   - cmcqrd_o3_label_results.jsonl
   - cmcqrd_gemini_label_results.jsonl
   - all_bt_with_difficulty_cmcqrd_oss.parquet


&nbsp;&nbsp;&nbsp;&nbsp;omni/
   - omni_pairs_o3_results.jsonl
   - omni_pairs_gemini_results.jsonl
   - omni_o3_label_results.jsonl
   - omni_gemini_label_results.jsonl
   - omni_o3_benchmark_results.jsonl
   - omni_o3_benchmark_judged.jsonl
   - omni_gemini_benchmark_results.jsonl
   - omni_gemini_benchmark_judged.jsonl
   - all_bt_with_difficulty_omni_oss.parquet


&nbsp;&nbsp;&nbsp;&nbsp;omni_non_linear/
- omni_non_linear_pairs_o3_results.jsonl
- omni_non_linear_pairs_gemini_results.jsonl


## Instructions for the data
Download the datafiles at the links provided above and insert them into the data/results folder indicated above. Then, execute the code in the experiments folder depending on the task you want to replicate and insert the output in the correct folder.


## Overview of the code

experiments/
- 01_cmcqrd_create_pairs.py
- 01_jee_create_pairs.py
- 01_omni_create_pairs.py
- 02_cmcqrd_batch_pairs.py
- 02_jee_batch_pairs.py
- 02_omni_batch_pairs.py
- 03_cmcqrd_process_results.py
- 03_jee_process_results.py
- 03_omni_process_results.py
- 04_cmcqrd_compute_bt.py
- 04_jee_compute_bt.py
- 04_omni_compute_bt.py
- 05_omni_benchmark.py
- 06_cmcqrd_label_by_llm.py
- 06_omni_label_by_llm.py
- 07_omni_add_noise_gemini.py
- 07_omni_add_noise_o3.py
- 08_select_tiers.py --> This file creates a new subset that only contains Tier 1 and Tier 4 problems of Omni-MATH-2, execute experiments 01-04 again for this set

src/
- figures_main.ipynb
- figures_appendix.ipynb    
- bt.py
- pairs.py
- prompts.py
- utils.py


## Instructions for the code
A detailed description on how to create the figures is provided in figures_main.ipynb and figures_appendix.ipynb. The python scripts 01-04 in experiments/ compute BT scores with OpenAI o3 and Gemini 2.5 Pro, for all three datasets. The scripts 05-08 create additional data to support the figures. 





