import yaml
import os
from datetime import datetime

datenow = datetime.now().strftime("%Y-%m-%d")

devlist = ["portamon","oxymon","octamon","octamon-m","brite","portalite"]

applist = ["BCI", "BF-M", "BF-P", "BF-PF", "BF-T", "BF-V", "CR", "HS", "HA", \
           "NN", "NS-FNIRS", "NIRS-EEG", "SS", "U", "VR"]

apptag_dict = {"BCI" : "brain-computer-interfaces", "BF-M" : "brain-fnirs-motor-cortex", \
               "BF-P" : "brain-fnirs-parietal-cortex", "BF-PF" : "brain-fnirs-prefrontal-cortex", \
               "BF-T" : "brain-fnirs-temporal-cortex", "BF-V" : "brain-fnirs-visual-cortex", \
               "CR" : "clinical-and-rehabilitation", "HS" : "hyperscanning", "HA" : "hypoxia-and-altitude-studies", \
               "NN" : "neonatal", "NS-FNIRS" : "neurostimulation-fnirs", "NIRS-EEG" : "nirs-eeg", \
               "SS" : "sports-science", "U" : "urology", "VR" : "virtual-reality"}

# Hardcoded path to output from academic tool, please change me!
infolder = "C:/temp/2/content/"   

# Get rid of "---" at start and end to not confuse yaml.load
for root, dirs, files in os.walk(infolder, topdown=False):
   #Loop over *.md files
    for name in files:
       if name.endswith(".md"):
            with open (os.path.join(root, name),'r+') as f:
                data = ''.join([line for line in f if not line.startswith("---")])
                f.seek(0)
                f.write(data)     
                f.truncate()
       #Get rid of file entryin cite.bib, doesn't look good
       elif name.endswith(".bib"):
            with open (os.path.join(root, name),'r+') as f:
                data = ''.join([line for line in f if not line.startswith(" file = ")])
                f.seek(0)
                f.write(data)     
                f.truncate()
                
# Get all files
for root, dirs, files in os.walk(infolder, topdown=False):
   #Loop over *.md files
    for name in files:
       if name.endswith(".md"):
           #Read in file with yaml.load
           with open (os.path.join(root, name)) as f:
               print("Opening: " + os.path.join(root, name))
               dat = yaml.load(f,Loader=yaml.FullLoader)
               dat["categories"] = [] # this is for the device categories
               dat["projects"] = []   # this is for the application categories
               
               # Only handle files that have "tags"
               
               if "tags" in dat: 
                   # Put devices into categories and applications into projects
                   dat["categories"] = [item for item in dat["tags"] if item.lower() in devlist]
                   dat["projects"] = [item for item in dat["tags"] if item in applist]
                   # Translate shortcodes into full slugs
                   dat["projects"] = [apptag_dict[item] for item in dat["projects"]]
                                                 
                   # Remove devices and applications from tags
                   dat["tags"] = [item for item in dat["tags"] if item.lower() not in devlist]
                   dat["tags"] = [item for item in dat["tags"] if item not in applist]
                   
                   
                   dat["date"] = datenow
                   print(dat)
                   #write output 
                   with open(os.path.join(root, name), 'w') as outfile:
                       yaml.dump(dat, outfile, allow_unicode = True)


# Add "---" on first and last line to let hugo know it's yaml and not md
for root, dirs, files in os.walk(infolder, topdown=False):
   #Loop over *.md files
    for name in files:
       if name.endswith(".md"):
           with open (os.path.join(root, name),'r+') as f:
               content = f.read()
               f.seek(0, 0)
               f.write("---\r\n" + content + "\r\n---\r\n")

