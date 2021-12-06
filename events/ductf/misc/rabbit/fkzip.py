import subprocess
import glob

def bun(flag):
    result = subprocess.run(['bunzip2', flag])
    return result

def get_flag():
    flag = glob.glob('flag*')[0]
    return flag

def file_cmd(flag):
    result = subprocess.run(['file', flag], stdout=subprocess.PIPE)
    return result

def mv_cmd(src, dst):
    result = subprocess.run(['mv', src, dst], stdout=subprocess.PIPE)

def rnm_ext(flag, ext):
    new_name = flag.split(".")[0]
    mv_cmd(flag, new_name+ext)

out = "bzip2"

while "text" not in out:
    flag_name = get_flag()
    ftype = file_cmd(flag_name)
    out = ftype.stdout.decode().split(": ")[1]
    if "bzip2" in out:
        rnm_ext(flag_name, ".bz2")
        flag_name = get_flag()
        result = subprocess.run(['bunzip2', flag_name], stdout=subprocess.PIPE)
    elif "XZ" in out:
        rnm_ext(flag_name, ".xz")
        flag_name = get_flag()
        result = subprocess.run(['unxz', flag_name], stdout=subprocess.PIPE)
    elif "gzip" in out:
        rnm_ext(flag_name, ".gz")
        flag_name = get_flag()
        result = subprocess.run(['gunzip', flag_name], stdout=subprocess.PIPE)
    elif "Zip" in out:
        rnm_ext(flag_name, ".zip")
        flag_name = get_flag()
        result = subprocess.run(['unzip', flag_name], stdout=subprocess.PIPE)
        result = subprocess.run(['rm', flag_name], stdout=subprocess.PIPE)

flag_name = get_flag()
result = subprocess.run(['base64', '-d', flag_name])
print()
