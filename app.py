from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
  return '''<h1>Flask is running on SerpentTalk.com</h1>
<p><a href="data"> Data generated from JSON formatted dictionary</a> &nbsp; &nbsp; |&nbsp; &nbsp; 
<a href="feeeedme"> Feeeedme- a Meal Planning Suggestion app</a></p>'''

@app.route('/data')
def names():
  data = {"names":['John', 'Jacob', 'Julie','Jennifer']}
  return jsonify(data)

@app.route('/feeeedme')
def meal_idea():
  main = open ("main_dish.txt", 'r').read()
  main_split= main.split('\n')
  starch = open ("starch.txt", 'r').read()
  starch_split= starch.split('\n')
  vegetable = open ("vegetable.txt", 'r').read()
  vegetable_split= vegetable.split('\n')
  main_dish = random.choice(main_split)
  starch_side = random.choice(starch_split)
  veggie_side = random.choice(vegetable_split)
  #return ' <p>How about {} with {} and {}".format(main_dish, starch_side,veggie_side)</p>'
  return 'How about ' + main_dish + ' with ' + starch_side + ' and ' + veggie_side + '?'

if __name__  == '__main__':
  app.run()
