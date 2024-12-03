from ftplib import FTP
import os

# FTP服务器信息
ftp_host = "192.168.0.241"
ftp_user = "cal"
ftp_password = "1234Qwer"

# 要上传的本地文件
local_file = ".\image_600x800.jpg"

# 连接到FTP服务器
ftp = FTP(ftp_host)
ftp.login(user=ftp_user, passwd=ftp_password)

# 切换到目标目录
ftp.cwd("cal")

# 上传文件
with open(local_file, "rb") as file:
    ftp.storbinary(f"STOR {os.path.basename(local_file)}", file)

# 关闭连接
ftp.quit()

print(f"文件 {local_file} 已成功上传到FTP服务器的cal目录。")