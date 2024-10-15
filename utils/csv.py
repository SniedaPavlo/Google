import pandas as pd

def save_csv(path, data, columns):
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(path, index=False, encoding='utf-8-sig')
    print(f'Data saved to {path}')
    
def parse_csv(file_path):
    df = pd.read_csv(file_path)
    
    data = df.to_dict(orient='records')
    return data
