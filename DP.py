import dropbox

class DP:
    def __init__(self, access_token):
        self.access_token=access_token
    
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
    
def main():
    access_token = 'E-x9-dSNM-0AAAAAAAAAAa8YDt0gjJEAla-4LblpgHoEsEWi8PxVmI4G8vIcEfju'
    tranferData = DP(access_token)

    file_from = input("Enter file path... ")
    file_to = input("Enter destination path... ")

    tranferData.upload_file(file_from, file_to)

if __name__  == '__main__':
    main()