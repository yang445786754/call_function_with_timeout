# call_function_with_timeout
A library to make your funtions support timeouts

Example

```python
import time
from call_function_with_timeout import SetTimeout

# make your function
def do_something(a=0, b=0):
    time.sleep(10)
    print(a + b)

# define function with timeout
func_with_timeout = SetTimeout(do_something, timeout=5)
# call the function
res = func_with_timeout(a=12, b=8)

print(res)

```
