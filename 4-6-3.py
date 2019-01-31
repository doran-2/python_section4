import sys
import io
import numpy as np
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#렌덤으로 DataFrame 생성
df = pd.DataFrame(np.random.randint(1,45,size=(10,6)), columns=list('ABCDEF'))
print(df)

df.to_excel('C:/Python/section4/lotto.xlsx', index=False, header=False)
