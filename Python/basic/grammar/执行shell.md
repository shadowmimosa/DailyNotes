<font size=4 face='楷体'>

## 执行 shell

执行 shell 可选的有 `os.system` 和 `subprocess`模块

建议直接 subprocess, 更稳定更安全, 接口可读性高

```python
def run(*popenargs,
        input=None, capture_output=False, timeout=None, check=False, **kwargs):
    """Run command with arguments and return a CompletedProcess instance.

    The returned instance will have attributes args, returncode, stdout and
    stderr. By default, stdout and stderr are not captured, and those attributes
    will be None. Pass stdout=PIPE and/or stderr=PIPE in order to capture them.

    If check is True and the exit code was non-zero, it raises a
    CalledProcessError. The CalledProcessError object will have the return code
    in the returncode attribute, and output & stderr attributes if those streams
    were captured.

    If timeout is given, and the process takes too long, a TimeoutExpired
    exception will be raised.

    There is an optional argument "input", allowing you to
    pass bytes or a string to the subprocess's stdin.  If you use this argument
    you may not also use the Popen constructor's "stdin" argument, as
    it will be used internally.

    By default, all communication is in bytes, and therefore any "input" should
    be bytes, and the stdout and stderr will be bytes. If in text mode, any
    "input" should be a string, and stdout and stderr will be strings decoded
    according to locale encoding, or by "encoding" if set. Text mode is
    triggered by setting any of text, encoding, errors or universal_newlines.

    The other arguments are the same as for the Popen constructor.
    """
    if input is not None:
        if kwargs.get('stdin') is not None:
            raise ValueError('stdin and input arguments may not both be used.')
        kwargs['stdin'] = PIPE

    if capture_output:
        if kwargs.get('stdout') is not None or kwargs.get('stderr') is not None:
            raise ValueError('stdout and stderr arguments may not be used '
                             'with capture_output.')
        kwargs['stdout'] = PIPE
        kwargs['stderr'] = PIPE

    with Popen(*popenargs, **kwargs) as process:
        try:
            stdout, stderr = process.communicate(input, timeout=timeout)
        except TimeoutExpired as exc:
            process.kill()
            if _mswindows:
                # Windows accumulates the output in a single blocking
                # read() call run on child threads, with the timeout
                # being done in a join() on those threads.  communicate()
                # _after_ kill() is required to collect that and add it
                # to the exception.
                exc.stdout, exc.stderr = process.communicate()
            else:
                # POSIX _communicate already populated the output so
                # far into the TimeoutExpired exception.
                process.wait()
            raise
        except:  # Including KeyboardInterrupt, communicate handled that.
            process.kill()
            # We don't call process.wait() as .__exit__ does that for us.
            raise
        retcode = process.poll()
        if check and retcode:
            raise CalledProcessError(retcode, process.args,
                                     output=stdout, stderr=stderr)
    return CompletedProcess(process.args, retcode, stdout, stderr)
```

### Reference

**2021.08.04**
