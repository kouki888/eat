from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
COLUMNS = ['菜單名稱','食材','烹飪方式','成本','建議售價']
def load_menu():
    path = ROOT / 'data' / 'menu.csv'
    if not path.exists():
        return pd.DataFrame(columns=COLUMNS)
    df = pd.read_csv(path, encoding='utf-8-sig')
    if not set(COLUMNS).issubset(df.columns):
        raise ValueError('CSV 缺少必要欄位')
    return df
