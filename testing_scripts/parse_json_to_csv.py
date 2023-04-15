import pandas as pd
import json

NUMBER_OF_FILES = 5

for i in range(1, NUMBER_OF_FILES + 1):

    data = json.load(open(str(i) + '_ue_metrics.json'))
    # df = pd.read_json(str(i) + '_ue_metrics.json', lines=True)
    df = pd.DataFrame(data["intervals"])
    df.to_csv(str(i) + '_ue_metrics.csv')


#df = pd.read_json('test.json')
#print(df)
#df.to_csv('test.csv')

