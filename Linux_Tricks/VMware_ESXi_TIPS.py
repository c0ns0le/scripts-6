1, NIC teaming in ESXi and ESX
http://kb.vmware.com/selfservice/search.do?cmd=displayKC&docType=kc&docTypeID=DT_KB_1_1&externalId=1004088

2, NIC teaming
http://kb.vmware.com/selfservice/search.do?cmd=displayKC&docType=kc&docTypeID=DT_KB_1_1&externalId=2040972
http://kb.vmware.com/selfservice/microsites/search.do?cmd=displayKC&docType=kc&externalId=1004048&sliceId=1&docTypeID=DT_KB_1_1&dialogID=7904016&stateId=0%200%208557713

Host requirements for link aggregation for ESXi and ESX (1001938) 
http://kb.vmware.com/selfservice/microsites/search.do?cmd=displayKC&docType=kc&docTypeID=DT_KB_1_1&externalId=1001938
http://wiki.weithenn.org/cgi-bin/wiki.pl?VMware_Networking#Heading13

3, how to add VDS
http://www.ithome.com.tw/node/61046

4, Change ESXi management IP address.
esxcli network ip interface ipv4 set -i vmk1 -I 10.27.51.143 -N 255.255.255.0
-t static

5, This article provides steps to disable vNetwork Distributed Switches from
vCenter Server.
http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1010718

6,Enable and configure SNMP on VMware ESXi 5 - TuM'Fatig:
https://www.tumfatig.net/20120224/enable-and-configure-snmp-on-vmware-esxi-5/

7, vSphere Client and vSphere PowerCLI may fail to connect to vCenter Server 5.5 due to a Handshake failure (2049143) 
Add the <cipherList>ALL</cipherList> parameter between the <ssl>...</ssl> section of the configuration file
For Windows-based vCenter Server
C:\ProgramData\VMware\VMware VirtualCenter\vpxd.cfg

For the vCenter Server Appliance
/etc/vmware-vpx/vpxd.cfg

For ESXi 5.5
/etc/vmware/rhttpproxy/config.xml    
For Windows-based vCenter Server
C:\ProgramData\VMware\VMware VirtualCenter\vpxd.cfg


8, Migrate Standard Switch to VSwitch( two Management port).
1) 把vmk0,vmk1在交换机上配制为ACCESS PORT.
2) 把vmk0,vmk1在VSwitch上绑定到同一个管理处地址（即VMK0的地址）。
3) 把VMK0所在交换机上的接口配制为trunk port.
4) 迁移VMK0至VSwitch中相应的vlan，删除vmk1即可以。

9, Migrate Standard Switch to VSwitch( single Management port).
1) 把VMK0所在交换机上的接口配制为trunk port.
2) 把vmk0在esxi console中配制为相应的vlan ID.
3) 连接至ESXi并迁移管理网络至分布式交换机即可。
4) 把VMK0所在交换机上的接口配制为trunk port.


10, How to migrate backups from VDR to VDP
http://www.vladan.fr/how-to-migrate-backups-from-vdr-to-vdp/


11,VMware KB: Rebuilding the virtual machine's .vmx file from vmware.log:
http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1023880

12, Error: Unable to connect to the MKS: Virtual machine config file does not exist

13, Add more than 4T disk to ESXi5.5
# vmkfstools -c 7627533M -d thin /vmfs/volumes/RAID06-File/120-File/fileback120.vmdk
http://kb.vmware.com/selfservice/search.do?cmd=displayKC&docType=kc&docTypeID=DT_KB_1_1&externalId=1002511

14, Enable esxi5.5 fireware for VNC
https://gist.github.com/jasonberanek/4670943

15, enable VNC
http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1246


16, XP issue:
http://www.omniweb.com/wordpress/?p=1106



17, create VMs from commandline


ESXi auto create:

/vmfs/volumes/5358fbe3-d72d929e-7e65-f8bc124414ce # ./test.sh windows2008r2
Create: 100% done.
(vim.fault.NotFound) {
   dynamicType = <unset>, 
   faultCause = (vmodl.MethodFault) null, 
   msg = "Unable to find a VM corresponding to "(vim.fault.AlreadyExists)"", 
}

18, vCenter install Pot 80 is used ?
stop SQL Server Reporting Services (MSSQLSERVER) service
http://stackoverflow.com/questions/1430141/port-80-is-being-used-by-system-pid-4-what-is-that

19, To set das.ignoreRedundantNetWarning to true:

    From the VMware Infrastructure Client, right-click on the cluster and click Edit Settings.
    Select vSphere HA and click Advanced Options.
    In the Options column, enter das.ignoreRedundantNetWarning
    In the Value column, type true.

Note: Steps 3 and 4 create a new option.

Click OK.
Right-click the host and click Reconfigure for vSphere HA. This reconfigures HA.

20, vmware esxi mapping san/raw disk to vm direct
http://buildvirtual.net/working-with-raw-device-mappings/

21, Creating/Adding a Raw Device Mapping (RDM) to a Virtual Machine - VMadmin.co.uk
http://www.vmadmin.co.uk/resources/35-esxserver/58-rdmvm
http://forza-it.co.uk/esxi-5-1-using-raw-device-mappings-rdm-on-an-hp-microserver/

22, vCenter 5.5 linux web support
{{{
git clone https://github.com/i-rinat/freshplayerplugin.git
cd freshplayerplugin && mkdir build
cd build
cmake ..
make
cp libfreshwrapper-pepperflash.so ~/.mozilla/plugins/
}}}

https://communities.vmware.com/thread/459534?start=15&tstart=0
https://github.com/i-rinat/freshplayerplugin
http://www.webupd8.org/2014/05/fresh-player-plugin-pepper-flash.html
