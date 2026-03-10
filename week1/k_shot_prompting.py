from dotenv import load_dotenv
from ollama import chat

load_dotenv()

NUM_RUNS_TIMES = 5

# TODO: Fill this in!
YOUR_SYSTEM_PROMPT = """
You are a highly obedient text processing assistant.
Your ONLY job is to follow the exact pattern shown in the examples below.
DO NOT THINK. DO NOT EXPLAIN. ONLY OUTPUT THE REVERSED WORD.

<example>
Input: apple
Output: elppa
</example>

<example>
Input: status
Output: sutats
</example>

<example>
Input: http
Output: ptth
</example>

<example>
Input: httpstatus
Output: sutatsptth
</example>
"""

USER_PROMPT = """
Reverse the order of letters in the following word. Only output the reversed word, no other text:

httpstatus
"""


EXPECTED_OUTPUT = "sutatsptth"


def test_your_prompt(system_prompt: str) -> bool:
    """Run the prompt up to NUM_RUNS_TIMES and return True if any output matches EXPECTED_OUTPUT.

    Prints "SUCCESS" when a match is found.
    """
    for idx in range(NUM_RUNS_TIMES):
        print(f"Running test {idx + 1} of {NUM_RUNS_TIMES}")
        response = chat(
            # DIKEMBALIKAN MENGGUNAKAN MISTRAL 12B
            model="mistral-nemo:12b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": USER_PROMPT},
            ],
            options={"temperature": 0.0},  # Temperature 0 agar Mistral tidak halusinasi
        )
        output_text = response.message.content.strip()
        if output_text.strip() == EXPECTED_OUTPUT.strip():
            print("SUCCESS")
            print(f"Jawaban AI: {output_text}")
            return True
        else:
            print(f"Expected output: {EXPECTED_OUTPUT}")
            print(f"Actual output: {output_text}")
    return False


if __name__ == "__main__":
    test_your_prompt(YOUR_SYSTEM_PROMPT)
