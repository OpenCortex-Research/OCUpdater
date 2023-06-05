#!/bin/bash

# This script can be used to apply OpenCortex patches to a QC update file

BLUE='\033[0;34m'  
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# echo the ascii art banner
echo -e "${YELLOW}"
echo -e "    ____                   ______           __             "
echo -e "   / __ \____  ___  ____  / ____/___  _____/ /____  _  __  "
echo -e "  / / / / __ \/ _ \/ __ \/ /   / __ \/ ___/ __/ _ \| |/_/  "
echo -e " / /_/ / /_/ /  __/ / / / /___/ /_/ / /  / /_/  __/>  <    "
echo -e " \____/ .___/\___/_/ /_/\____/\____/_/   \__/\___/_/|_|    "
echo -e "     /_/                       CorOS update patcher        "
echo -e "${NC}"

echo "This tool will patch the given CorOS update file"

echo -e "${BLUE}================ OpenCortex Update Patcher ================${NC}"