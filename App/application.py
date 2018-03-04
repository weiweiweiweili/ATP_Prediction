from flask import Flask, render_template, request, redirect, url_for
import pickle
import pandas as pd

app = Flask(__name__)
#from msiapp import application, db
#from msiapp.models import Track, City
#import requests

@app.route('/',methods=['GET'])
def index():
    """Main view that lists songs

    Create view into index page that uses data queried from Track database and
    inserts it into the msiapp/templates/index.html template

    :return: rendered html template

    """

    return render_template('index.html')

@app.route('/', methods=['POST'])
def model():

    """View that process a POST with new user input

    :return: redirect to result page
    """

    tournament = str(request.form['tourney_name'])
    player1 = str(request.form['player1name'])
    player2 = str(request.form['player2name'])

    player_info = pd.read_csv("player_info.csv")
    player_ht_diff = player_info['player_name'==player1]['player_ht'] - player_info['player_name'==player2]['player_ht']
    player_age_diff = player_info['player_name'==player1]['player_age'] - player_info['player_name'==player2]['player_age']
    player_rank_diff = player_info['player_name'==player1]['rank'] - player_info['player_name'==player2]['rank'] 
    player_rank_points_diff = player_info['player_name'==player1]['rank_point'] - player_info['player_name'==player2]['rank_point']

    tournament_info = pd.read_csv("tournament_info.csv")
    surface_clay = 0  
    surface_grass = 0
    surface_hard = 0  
    tourney_level_A = 0
    tourney_level_G = 0
    tourney_level_M = 0
    
    surface = tournament_info['tourney_name' == tournament]['surface']
    tourney_level = tournament_info['tourney_name' == tournament]['tourney_level']
    
    if surface == "Hard":
        surface_hard = 1
    elif surface == "Clay":
        surface_clay = 1
    else:
        surface_grass = 1

    if tourney_level == "A":
        tourney_level_A = 1
    elif tourney_level == "M":
        tourney_level_M = 1
    else:
        tourney_level_G = 1

    user_inputs = [player_ht_diff,player_age_diff,player_rank_diff,player_rank_points_diff, surface_clay, surface_grass, surface_hard, tourney_level_A, tourney_level_G, tourney_level_M]

    filename = 'finalized_model.pickle'
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict(user_inputs)
    
    return render_template('results.html')
    #return redirect(url_for('results.html'))

if __name__ == "__main__":
    app.run(debug=True)
