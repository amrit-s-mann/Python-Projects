def get_args_and_kwargs(*args, **kwargs):
    if len(args) + len(kwargs) >= 4 and "num" in kwargs and type(kwargs["num"]) in [int, float] and kwargs["num"] > 5:
        return True
    else:
        return False
    
x = get_args_and_kwargs("a", [2], num= 55.3, x=True)
print(x)