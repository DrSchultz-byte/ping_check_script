# ping_check_script
ping-网络可用性检查脚本

欢迎光临，这是我的代码

本代码是一个用于大规模检测网络IP通断的脚本

在python环境下，支持各类系统版本，使用之前请修改源码配置

使用前请修改： 请修改结果日志文件ping_circle{0}.txt的存放位置 默认在/usr/ping_result目录（需要保证有ping_result目录，否则会报错!!!）

如有需要，请修改ping_ip_list.txt的位置 默认在/usr目录

使用方法： 将需要测试的ip写入到ping_ip_list.txt文件 执行ping_check.py脚本即可
