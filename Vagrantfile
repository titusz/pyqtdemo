$macbuild = <<SCRIPT
curl -L https://www.python.org/ftp/python/3.5.4/python-3.5.4-macosx10.6.pkg -o python-3.5.4-macosx10.6.pkg -s
sudo installer -pkg python-3.5.4-macosx10.6.pkg -target /
python3 -m venv venv
source venv/bin/activate
pip install fbs==0.1.0
SCRIPT

Vagrant.configure("2") do |config|

  config.vm.provider "virtualbox" do |v|
    v.gui = true
    v.memory = 4096
  end

  config.vm.define "mac" do |mac|
 	  mac.vm.box = "jhcook/macos-sierra"
 	  mac.vm.provision "shell", inline: $macbuild
  end

  config.vm.define "win" do |win|
	  win.vm.box = "Microsoft/EdgeOnWindows10"
	  win.vm.box_version = "1.0"
	  win.ssh.username = "IEUser"
	  win.ssh.password = "Passw0rd!"
  end

end
