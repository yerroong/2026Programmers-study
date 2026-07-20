def solution(brown, yellow):
    for h in range(3, brown+yellow+1):
        if (brown+yellow) % h ==0:
            w = (brown+yellow)//h
            if (h-2)*(w-2) == yellow:
              return [w,h]