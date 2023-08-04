import subprocess

class StandardOutput:
    @staticmethod
    def stdout(system_command:str):
        stdout = subprocess.check_output(system_command, shell=True, text=True, stderr=subprocess.STDOUT)
        return stdout

class WhoAmI(StandardOutput):
    def whoami(self):
        full_string = super().stdout("powershell.exe whoami").rstrip('\n').split('\\')
        hostname, username = full_string[0], full_string[1]
        return hostname, username

class Initiated:
    def __init__(self) -> None:
        self.__initiated__ = False

    @property
    def initiated(self):
        return self.__initiated__    
    @initiated.setter
    def initiated(self, new:bool):
        self.__initiated__ = new

class Finished:
    def __init__(self) -> None:
        self.__finished__ = False

    @property
    def finished(self):
        return self.__finished__    
    @finished.setter
    def finished(self, new:bool):
        self.__finished__ = new

from webbrowser.Chrome import Chrome
from os import listdir
class DownloadProcess(Chrome, WhoAmI, Initiated, Finished):
    def __init__(self, download_url:str):
        WhoAmI.__init__(self)
        Initiated.__init__(self)
        Finished.__init__(self)
        self.download_process(download_url)

    def download_process(self, download_url):
        browser = Chrome()
        browser.browse(download_url)
        while not self.initiated:
            self.initiated = self.update_download_state()
        while not self.finished:
            self.finished = not self.update_download_state()
        browser.terminate()
    
    def update_download_state(self):
        return bool(len( [item for item in listdir(f"C:\\Users\\{self.whoami()[1]}\\Downloads") if item.endswith('.crdownload')] ))
        
if __name__=="__main__":
    raise NotImplementedError()