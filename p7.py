#p6.pyを時間でへんこうする

import time
import pickle
import sys

with open("prime_jisyo.pkl",mode='rb') as fi:
    prime_data=pickle.load(fi)

max_prime=prime_data[len(prime_data)]
n=max_prime

print(f"今、{max_prime}まで見つかっています\n次は何秒探しますか？")
jikan=int(input())

if jikan<=0:
    sys.exit(f"正の時間を入力してください")
else:
    print("始めます\n")
old=time.time()

kosuu=len(prime_data)
#max_primeの次の奇数から始める
while int( time.time() - old ) <= jikan:
    for i in range(n+2,n+4,2):
        c=0
        for t in range(1,len(prime_data)+1,1):
            x=prime_data[t]
            d=i%x
            if d==0:
                c=1
                break
        if c==0:
            kosuu+=1
            prime_data[kosuu]=i
    n+=2
#1つ素数を見つけた後に時間経過を判定するため、時間ぴったりになりにくい

with open("prime_jisyo.pkl","wb") as tf:
    pickle.dump(prime_data,tf)

print(f"2から{n}までに{len(prime_data)}個の素数が見つかりました!!")
#実行時間を表示する
print(f"{time.time()-old}秒かかったよ")
print(f"最後に見つけた素数は、{len(prime_data)}番目の{prime_data[len(prime_data)]}です\n")

# Excel 1048576
# https://tools.m-bsys.com/calculators/prime_number_generator.php で個数を確認