 
 
 sudo apt-get update
 sudo apt-get upgrade
 sudo apt-get install python3
 sudo python -m pip install numpy
 sudo python -m pip install imutils
 sudo python -m pip install requests
 sudo python -m pip install pynmea2
 sudo python -m pip install geopy
 
 sudo python -m pip install opencv-contrib-python
 sudo apt-get install libhdf5-100
 sudo apt-get install libcblas3
 sudo apt-get install  libatlas3-base
 sudo apt-get install libjasper1
 sudo apt-get install libqtgui4
 
 apt-get install python-dev
 apt-get install libjpeg-dev
 apt-get install libjpeg8-dev
 apt-get install libpng3
 apt-get install libfreetype6-dev

 sudo apt-get install ssmtp mailutils mpack
 sudo rm /etc/ssmtp/ssmtp.conf
 sudo cp ssmtp.conf /etc/ssmtp/ssmtp.conf
 
 sudo rm /etc/aliases
 sudo cp aliases /etc/aliases
 sudo newaliases
 sudo chfn -f "device1 @ antr" pi
 sudo apt-get install mailtools

 
 
 
 sudo echo "sudo python /home/pi/wtr/gpsaccess.py &" >>/etc/rc.local
 sudo echo "sudo python3 /home/pi/wtr/cameracode2.py &" >>/etc/rc.local
 sudo echo "sudo python3 /home/pi/wtr/SDnld.py &" >>/etc/rc.local
  