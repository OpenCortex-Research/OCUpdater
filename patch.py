#!/usr/bin/python2
import argparse, json
#with open("/media/p4/OpenCortex/updates/settings.json") as jsonfile:
#        settings = json.load(jsonfile)

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,)

parser.add_argument("Operation", choices=["patch"])
parser.add_argument("-q", "--quiet", default=False, action="store_true", help="Reduce output text")
parser.add_argument("-s", "--silent", default=False, action="store_true", help="Stop all text output. Use for headless patching")
parser.add_argument("File")

args = parser.parse_args()
operation = args.Operation
if args.File is None:
    parser.error("Update file required")

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