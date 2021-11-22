if 3 > 2:
    print('It works!')

if 5 > 2:
    print('5 is indeed greater than 2')
else:
    print('5 is not greater than 2')
# 
name = 'Sonja'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Sonja':
    print('Hey Sonja!')
else:
    print('Hey anonymous!')
# 
volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")

# ボリュームが大きすぎたり小さすぎたりしたら変更する
if volume < 20 or volume > 80:
    volume = 50
    print("That's better!")

# 自作関数1
def hi_old(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')

# 自作関数2
def hi(name):
    print('Hi ' + name + '!')

hi("Rachel")
hi("Koki") 

# loop1
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']

for name in girls:
    hi(name)
    print('Next girl')

# loop2 ※開始に指定した数値は含まれて、終了に指定した値は含まれないのです。
for i in range(1, 6):
    print(i)