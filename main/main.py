#%% 데이터 API


from src.power_api import PowerAPI

# Create a new API object
api = PowerAPI()

# Define the API parameters
parameters = {
    'parameters': 'ALLSKY_SFC_SW_DWN',
    'userCommunity': 'SB',
    'tempAverage': 'DAILY',
    'outputList': 'JSON',
    'lat': '40',
    'lon': '-75',
    'start': '20220101',
    'end': '20220320',
}

# Make the API request
response = api.request_data("SinglePoint", parameters)

# Print the response
print(response)
# %%
