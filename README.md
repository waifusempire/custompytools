<h1>custompytools</h1>
<h3>Python Version - 3.10</h3>
<h3>Author - <a href="https://github.com/waifusempire">waifusempire</a></h3>
<h3>Version - 1.0.0</h3>
<br>
<h1><a href="./lib">lib</a></h1>
<h2>● <a href="README.md#console">console</a></h2>
<h3>○ ● <a href="README.md#con1">write</a></h3>
<h3>○ ● <a href="README.md#con2">read</a></h3>
<h3>○ ● <a href="README.md#con3">clear</a></h3>
<h3>○ ● <a href="README.md#con4">execute_command</a></h3>
<h3>○ ● <a href="README.md#con56">console</a></h3>
<h3>○ ● <a href="README.md#con56">Mode</a></h3>
<h3>○ ● <a href="README.md#con7">Console</a></h3>
<h2>● <a href="README.md#json">better_json.py</a></h2>
<h3>○ ● <a href="README.md#js1">OpenJson</a></h3>
<h3>○ ● <a href="README.md#js2">JsonIO</a></h3>

<br>
<h1 id="console">console</h1>
<br>
<h2 id="con1">1. write(*_values, _sep: str = ..., _end: str = ...)</h2>
Write something to the console<br>
Example<br>

```py
>>> from custompytools.lib import write
>>> 
>>> write("Hello World!") # print
Hello World!
>>> 
```
<br>
<h2 id="con2">2. read(_output: str = ..., _type: int | float | str | bool = ...) -> int | float | str | bool</h2>
Read from the console<br>
Example<br>

```py
>>> from custompytools.lib import read
>>> 
>>> randomnum = read("Give a random integer - ", int) # input but with type conversion
Give a random integer - 5
>>> randomnum
5
>>> type(randomnum)
<class 'int'>
>>> 
```
<br>
<h2 id="con3">3. clear()</h2>
Clears the console<br>
Example<br>

```py
>>> from custompytools.lib import clear
>>> 
>>> 
>>> clear() # Before
```
```py
>>> #After



```
<br>
<h2 id="con4">4. execute_command(command: CMD | str, text: bool = ..., stdout: FILE = ..., stdin: FILE = ..., stderr: FILE = ...) -> Completed:</h2>
Run a subprocess<br>
Example<br>

```py
>>> from custompytools.lib import execute_command as execute
>>> 
>>> cmd = execute("pip install -U pip")
... # Updates pip 
>>> cmd.returncode
0
>>> 
```
<br>
<h2 id="con56">5. console(mode: Mode, /, *args, **kwargs) & 6. Mode</h2>
console is a fusion of the commands above<br>
Example<br>

```py
>>> from custompytools.lib import console, Mode
>>> 
>>> console(Mode.write, "Hello World!")
Hello World!
>>> 
```
<br>
<h2 id="con7">7. Console</h2>
Console.<a href="README.md#con1">write</a><br>
Console.<a href="README.md#con2">read</a><br>
Console.<a href="README.md#con3">clear</a><br>
Console.<a href="README.md#con4">execute</a><br>
<br>
<h1 id="json">better_json.py</h1>
<br>
<h2 id="js1">1. OpenJson(file_name: str, mode: str = "l") -> <a href="README.md#js2">JsonIO</a></h2>
OpenJson is a context manager which returns a JsonIO object<br>
Example<br>

```py
>>> from custompytools.lib import OpenJson
>>> 
>>> with OpenJson("test.json", "d") as f: # 'l' - load , 'd' - dump
...     f.dump({"Test": "Test"})
... 
None
>>> 
>>> with OpenJson("test.json", "l") as f: # 'l' - load , 'd' - dump
...     f.load()
... 
{'Test': 'Test'}
>>> 
```
<br>
<h2 id="js2">2. JsonIO</h2>
A wrapper around the TextIOWrapper class, is returned from <a href="README.md#js1">OpenJson</a>, this class shouldn't be subclassed<br><br>
<b> - Attributes - </b><br>
 - dump(data: DictLike | ListLike, **kwargs) -> None<br>
 - load(**kwargs) -> JsonObject | JsonArray<br>
 - is_marked_loaded -> bool<br>
 - is_marked_dumped -> bool<br>
 - closed -> bool<br>
 - name -> str<br>
 - file -> TextIOWrapper<br>
 - mode -> str


