import re 
def count_substring(string, sub_string):
    res = len(re.findall('(?= sub_string)', string)) 
    return res

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
