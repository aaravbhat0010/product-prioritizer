from flask import Flask, render_template_string, request

from prioritize import prioritize

app = Flask(__name__)
PAGE = """
<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Product Prioritizer</title>
<h1>Product Prioritizer</h1>
<p>Use customer feedback to decide what to investigate first.</p>
<form method="post">
    <label for="goal">Product goal</label><br>
    <input id="goal" name="goal" value="{{ goal }}" required><br><br>
    <label for="feedback">Customer feedback</label><br>
    <textarea id="feedback" name="feedback" rows="6" cols="40"
              required>{{ feedback }}</textarea><br><br>
    <button type="submit">Prioritize</button>
</form>
{% if result %}
    <h2>Recommendation</h2>
    <div style="white-space: pre-wrap">{{ result }}</div>
{% endif %}
{% if error %}<p role="alert">{{ error }}</p>{% endif %}
"""


@app.route("/", methods=["GET", "POST"])
def home():
    goal = request.form.get("goal", "").strip()
    feedback = request.form.get("feedback", "").strip()
    result = error = ""
    if request.method == "POST":
        if goal and feedback:
            try:
                result = prioritize(goal, feedback)
            except (OSError, ValueError, KeyError):
                error = "Could not get a reply. Check that Ollama is open and the model is downloaded."
        else:
            error = "Enter both a product goal and customer feedback."
    return render_template_string(
        PAGE, goal=goal, feedback=feedback, result=result, error=error
    )


if __name__ == "__main__":
    app.run()
