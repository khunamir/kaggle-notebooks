import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
df = pd.read_csv("/kaggle/input/reddit-vaccine-myths/reddit_vm.csv")

df.head()

df.describe()

df.columns
pd.isnull(df['body']).sum()

df = df.dropna()

df.head()

df.head()['body']