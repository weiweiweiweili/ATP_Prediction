from flask import Flask, render_template, request, redirect, url_for
import pickle
import pandas as pd
from sqlalchemy import create_engine
# from msiapp import app

application = Flask(__name__)

# player_info = pd.read_csv("player_info.csv")
# tournament_info = pd.read_csv("tournament_info.csv")

DB_URL = 'mysql+pymysql://root:mypassword@tryrds.cgc88eyrdecc.us-west-1.rds.amazonaws.com:3306/flask'

application.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
# silence the deprecation warning
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

engine = create_engine(DB_URL)

# player_info.to_sql(name='player_info', con = engine, if_exists = 'append', index=False)
player_info = pd.read_sql_query('select * from player_info', con=engine)

# tournament_info.to_sql(name='tournament_info', con = engine, if_exists = 'append', index=False)
tournament_info = pd.read_sql_query(
    'select * from tournament_info', con=engine)

# db = SQLAlchemy(application)


@application.route('/', methods=['GET'])
def result():
    return render_template('index.html')


@application.route('/', methods=['POST'])
def index_model():
	#add docstring and unit test
    if request.method == "POST":
        tournament = str(request.form['tourney_name'])
        player1 = str(request.form['player1name'])
        player2 = str(request.form['player2name'])

        # player_info = pd.read_csv("player_info.csv")
        player_ht_diff = float(player_info.loc[player_info.player_name == player1, 'player_ht']) - float(
            player_info.loc[player_info.player_name == player2, 'player_ht'])
        player_age_diff = float(player_info.loc[player_info.player_name == player1, 'player_age']) - float(
            player_info.loc[player_info.player_name == player2, 'player_age'])
        player_rank_diff = float(player_info.loc[player_info.player_name == player1, 'rank']) - float(
            player_info.loc[player_info.player_name == player2, 'rank'])
        player_rank_points_diff = float(player_info.loc[player_info.player_name == player1, 'rank_point']) - float(
            player_info.loc[player_info.player_name == player2, 'rank_point'])

        # tournament_info = pd.read_csv("tournament_info.csv")
        surface_clay = 0
        surface_grass = 0
        surface_hard = 0
        tourney_level_A = 0
        tourney_level_G = 0
        tourney_level_M = 0

        surface = str(tournament_info.loc[
                      tournament_info.tourney_name == tournament, 'surface'])
        tourney_level = str(tournament_info.loc[
                            tournament_info.tourney_name == tournament, 'tourney_level'])

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

        user_inputs = pd.DataFrame(index=[0], columns=['player_ht_diff', 'player_age_diff', 'player_rank_diff', 'player_rank_points_diff',
                                                       'surface_clay', 'surface_grass', 'surface_hard', 'tourney_level_A', 'tourney_level_G', 'tourney_level_M'])
        user_inputs.loc[0] = pd.Series({'player_ht_diff': player_ht_diff, 'player_age_diff': player_age_diff, 'player_rank_diff': player_rank_diff, 'player_rank_points_diff': player_rank_points_diff,
                                        'surface_clay': surface_clay, 'surface_grass': surface_grass, 'surface_hard': surface_hard, 'tourney_level_A': tourney_level_A, 'tourney_level_G': tourney_level_G, 'tourney_level_M': tourney_level_M})

        filename = 'finalized_model.pickle'
        loaded_model = pickle.load(open(filename, 'rb'))
        result = loaded_model.predict_proba(user_inputs)

        player1_win = 0.5
        player2_win = 0.5
        player1_win = result[:, 1]
        player2_win = result[:, 0]

        return render_template('results.html', odd=[player1_win, player2_win])

if __name__ == "__main__":
    application.run(debug=True)
