import json
import os
import time
from pathlib import Path
import re

import pytest
import allure
from openai import OpenAI

from metrics import TestMetrics
from llm_judge import evaluate_response


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


MODEL_NAME = "gpt-4o-mini"


BASE_DIR = Path(__file__).resolve().parent.parent
PROMPT_FILE = BASE_DIR / "prompts" / "llm-test-prompts.json"



def load_test_prompts():

    with open(
        PROMPT_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



def validate_bullet_format(answer, expected_count):

    lines = [
        line.strip()
        for line in answer.split("\n")
        if line.strip()
    ]


    assert len(lines) > 0, (
        "Response is empty"
    )


    # İlk satır mutlaka bullet olmalı
    assert re.match(
        r"^[-*•]\s+",
        lines[0]
    ), (
        f"Response contains extra text before bullets: {lines[0]}"
    )


    bullet_lines = [
        line
        for line in lines
        if re.match(
            r"^[-*•]\s+",
            line
        )
    ]


    # Bullet sayısı kontrolü
    assert len(bullet_lines) == expected_count, (

        f"Expected {expected_count} bullet points "
        f"but got {len(bullet_lines)}"

    )


    # Ekstra açıklama kontrolü
    assert len(lines) == len(bullet_lines), (

        "Response contains additional non-bullet text"

    )


    for line in bullet_lines:


        # Markdown bold kontrolü
        assert not line.startswith("**"), (

            f"Unexpected markdown formatting: {line}"

        )


    return True




@allure.title("{test_case[id]} - LLM Response Quality Test")
@pytest.mark.parametrize(
    "test_case",
    load_test_prompts()
)
def test_llm_response_quality(test_case):


    with allure.step("Send prompt to OpenAI model"):

        start_time = time.time()


        response = client.chat.completions.create(

            model=MODEL_NAME,

            messages=[
                {
                    "role": "user",
                    "content": test_case["prompt"]
                }
            ],

            temperature=0
        )


        response_time = round(
            time.time() - start_time,
            2
        )



    answer = response.choices[0].message.content



    print("\n========== AI RESPONSE ==========")
    print("TEST CASE:", test_case["id"])
    print(answer)
    print("================================")




    with allure.step("Validate LLM response"):


        assert answer is not None

        assert len(answer.strip()) > 0




    with allure.step("Format validation"):


        prompt = test_case["prompt"].lower()


        expected_bullet_count = None


        if "exactly three bullet points" in prompt:

            expected_bullet_count = 3


        elif "three benefits" in prompt:

            expected_bullet_count = 3


        elif "exactly five bullet points" in prompt:

            expected_bullet_count = 5


        elif "five bullet points" in prompt:

            expected_bullet_count = 5




        if expected_bullet_count:


            validate_bullet_format(

                answer,

                expected_bullet_count

            )





    with allure.step("AI Judge Evaluation"):


        evaluation = evaluate_response(

            prompt=test_case["prompt"],

            response=answer,

            expected=test_case["expected"]

        )





    with allure.step("Attach test details to Allure report"):


        attachments = {


            "Test Case ID": test_case["id"],

            "Category": test_case["category"],

            "User Prompt": test_case["prompt"],

            "Expected Result": test_case["expected"],

            "AI Response": answer,

            "AI Quality Score": str(evaluation["score"]),

            "AI Quality Level": evaluation["quality"],

            "AI Judge Reason": evaluation["reason"],

            "Response Time": f"{response_time}s"

        }




        for name, content in attachments.items():


            allure.attach(

                str(content),

                name=name,

                attachment_type=allure.attachment_type.TEXT

            )





    with allure.step("Validate AI Quality Score"):


        test_passed = evaluation["score"] >= 3



        TestMetrics.add_result(

            score=evaluation["score"],

            response_time=response_time,

            passed=test_passed

        )



        assert test_passed, (

            f"LLM quality score too low: "

            f"{evaluation['score']} - "

            f"{evaluation['reason']}"

        )





    print("\n==============================")

    print("TEST CASE:", test_case["id"])

    print("CATEGORY:", test_case["category"])

    print("RESPONSE TIME:", response_time, "seconds")

    print("SCORE:", evaluation["score"])

    print("QUALITY:", evaluation["quality"])

    print("REASON:", evaluation["reason"])

    print("==============================")






def teardown_module():


    report = TestMetrics.report()



    print("\n==============================")
    print("LLM TEST SUMMARY")
    print("==============================")


    for key, value in report.items():

        print(
            f"{key}: {value}"
        )


    print("==============================")