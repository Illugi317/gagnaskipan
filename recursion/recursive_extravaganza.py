def length_of_string(string:str):
    if string == '': return 0
    return 1 + length_of_string(string[1:])

def linear_search(my_list, search_value, counter=0):
    try:
        if my_list[counter] == search_value:
            return True
        else:
            return linear_search(my_list, search_value, counter+1)
    except IndexError:
        return False


def count_instance(my_list, search_value,cnt=0):
    if my_list == []:
        return cnt
    if my_list[0] == search_value:
        return count_instance(my_list[1:],search_value,cnt+1)
    else:
        return count_instance(my_list[1:],search_value,cnt)

def are_dupes(my_list:list):
    return are_dupes_helper(my_list)

def are_dupes_helper(my_list:list,index=0):
    if my_list == []:
        return False
    if count_instance(my_list, my_list[0]) > 1:
        return True
    else:
        return are_dupes_helper(my_list[1:])

def remdup(l, dup=None):
	if len(l) < 2:
		return l
	if dup is not None:
		try:
			l.remove(dup)
			remdup(l, dup)
		except ValueError:
			pass
	return [l[0]] + remdup(l[1:], l[0])

def binary_search(my_list:list,search_value:int,high:int,low:int):
    if high >= low:
        middle = ( high + low) // 2
        
        if my_list[middle] == search_value:
            return middle
        elif my_list[middle] > search_value:
            return binary_search(my_list,search_value,low,middle -1)
        else:
            return binary_search(my_list,search_value,high,middle +1)
    else:
        return False


def is_substring(substring, a_str, index=0):
    if len(substring) == index:
        return True
    if len(a_str) == 0:
        return False
    
    if substring[index] == a_str[0]:
        return is_substring(substring, a_str[1:],index+1)
    else:
        return is_substring(substring, a_str[1:])

def x_ish(a_str, x):
    if len(x) == 0:
        return True

    if linear_search(a_str,x[0]):
        return x_ish(a_str,x[1:])
    return False

def palindrome(a_str):
    if len(a_str) <= 1:
        return True
    if a_str[0] == a_str[-1]:
        return palindrome(a_str[1:-1])
    return False