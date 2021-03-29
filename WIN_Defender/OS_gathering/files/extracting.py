import re
import json
import sys
import os

args = sys.argv
if (len(args) < 2):
    sys.exit(1)

path = args[1]
if(path[-1:] == "/"):
    path = path[:-1]

result_filedata_table = {}

target_filepath_list = []
target_filepath_list.append('/0/stdout.txt')
target_filepath_list.append('/1/stdout.txt')
target_filepath_list.append('/2/stdout.txt')
target_filepath_list.append('/3/stdout.txt')
target_filepath_list.append('/4/stdout.txt')
target_filepath_list.append('/5/stdout.txt')
target_filepath_list.append('/6/stdout.txt')
for target_filepath in target_filepath_list:
    filepath = path + '/command' + target_filepath
    if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
        with open(filepath) as file_object:
            reader = json.load(file_object)
            if isinstance(reader, list):
                rows = reader
            else:
                rows = []
                rows.append(reader)
            for row in rows:
                for param_key, param_value in row.items():
                    if param_key == 'DisableNotifications':
                        if target_filepath == '/3/stdout.txt':
                            result_filedata_table['FireWallPublicProfileNotice'] = param_value
                        elif target_filepath == '/4/stdout.txt':
                            result_filedata_table['FireWallStandardProfileNotice'] = param_value
                        elif target_filepath == '/5/stdout.txt':
                            result_filedata_table['FireWallDomainProfileNotice'] = param_value
                    else:
                        result_filedata_table[param_key] = param_value

result = {}
target_parameter_root_key = 'VAR_WIN_Defender'
result[target_parameter_root_key] = result_filedata_table
print(json.dumps(result))

