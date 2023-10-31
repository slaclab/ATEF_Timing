import subprocess
import config


print("Hutch code list: \n\nCXI_FS5: 5  \nMEC_FS6: 6  \nMFX_FS4.5: 45  \nNEH_FS11: 11 \nNEH_FS14: 14  \nXCS_FS4: 4\n")
hutch_code = input("Enter hutch code: ")
hutch_dict = {"5" : "CXI_FS5", "6" : "MEC_FS6",  "45" : "MFX_FS4.5",  "11" : "NEH_FS11", "14" : "NEH_FS14",  "4" : "XCS_FS4"}
hutch = hutch_dict[hutch_code]
folder= "/cds/home/r/rj1/atef/timing_config/"+ hutch + "/"
ioc_path = folder + hutch + '_IOC.txt'
pv_lists_path = folder + "pv_lists/"

subprocess.run(["mkdir", "-p", pv_lists_path])

with open(ioc_path, 'r') as readtxt:
    ioc_list = [line.strip() for line in readtxt.readlines()]
    # Read the file line by line
    for ioc in ioc_list:
        #print("Getting .pvlist file from " + ioc)
        subprocess.run(["cp", "/cds/data/iocData/"+ ioc +"/iocInfo/IOC.pvlist", pv_lists_path + ioc +"_IOC.pvlist"])
        print("Begin configuring " + ioc + "| IOC: " + str(ioc_list.index(ioc)+1) + "/" + str(len(ioc_list)))
        config.run_config_json(hutch, ioc, ioc_list.index(ioc), (ioc_list.index(ioc)+1)/len(ioc_list), folder, pv_lists_path + ioc +"_IOC.pvlist", pv_lists_path + "new_" + ioc +"_IOC.pvlist")
        print("Done")