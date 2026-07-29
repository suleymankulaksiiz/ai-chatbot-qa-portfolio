import json
from pathlib import Path


class TestMetrics:

    total_tests = 0
    passed_tests = 0
    failed_tests = 0
    scores = []
    response_times = []


    @classmethod
    def add_result(cls, score, response_time, passed):

        cls.total_tests += 1

        cls.scores.append(score)

        cls.response_times.append(response_time)


        if passed:
            cls.passed_tests += 1
        else:
            cls.failed_tests += 1



    @classmethod
    def report(cls):

        average_score = (
            sum(cls.scores) / len(cls.scores)
            if cls.scores
            else 0
        )


        average_time = (
            sum(cls.response_times) / len(cls.response_times)
            if cls.response_times
            else 0
        )


        success_rate = (
            (cls.passed_tests / cls.total_tests) * 100
            if cls.total_tests
            else 0
        )


        return {

            "total_tests": cls.total_tests,

            "passed_tests": cls.passed_tests,

            "failed_tests": cls.failed_tests,

            "success_rate": f"{round(success_rate,2)}%",

            "average_score": round(
                average_score,
                2
            ),

            "average_response_time": round(
                average_time,
                2
            )
        }



    @classmethod
    def save_json(cls):

        report = cls.report()


        reports_path = Path("reports")

        reports_path.mkdir(
            exist_ok=True
        )


        file_path = reports_path / "metrics_report.json"


        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                report,
                file,
                indent=4
            )


        return file_path