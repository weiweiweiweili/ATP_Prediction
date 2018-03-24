import application
import pandas as pd
import pickle

def test_predict():
	"""Test model prediction"""
	
	# Create a row of data and run prediction.
	# Set difference to be 0 such that the winning odd is expected to be 0.5.
	user_inputs = pd.DataFrame(index=[0], columns=['player_ht_diff', 'player_age_diff', 'player_rank_diff', 'player_rank_points_diff',
                                                       'surface_clay', 'surface_grass', 'surface_hard', 'tourney_level_A', 'tourney_level_G', 'tourney_level_M'])
	user_inputs.loc[0] = pd.Series({'player_ht_diff': 0, 'player_age_diff': 0, 'player_rank_diff': 0, 'player_rank_points_diff': 0,
                                        'surface_clay': 1, 'surface_grass': 0, 'surface_hard': 0, 'tourney_level_A': 1, 'tourney_level_G': 0, 'tourney_level_M': 0})

	#run model
	filename = 'finalized_model.pickle'
    loaded_model = pickle.load(open(filename, 'rb'))
	result = loaded_model.predict_proba(user_inputs)
	player1_win = result[:,0]

	# Check if output is indeed 0.5.
	assert player1_win==0.5
