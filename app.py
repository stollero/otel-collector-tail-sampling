from random import randint
from flask import Flask

from opentelemetry import trace
from opentelemetry.trace.status import Status, StatusCode

# Acquire a tracer
tracer = trace.get_tracer("diceroller.tracer")

app = Flask(__name__)


@app.route("/rolldice")
def roll_dice():
    with tracer.start_as_current_span("roll_dice") as span:
        roll_result = roll()
        if roll_result == 6:
            span.set_status(Status(StatusCode.ERROR, "Rolled a 6"))
            return "Not Found", 404
        else:
            span.set_status(Status(StatusCode.OK, "Successful roll"))
            return str(roll_result)


def roll():
    # This creates a new span that's the child of the current one
    with tracer.start_as_current_span("roll") as rollspan:
        res = randint(1, 6)
        rollspan.set_attribute("roll.value", res)
        return res
