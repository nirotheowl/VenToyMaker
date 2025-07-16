██╗   ██╗███████╗███╗   ██╗████████╗ ██████╗ ██╗   ██╗
██║   ██║██╔════╝████╗  ██║╚══██╔══╝██╔═══██╗╚██╗ ██╔╝
██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║ ╚████╔╝ 
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║  ╚██╔╝  
 ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝   ██║   
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝    ╚═╝   
    ███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗
    ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
    ██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝
    ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
    ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║
    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                For Debian/CentOS

AUTO ISO IMAGE DOWNLOAD not finished
(!you won't be prompted for it yet either!)
Must have a clean media device connected beforehand. There is no error check for it yet.
It will try to detect the device, but always double-check before writing to anything.

TO RUN:

1. Download the ZIP file and extract it:
   - Right-click → "Extract Here"
   - OR use the terminal:
       unzip VentoyMaker.zip

2. Open a terminal in the extracted folder.

3. Run the setup script with root permissions:
       sudo ./start.sh

   This will:
     - Check if Python3 is installed
     - Create the necessary folders under ~/VentoyMaker
     - Copy the main Python script into place

4. Place your ISO files into this folder:
       ~/VentoyMaker/ISO images

5. To start the program:
       python3 ~/VentoyMaker/scripts/ventoymaker.py

   (You can also use the included launcher script if available:
       ./ventoymaker-launcher.sh
   )

Once running, the wizard will guide you through selecting ISOs and flashing them to a USB drive.
