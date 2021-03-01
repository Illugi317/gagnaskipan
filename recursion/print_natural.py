def natrual_numbers(n):
    helper_function(n,0)

def helper_function(n,cnt):
    if cnt > n:
        return
    else:
        print(cnt,end=" ")
        helper_function(n, cnt + 1)
