"""
Day 1 — LLM API Foundation
AICB-P1: AI Practical Competency Program, Phase 1

Instructions:
    1. Fill in every section marked with TODO.
    2. Do NOT change function signatures.
    3. Copy this file to solution/solution.py when done.
    4. Run: pytest tests/ -v
"""

import os
import time
from typing import Any, Callable
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
# ---------------------------------------------------------------------------
# Estimated costs per 1K OUTPUT tokens (USD) — update if pricing changes
# ---------------------------------------------------------------------------
COST_PER_1K_OUTPUT_TOKENS = {
    "gpt-4o": 0.010,
    "gpt-4o-mini": 0.0006,
}

OPENAI_MODEL = "gpt-4o"
OPENAI_MINI_MODEL = "gpt-4o-mini"

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

# ---------------------------------------------------------------------------
# Task 1 — Call GPT-4o
# ---------------------------------------------------------------------------
def call_openai(
    prompt: str,
    model: str = OPENAI_MODEL,
    temperature: float = 0.7,
    top_p: float = 0.9,
    max_tokens: int = 256,
) -> tuple[str, float]:

    
    start_time = time.time()
    """
    Call the OpenAI Chat Completions API and return the response text + latency.

    Args:
        prompt:      The user message to send.
        model:       The OpenAI model to use (default: gpt-4o).
        temperature: Sampling temperature (0.0 – 2.0).
        top_p:       Nucleus sampling threshold.
        max_tokens:  Maximum number of tokens to generate.

    Returns:
        A tuple of (response_text: str, latency_seconds: float).

    Hint:
        from openai import OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    """
    # # TODO: import OpenAI, create client, call chat.completions.create,
    # #       measure start/end time, return (response_text, latency)
    # raise NotImplementedError("Implement call_openai")
    respones = client.chat.completions.create(
        model = model,
        messages = [{"role" : "user", "content" : prompt }],
        temperature = temperature,
        top_p = top_p,
        max_tokens = max_tokens
    )
    
    end_time = time.time()
    latency = end_time - start_time
    
    return respones.choices[0].message.content, float(latency)

# ---------------------------------------------------------------------------
# Task 2 — Call GPT-4o-mini
# ---------------------------------------------------------------------------
def call_openai_mini(
    prompt: str,
    temperature: float = 0.7,
    top_p: float = 0.9,
    max_tokens: int = 256,
) -> tuple[str, float]:
    return call_openai(
        model = OPENAI_MINI_MODEL,
        prompt = prompt,
        temperature=temperature,
        top_p = top_p,
        max_tokens= max_tokens
    )
    """
    Call the OpenAI Chat Completions API using gpt-4o-mini and return the
    response text + latency.

    Args:
        prompt:      The user message to send.
        temperature: Sampling temperature (0.0 – 2.0).
        top_p:       Nucleus sampling threshold.
        max_tokens:  Maximum number of tokens to generate.

    Returns:
        A tuple of (response_text: str, latency_seconds: float).

    Hint:
        Reuse call_openai() by passing model=OPENAI_MINI_MODEL.
    """
    # # TODO: call call_openai with model=OPENAI_MINI_MODEL
    # raise NotImplementedError("Implement call_openai_mini")


# ---------------------------------------------------------------------------
# Task 3 — Compare GPT-4o vs GPT-4o-mini
# ---------------------------------------------------------------------------
def compare_models(prompt: str) -> dict:
    res_4o, lat_4o = call_openai(prompt)
    res_mini, lat_mini = call_openai_mini(prompt)

    #Cost Estimate
    estimated_cost = len(res_4o.split())/0.75
    cost_estimate = estimated_cost/1000 * COST_PER_1K_OUTPUT_TOKENS["gpt-4o"]
    return {
        "gpt4o_response" : res_4o,
        "mini_response" : res_mini,
        "gpt4o_latency" : lat_4o,
        "mini_latency" : lat_mini,
        "gpt4o_cost_estimate" : cost_estimate
    }
    
    """
    Call both gpt-4o and gpt-4o-mini with the same prompt and return a
    comparison dictionary.

    Args:
        prompt: The user message to send to both models.

    Returns:
        A dict with keys:
            - "gpt4o_response":      str
            - "mini_response":       str
            - "gpt4o_latency":       float
            - "mini_latency":        float
            - "gpt4o_cost_estimate": float  (estimated USD for the response)

    Hint:
        Cost estimate = (len(response.split()) / 0.75) / 1000 * COST_PER_1K_OUTPUT_TOKENS["gpt-4o"]
        (0.75 words ≈ 1 token is a rough approximation)
    """
    # # TODO: call call_openai and call_openai_mini, assemble and return the dict
    # raise NotImplementedError("Implement compare_models")


