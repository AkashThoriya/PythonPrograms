def count_substring(string, sub_string):
    count = sum(int(string.startswith(sub_string, i)) for i in range(len(string)))
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
