import json

def generate_diff(file1, file2):
    file1 = changing_values(file1)
    file2 = changing_values(file2)
    result = {}
    print("{")
    for key in file1:
       if (key in file2) and file1[key] == file2[key]:
          result['  ' + key] = file1[key]
          del file2[key]
       elif (key in file2) and file1[key] != file2[key]:
          result['- ' + key] = file1[key]
          result['+ ' + key] = file2[key]
          del file2[key]
       else:
          result['- ' + key] = file1[key]
    file2_upd = {f'+ {key}': v for key, v in file2.items()}
    result.update(file2_upd)
    result = dict(sorted(result.items(), key=lambda x: x[0][2]))
    for key in result:
       t = result[key]
       print(f'{key}: {t}')
    print("}")


def changing_values(dict_n):
  for key, value in dict_n.items():
    if value == True:
      dict_n[key] = 'true'
    if value == False:
      dict_n[key] = 'false'
  return dict_n