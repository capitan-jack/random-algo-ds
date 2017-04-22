

def print_string_with_spaces(str, n):
    if n==len(str):
        print(*str)
    else:
        print_string_with_spaces(str[0:n] + [' '] + str[n:len(str)], n+2)
        print_string_with_spaces(str[0:n] + str[n:len(str)], n+1)


print_string_with_spaces(['a','b','c','d'],1)
