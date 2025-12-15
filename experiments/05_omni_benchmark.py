import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd

from src.prompts import SOLVE_PROMPT_OMNI
from src.utils import write_jsonl

df = pd.read_parquet("data/omni/omni.parquet")

messages = []
for i, row in df.iterrows():
    messages.append(
        {
            "custom_id": f"{row['id']}",
            "method": "POST",
            "url": "/v1/responses",
            "body": {
                "model": "o3-2025-04-16",
                "reasoning": {
                    "effort": "medium",
                },
                "instructions": SOLVE_PROMPT_OMNI,
                "input": f"{row['problem']}",
            },
        }
    )

#write_jsonl("data/omni/omni_benchmark_o3.jsonl", messages)



messages = []
for i, row in df.iterrows():
    req = {
        "systemInstruction": {
            "parts": [{"text": SOLVE_PROMPT_OMNI}]
        },
        "contents": [
            {
                "role": "user",
                "parts": [{
                    "text": f"{row['problem']}"
                }]
            }
        ],
        "generationConfig": {
            "thinkingConfig": {
                "thinkingBudget": 8192,
            }
        }
    }
    line = {"key": f"{row['id']}", "request": req}
    messages.append(line)

#write_jsonl("data/omni/omni_benchmark_gemini.jsonl", messages)

# from google import genai
# from google.genai import types

# client = genai.Client()

# uploaded = client.files.upload(
#     file="data/omni/omni_benchmark.jsonl",
#     config=types.UploadFileConfig(mime_type="jsonl"),
# )
# job = client.batches.create(
#     model="gemini-2.5-pro",
#     src=uploaded.name,
# )
