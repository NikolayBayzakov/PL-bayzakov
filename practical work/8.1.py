def cnt_digits(a, b, c, N):
    cnt = 0 
    digits = [a, b, c]
    
    for i in digits:
        for j in digits:
            for k in digits:
                number = i * 100 + j * 10 + k
                if 100 <= number <= N:
                    cnt += 1 
    return cnt 

