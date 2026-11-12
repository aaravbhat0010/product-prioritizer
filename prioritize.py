import json
from urllib.request import Request, urlopen


def prioritize(goal, feedback):
    prompt = f"""Help a product manager decide what to investigate first.

Product goal: {goal}
Customer feedback: {feedback}

Give four short sections: Priority, Evidence, Metric, and Open question.
Pick one issue and explain how it connects to the goal. Quote the exact
feedback behind the choice, name one metric, and say what data to check.
Treat frequency and impact as unknown. Use plain text headings.
"""
    payload = {"model": "qwen3:4b-instruct", "prompt": prompt, "stream": False}
    request = Request(
        "http://localhost:11434/api/generate",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urlopen(request, timeout=120) as response:
        return json.load(response)["response"]


if __name__ == "__main__":
    goal = input("Product goal: ").strip()
    feedback = input("Customer feedback (one line): ").strip()
    if not goal or not feedback:
        raise SystemExit("Enter both a product goal and customer feedback.")
    print(prioritize(goal, feedback))
