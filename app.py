"""Flask App for the Water Overflow problem"""

import logging
from src.glass_controller import GlassController
from flask import Flask, request, render_template


logging.basicConfig(
    level=logging.DEBUG,
    format=f"%(asctime)s %(levelname)s: %(message)s",
)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/volume")
def get_volume():
    errors = []
    row = request.args.get("row")
    col = request.args.get("col")
    liters = request.args.get("liters")

    if not row or not col or not liters:
        errors.append("Input all fields")

    if col and row and int(col) > int(row):
        errors.append(f"row should be >= column")

    if errors:
        app.logger.error(errors)
        return render_template("errors.html", error_list=errors), 400

    row = int(row)
    col = int(col)
    liters = float(liters)

    glasses, result = GlassController(row, col, liters).run()
    app.logger.info(glasses)
    app.logger.info(f"result: {result}")

    return render_template(
        "results.html",
        row=row,
        col=col,
        liters=liters,
        result=result,
        glasses=glasses,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
