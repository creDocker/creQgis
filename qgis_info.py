from qgis.utils import iface
import os

print("Hello from QGIS")
## https://towardsdatascience.com/how-to-use-qgis-spatial-algorithms-with-python-scripts-4bf980e39898
'''
import sys
import pandas as pd
paths = sys.path
df = pd.DataFrame({'paths':paths})
df.to_csv('./qgis_sys_paths.csv', index=False)
'''

'''
import os
import json
env = dict(os.environ)
rem = ['SECURITYSESSIONID', 'LaunchInstanceID', 'TMPDIR']
_ = [env.pop(r, None) for r in rem]with open('./qgis_env.json', 'w') as f:
    json.dump(env, f, ensure_ascii=False, indent=4)
'''

from platform import python_version
print(python_version())


##iface.actionExit().trigger()

os._exit(0)
#qgis --nologo --code ./qgis_info.py
