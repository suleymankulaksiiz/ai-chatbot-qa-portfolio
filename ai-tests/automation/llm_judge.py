from openai import OpenAI
import os
import json


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)



def evaluate_response(
        prompt,
        response,
        expected
):


    judge_prompt = f"""

You are a strict AI Quality Assurance evaluator.

Your task is to evaluate ONLY the AI response provided.
Do not assume missing problems.
Do not invent formatting issues.
Judge based only on the user prompt and expected behavior.


User Prompt:
{prompt}


Expected Behavior:
{expected}


AI Response:
{response}



Evaluation Rules:


5 = Fully correct.
- Follows the user instruction.
- Provides correct information.
- Matches required format.
- No unnecessary violations.


4 = Mostly correct.
- Small style differences only.
- No important requirement is broken.


3 = Acceptable.
- Minor deviation exists.
- Core requirement is satisfied.


2 = Partially correct.
- Response is mostly correct.
- But an important instruction is violated.


1 = Incorrect.
- Does not follow the user instruction.
- Contains wrong information.
- Completely fails the task.



Important QA Rules:


- If the response contains exactly the requested number of bullet points,
  do NOT reduce the score because bullet text is long.

- A valid bullet list must not be considered wrong only because
  bullet sentences are detailed.

- Do not complain about "extra text" unless there is clearly visible
  text outside the requested format.

- Do not invent formatting problems.

- Judge semantic quality separately from formatting.

- If format requirements are already satisfied,
  consider the response correct.



Return ONLY valid JSON.

No markdown.
No explanations.
No ```json.


JSON format:


{{
    "score": 5,
    "quality": "Perfect",
    "reason": "Response follows all requirements."
}}


"""



    result = client.chat.completions.create(

        model="gpt-4o-mini",

        temperature=0,

        messages=[

            {
                "role": "system",
                "content": (
                    "You are an AI QA evaluator. "
                    "Evaluate responses objectively "
                    "without inventing failures."
                )
            },

            {
                "role": "user",
                "content": judge_prompt
            }

        ]
    )



    content = result.choices[0].message.content.strip()



    try:

        return json.loads(content)


    except json.JSONDecodeError:


        return {

            "score": 1,

            "quality": "Invalid",

            "reason": (
                "AI Judge returned invalid JSON response."
            )

        }