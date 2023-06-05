#!/usr/bin/python2
import argparse, json, subprocess, sys
#with open("/media/p4/OpenCortex/updates/settings.json") as jsonfile:
#        settings = json.load(jsonfile)

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,)

parser.add_argument("Operation", choices=["patch"])
parser.add_argument("-q", "--quiet", default=False, action="store_true", help="Reduce output text")
parser.add_argument("-s", "--silent", default=False, action="store_true", help="Stop all text output. Use for headless patching")
parser.add_argument("File")

# For Dev Testing
class subprocess:
    def __init():
        pass

    def call(args):
        print(args)

args = parser.parse_args()
operation = args.Operation
if args.File is None:
    parser.error("Update file required")
file = args.File

BLUE='\033[0;34m'  
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# echo the ascii art banner
print(f"""{YELLOW}
    ____                   ______           __             
   / __ \____  ___  ____  / ____/___  _____/ /____  _  __  
  / / / / __ \/ _ \/ __ \/ /   / __ \/ ___/ __/ _ \| |/_/  
 / /_/ / /_/ /  __/ / / / /___/ /_/ / /  / /_/  __/>  <    
 \____/ .___/\___/_/ /_/\____/\____/_/   \__/\___/_/|_|    
     /_/                       CorOS update patcher        
{NC}""")

print(f"{BLUE}=============== OpenCortex Update Patcher ==============={NC}")
subprocess.call(["mkdir", "-r", "/media/p4/OpenCortex/updates/cache/fs/"])
subprocess.call(["mkdir", "-r", "/media/p4/OpenCortex/updates/cache/uncompressed-fs/"])
print(f"{YELLOW}[!]{NC} Extracting update file...")
subprocess.call(["gunzip", f"{file}"])
subprocess.call(["tar","-xvf", f"{file[:-3]}", "-C", "/media/p4/OpenCortex/updates/cache/uncompressed-fs/"])
print(f"{YELLOW}[!]{NC} Mounting update file...")
subprocess.call(["mount", "-t", "ext4", "/media/p4/OpenCortex/updates/cache/uncompressed-fs/rootfs.ext3", "/media/p4/OpenCortex/updates/cache/fs/"])

# Do patching here

print(f"{YELLOW}[!]{NC} Compressing update file...")
subprocess.call(["tar", "-cvf", f"{file[:-3]}", "/media/p4/OpenCortex/updates/cache/uncompressed-fs/rootfs.ext3", "/media/p4/OpenCortex/updates/cache/uncompressed-fs/uImage", "/media/p4/OpenCortex/updates/cache/uncompressed-fs/zpu.dtb"])
subprocess.call(["gunzip", "-k", f"{file[:-3]}"])
print(f"{BLUE}[+]{NC} Update file patched: {file}")

print(f"{YELLOW}[!]{NC} Unmounting update...")
subprocess.call(["umount", "/media/p4/OpenCortex/updates/cache/fs/"])

print(f"{YELLOW}[!]{NC} Clearing cache...")
subprocess.call(["rm", "-r", "/media/p4/OpenCortex/updates/cache/"])
