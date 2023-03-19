import threading

from flask import Flask
from simulatorImpl.Simulator import Simulator

sim = Simulator()

app = Flask(__name__)

t1 = threading.Thread(target=sim.run_simulator)
t1.start()

@app.route("/")
def print_hi():
    return str(sim.get_temp())

