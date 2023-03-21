from SendEmal import Send_Email
from Test_InternetSpeed import TestInternetSpeed

fromaddress = "youngstarsairam@gmail.com"
toaddress = "sairambadiga@gmail.com"
# toaddress = "helpdesk@actcorp.in"

if __name__== '__main__':
    ist = TestInternetSpeed()
    se = Send_Email()
    UploadSpeed, DownloadSpeed, TransactionId = ist.tis()
    UploadSpeed = float(UploadSpeed)
    DownloadSpeed = float(DownloadSpeed)
    message = f"Hi,\n" \
              f"the speed of my internet is not as expected please find the details below\n" \
              f"upload speed = {UploadSpeed},\n" \
              f"Download Speed = {DownloadSpeed},\n" \
              f"Transaction Id = {TransactionId} \nmy registered email id is sairambadiga@gmail.com\n feel free to call me at any time regarding this to the number located belwo" \
              f"The promised internet speed is 50Mbps.\n\n\n Thanks!\nSairam Badiga\n9030284404"
    if (UploadSpeed < 350 and DownloadSpeed < 350):
        se.SendMail(fromusername=fromaddress, tousername=toaddress, message=message)
    else:
        print("Everthing is good!")