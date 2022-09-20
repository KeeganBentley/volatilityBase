import argparse
import subprocess
import os

def get_config():
    """
    Parses user input from command line
    Returns: dict containing path, searchRegexs and label values
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-v','--volPath', nargs='?')
    parser.add_argument("-m", "--memoryPath", nargs='?')
    parser.add_argument("-o", "--outputPath", nargs='?')
    args = parser.parse_args()
    return args

config = get_config()
os.system(f"python3 {config.volPath} -f{config.memoryPath} windows.info.Info > {config.outputPath}/info.txt")
os.system(f"python3 {config.volPath} -f{config.memoryPath} windows.pslist.PsList > {config.outputPath}/pslist.txt")
os.system(f"python3 {config.volPath} -f{config.memoryPath} windows.psscan.PsScan > {config.outputPath}/psscan.txt")
os.system(f"python3 {config.volPath} -f{config.memoryPath} windows.cmdline.CmdLine > {config.outputPath}/cmdline.txt")
os.system(f"python3 {config.volPath} -f{config.memoryPath} windows.getservicesids.GetServiceSIDs > {config.outputPath}/getSID.txt")
os.system(f"python3 {config.volPath} -f{config.memoryPath} windows.dlllist.DllList > {config.outputPath}/dlllist.txt")
os.system(f"python3 {config.volPath} -f{config.memoryPath} windows.registry.userassist.UserAssist > {config.outputPath}/reg_usrAss.txt")
os.system(f"python3 {config.volPath} -f{config.memoryPath} windows.svcscan.SvcScan > {config.outputPath}/svcscan.txt")
os.system(f"python3 {config.volPath} -f{config.memoryPath} windows.netscan.NetScan > {config.outputPath}/netscan.txt")
os.system(f"python3 {config.volPath} -f{config.memoryPath} windows.registry.hivelist > {config.outputPath}/reghivelist.txt")
os.system(f"python3 {config.volPath} -f{config.memoryPath} windows.registry.printkey.PrintKey > {config.outputPath}/regkeylist.txt")
os.system(f"python3 {config.volPath} -f{config.memoryPath} windows.filescan.FileScan > {config.outputPath}/filescan.txt")
os.system(f"python3 {config.volPath} -f{config.memoryPath} windows.registry.certificates.Certificates > {config.outputPath}/certs.txt")
os.system(f"python3 {config.volPath} -f{config.memoryPath} windows.malfind.Malfind > {config.outputPath}/malfind.txt")
os.system(f"mkdir {config.outputPath}/registryDump")
os.system(f"python3 {config.volPath} -f{config.memoryPath} -o {config.outputPath}/registryDump windows.registry.hivelist --dump")