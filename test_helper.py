#%%
import json
from pathlib import Path

#%%
def read_json(test_file):
    with open(test_file) as f:
        return json.load(f)

def write_json(obj, test_file, mode="w"):
    with open(test_file, mode) as f:
        json.dump(obj, f, indent=4)

#%%
def sample_test(function, test_name, test_file):
    '''only supported key-word arguments'''

    paramiter = read_json(test_file)[test_name]
    
    return function(**paramiter)

#%%
def save_paramiter(test_file, test_name, **kwargs):
    '''only supported key-word arguments'''
    test_file = Path(test_file)
    
    prev = {}
    if test_file.exists():
        test_file.touch()
    else:
        with open(test_file, "r") as f:
            text = f.read()
            if text: prev = json.load(f)
    
    prev[test_name] = kwargs
    write_json(prev, test_file, "w")

# %%
if __name__=="__main__":
    save_paramiter(
        "testcase\\5.json", "c", 
        n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
    )
# %%