# ---------------------------------------------------------------------------
# Task 4 — Streaming chatbot with conversation history
# ---------------------------------------------------------------------------
def streaming_chatbot() -> None:
    history = []
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        
        history.append({"role": "user", "content": user_input})
        
        stream = client.chat.completions.create(
            model=OPENAI_MINI_MODEL,
            messages=history,
            stream=True
        )
        
        print("Assistant: ", end="", flush=True)
        assistant_reply = ""
        for chunk in stream:
            delta = chunk.choices[0].delta.content or ""
            print(delta, end="", flush=True)
            assistant_reply += delta
        print()
        
        history.append({"role": "assistant", "content": assistant_reply})
        # Giữ lại 3 lượt hội thoại cuối (mỗi lượt gồm user + assistant = 6 messages)
        # Hoặc 3 messages cuối tùy theo yêu cầu test. Ở đây mình giữ 3 entries cuối.
        history = history[-3:]
    """
    Run an interactive streaming chatbot in the terminal.

    Behaviour:
        - Streams tokens from OpenAI as they arrive (print each chunk).
        - Maintains the last 3 conversation turns in history.
        - Typing 'quit' or 'exit' ends the loop.

    Hints:
        - Keep a list `history` of {"role": ..., "content": ...} dicts.
        - Use stream=True in client.chat.completions.create() and iterate:
            for chunk in stream:
                delta = chunk.choices[0].delta.content or ""
                print(delta, end="", flush=True)
        - After each turn, append the assistant reply to history.
        - Trim history to the last 3 turns: history = history[-3:]
    """
    # # TODO: enter while-loop, read user input, stream response, maintain history
    # raise NotImplementedError("Implement streaming_chatbot")


# ---------------------------------------------------------------------------
# Bonus Task A — Retry with exponential backoff
# ---------------------------------------------------------------------------
def retry_with_backoff(
    fn: Callable,
    max_retries: int = 3,
    base_delay: float = 0.1,
) -> Any:
    for attempt in range(max_retries + 1):
        try:
            return fn()
        except Exception as e:
            if attempt == max_retries:
                raise e
            delay = base_delay * (2 ** attempt)
            time.sleep(delay)
    """
    Call fn(). If it raises an exception, retry up to max_retries times
    with exponential backoff (base_delay * 2^attempt).

    Args:
        fn:          Zero-argument callable to execute.
        max_retries: Maximum number of retry attempts.
        base_delay:  Initial delay in seconds before the first retry.

    Returns:
        The return value of fn() on success.

    Raises:
        The last exception raised by fn() after all retries are exhausted.
    """
    # # TODO: implement retry loop with exponential backoff
    # raise NotImplementedError("Implement retry_with_backoff")


# ---------------------------------------------------------------------------
# Bonus Task B — Batch compare
# ---------------------------------------------------------------------------
def batch_compare(prompts: list[str]) -> list[dict]:
    results = []
    for p in prompts:
        res = compare_models(p)
        res["prompt"] = p
        results.append(res)
    return results
    """
    Run compare_models on each prompt in the list.

    Args:
        prompts: List of prompt strings.

    Returns:
        List of dicts, each being the compare_models result with an extra
        key "prompt" containing the original prompt string.
    """
    # # TODO: iterate over prompts, call compare_models, add "prompt" key
    # raise NotImplementedError("Implement batch_compare")


# ---------------------------------------------------------------------------
# Bonus Task C — Format comparison table
# ---------------------------------------------------------------------------
def format_comparison_table(results: list[dict]) -> str:
    header = f"{'Prompt':<40} | {'GPT-4o Resp':<40} | {'Mini Resp':<40} | {'4o Lat':<10} | {'Mini Lat':<10}"
    separator = "-" * len(header)
    lines = [header, separator]
    
    for r in results:
        p = (r["prompt"][:37] + "...") if len(r["prompt"]) > 40 else r["prompt"]
        r4o = (r["gpt4o_response"][:37] + "...") if len(r["gpt4o_response"]) > 40 else r["gpt4o_response"]
        rmini = (r["mini_response"][:37] + "...") if len(r["mini_response"]) > 40 else r["mini_response"]
        
        line = f"{p:<40} | {r4o:<40} | {rmini:<40} | {r['gpt4o_latency']:<10.2f} | {r['mini_latency']:<10.2f}"
        lines.append(line)
        
    return "\n".join(lines)
    """
    Format a list of compare_models results as a readable text table.

    Args:
        results: List of dicts as returned by batch_compare.

    Returns:
        A formatted string table with columns:
        Prompt | GPT-4o Response | Mini Response | GPT-4o Latency | Mini Latency

    Hint:
        Truncate long text to 40 characters for readability.
    """
    # # TODO: build and return a formatted table string
    # raise NotImplementedError("Implement format_comparison_table")


# ---------------------------------------------------------------------------
# Entry point for manual testing
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    test_prompt = "Explain the difference between temperature and top_p in one sentence."
    print("=== Comparing models ===")
    result = compare_models(test_prompt)
    for key, value in result.items():
        print(f"{key}: {value}")

    print("\n=== Starting chatbot (type 'quit' to exit) ===")
    streaming_chatbot()

    # Thêm đoạn này vào cuối file để làm Bài tập 2.1
    # print("\n=== Thực hiện Bài tập 2.1: Thử nghiệm Temperature ===")
    # temperatures = [0.0, 0.5, 1.0, 1.5]
    # test_prompt = "Hãy kể cho tôi một sự thật thú vị về Việt Nam."

    # for temp in temperatures:
    #     response, latency = call_openai(test_prompt, temperature=temp)
    #     print(f"\n--- Kết quả với Temperature = {temp} ---")
    #     print(response)
    #     print(f"(Latency: {latency:.2f}s)")
