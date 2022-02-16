from __future__ import annotations


import threading
from typing import Any, Callable
from time import sleep
from requests import get


class Promise:
    thread: threading.Thread
    resolver: Callable = None
    rejecter: Callable = None
    finished: bool = False
    result = None
    error = None
    
    def __init__(self, func: Callable[[Callable, Callable], None]):
        def resolve(data):
            try:
                if self.resolver:
                    self.result = self.resolver(data)
            except Exception as e:
                self.error = e
                
            self.finished = True
            
        def reject(err):
            try:
                if self.rejecter:
                    self.result = self.rejecter(err)
                else:
                    raise err
            except Exception as e:
                self.error = e
                
            self.finished = True
            
        def inner():
            try:
                func(resolve, reject)
            except Exception as e:
                reject(e)

        self.thread = threading.Thread(target=inner)
        self.thread.start()

    def then(self, action: Callable[[Any], None]):
        self.resolver = action
        
        def inner(resolve, reject):
            while not self.finished:
                sleep(0.1)
            if self.error:
                reject(self.error)
            try:
                resolve(self.result)
            except Exception as e:
                reject(e)
        
        return Promise(inner)
    
    def catch(self, exception_handle: Callable[[Exception], None]):
        self.rejecter = exception_handle
        
        def inner(resolve, reject):
            while not self.finished:
                sleep(0.1)
            try:
                resolve(self.error)
            except Exception as e:
                reject(e)
        
        return Promise(inner)


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
Promise(send_url("https://github.com")).then(lambda data: print(data)).catch(lambda err: print(f"Error: {err}"))

sleep(1)