#방법1: endswith를 이용하여 .h,.c로 끝나는 리스트안에 있는 원소를 출력가능
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
    if i.endswith(('.h', '.c')):
        print(i)   
#방법2: split함수를 이용해 출력
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
    name, ext = i.split('.')       # .을 기준으로 name과 ext에 분리되어 메모리가 담긴다. ex) intra.c --> name=intra, ext=c
    if ext == 'h' or ext == 'c':   # 만약 ext에 h나 c가 담긴다면 i를 프린트해라
        print(i)                   # i는 리스트의 원소들을 바인딩하고 있으므로 print(i)를 하게 될 경우 확장자가 h나 c인 원소들의 풀네임이 출력된다.