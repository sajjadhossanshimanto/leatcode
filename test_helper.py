#%%
import json
from pathlib import Path


#%%
def sample_test(function, test_name, test_file):
    '''only supported key-word arguments'''

    with open(test_file) as f:
        paramiter = json.load(f)[test_name]
    
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
    with open(test_file, "w") as f:
        json.dump(prev, f)

# %%
if __name__=="__main__":
    save_paramiter(
        "testcase\\5.json", "c", 
        n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
    )
# %%
