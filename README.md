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
is_done, is_timeout, erro_message, results = func_with_timeout(a=12, b=8)

```
You will find that after the method is called to the time you specified, it will return and kill the currently executing thread.

You can also use it as a decorator

```python
import time
from call_function_with_timeout import SetTimeoutDecorator

# make your function with timeout
@SetTimeoutDecorator(timeout=5)
def do_something(a=0, b=0):
    time.sleep(10)
    print(a + b)

# call the function
is_done, is_timeout, erro_message, results = do_something(a=12, b=8)

```