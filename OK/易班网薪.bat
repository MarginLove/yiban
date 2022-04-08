@echo off
if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit
:begin
call conda activate dl
python C:\Users\Administrator\Desktop\yiban0.2.py

%这是无窗口运行python%

