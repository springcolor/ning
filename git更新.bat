echo .....Jump to folder E:\komi\komiTest（跳转至该路径，是一个git项目，应该会有一个.git文件夹。如果这个bat文件已经在git项目路径下了，可以不用跳转，直接写git命令，会对该git项目直接进行操作）
cd /d E:\komi\komiTest

echo .....!!!!git checkout master （执行git命令：切换至master分支）
git checkout master

echo .....enter any key to exit（想要bat文件执行完可以看到日志，而不是自动关闭，用以下方式可以实现：pause>nul）
pause>nul
