import numpy as np
import pandas as pd

tl = pd.DataFrame()

for thisId in ids:
	harvest_user_timeline(twitter_api, user_id=thisId, max_results=200)