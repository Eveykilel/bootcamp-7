
def reverse_string(string):
  
  if string == '':
    return
  #used to store the string value
  store_list = list(string)
  
  store_list.reverse()
  
  result = ''.join(store_list)

  
  if result == string:
    return True
  
  return result
  