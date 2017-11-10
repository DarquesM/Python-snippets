#Snippet for parallel jobs
#Working

from joblib import Parallel, delayed
import multiprocessing

def foo(p)
    #do stuff
    return something

from joblib.pool import has_shareable_memory
num_cores = multiprocessing.cpu_count()

Parallel(n_jobs=num_cores,max_nbytes=1e6)(delayed(has_shareable_memory)(foo(p)) for p in parameters)
