from __future__ import annotations


import threading
from typing import Any, Callable
from time import sleep
from requests import get


class Promise:
    thread: threading.Thread
    resolver: Callable = None
    rejecter: Callable = None
    finish_callback = None
    
    def then(self, action: Callable[[Any], None]):
        self.resolver = action
        return Promise(self.next_promise_function)
    
    def catch(self, exception_handle: Callable[[Exception], None]):
        self.rejecter = exception_handle
        return Promise(self.next_promise_function)
    
    def __init__(self, func: Callable[[Callable, Callable], None]):
        def resolve(data):
            result, error = None, None
            
            if self.resolver:
                try:
                    result = self.resolver(data)
                except Exception as e:
                    error = e
                
            if self.finish_callback and (result or error):
                self.finish_callback(result, error)
            
        def reject(err):
            result, error = None, None
            if self.rejecter:
                try:
                    result = self.rejecter(err)
                except Exception as e:
                    error = e
            else:
                error = err
            
            if self.finish_callback and (result or error):
                self.finish_callback(result, error)
            
        def thread_function():
            try:
                func(resolve, reject)
            except Exception as e:
                reject(e)

        self.thread = threading.Thread(target=thread_function)
        self.thread.start()
    
    def next_promise_function(self, resolve, reject):
        def post_catch_hook(result, error):
                if error:
                    reject(error)
                resolve(result)
                    
        self.finish_callback = post_catch_hook


def send_url(url):
    def inner(resolve, reject):
        try:
            resolve(get(url))
        except Exception as err:
            reject(err)
    return inner


Promise(send_url("https://gigdsgsdthub.com")).then(lambda data: print(data)).then(lambda data: print(data))
Promise(send_url("https://sdgsdggithub.com")).catch(lambda err: print(f"Error: {err}"))
Promise(send_url("https://github.sdgscom")).then(lambda data: print(data)).catch(lambda err: print(f"Error: {err}"))
Promise(send_url("https:gdsg//github.com")).then(lambda data: print(data)).catch(lambda err: print(f"Error: {err}"))
Promise(send_url("https://github.com")).then(lambda data: print(data)).catch(lambda err: print(f"Error: {err}"))
Promise(send_url("https:/dsgsd/githudsgsdb.com")).then(lambda data: print(data)).catch(lambda err: print(f"Error: {err}"))
Promise(send_url("https://github.com")).then(lambda data: print(data)).catch(lambda err: print(f"Error: {err}"))
Promise(send_url("https://github.com")).then(lambda data: print(data)).catch(lambda err: print(f"Error: {err}"))
Promise(send_url("https://gsdgsdithub.com")).then(lambda data: print(data)).catch(lambda err: print(f"Error: {err}"))
Promise(send_url("https://gsdgdsdsgsdgithub.com")).then(lambda data: print(data)).catch(lambda err: print(f"Error: {err}"))
Promise(send_url("https://github.com")).then(lambda data: print(data)).catch(lambda err: print(f"Error: {err}"))
Promise(send_url("https://github.com")).then(lambda data: data).then(lambda data: data.json()).catch(lambda err: f"Error: {err}").then(lambda data: print(data))
sleep(1)