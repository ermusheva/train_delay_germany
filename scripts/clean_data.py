import pandas as pd

def clean_df(df: pd.DataFrame):

    df = df.copy()

    # Leave in data only well-known high speed and regional train types
    # high_speed_train_types = ['ICE', 'SBB', 'ME', 'IC', 'NJ', 'EN', 'TL', 'EST', 'D', 'TGV', 'EC', 'ECE', 'RJX', 'RJ', 'WB', 'ES']
    high_speed_train_types = ['ICE', 'IC']
    # regional_train_types = ['BRB', 'MEX',  'RE', 'IRE', 'RRB', 'RB', 'NBE', 'NWB', 'WFB', 'HLB', 'ENO', 'erx', 'ALX',  'R',  'STB', 'EVB']
    regional_train_types = ['RE', 'RB']
    # commuter_rail_types = ['S', 'SWE', 'FEX', 'STN', 'SAB', 'AKN', 'CB', 'HBX']
    allowed_train_types = high_speed_train_types + regional_train_types
    # Filter while handling possible NaN values
    df = df[df['train_type'].isin(allowed_train_types).fillna(False)]

    # Remove all canceled trains
    # df = df.drop(df[df['is_canceled']].index)
    # df = df.drop(columns='is_canceled')

    # Replace negative delays with 0
    df.loc[df['delay_in_min'] <0, 'delay_in_min'] = 0

    # Group data from railway stations to cities
    # Create 'city' column from 'station'
    df['city'] = (
        df['station']
        .str.replace('Hbf', '', regex=False)                 # Remove "Hbf"
        .str.replace('Flughafen', '', regex=False)           # Remove " Flughafen"
        .str.replace(r'Berlin.*', 'Berlin', regex=True)      # Replace any Berlin station with "Berlin" and other big cities
        .str.replace(r'München.*', 'München', regex=True)      
        .str.replace(r'Dresden.*', 'Dresden', regex=True)      
        .str.replace(r'Frankfurt\(Main\).*', 'Frankfurt(Main)', regex=True)      
        .str.replace(r'Köln.*', 'Köln', regex=True)          
        .str.replace(r'Fürth.*', 'Fürth', regex=True)
        .str.replace(r'Hamburg.*', 'Hamburg', regex=True) 
        .str.replace(r'Münster.*', 'Münster', regex=True)   
        .str.replace(r'BER.*', 'Berlin', regex=True)         # Replace any BER station with "Berlin"
        .str.strip()                                         # Remove extra spaces
        ) 
    return df
