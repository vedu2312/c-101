
import dropbox
class Transferdata :
    def __init__(self,acesstoken):
        self.acesstoken=acesstoken
        
    def uploadFile(self,fromfile,tofile):
        db=dropbox.Dropbox(self.acesstoken)
        f=open(fromfile,'rb')
        db.files_upload(f.read(),tofile)
        
def main():
    acesstoken='sl.A_XePGbwG9TK_Bac9IfXtzIM_Mjb5S5hVha-pcbUthiKAEKTq6psm2Ov6tzHCIdzzYlAl6G45Gn1AV5hrtat5HmwtqlFSf5SMbixfoS4MRGM7A8Q7WZ28AEDrKpR-wi1zAUrSnQ'
    t=Transferdata(acesstoken)
    fromfile='notepad.txt'
    tofile='https://www.dropbox.com/home/myfile/notepad1.txt'
    t.uploadfile(fromfile,tofile)
    print("done")
    
    
main()                     