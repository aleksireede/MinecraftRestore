import sys
import os
import shutil

username = ''
debug = False
media_dir = ''
OS_String = 'Your Operating system is:'
drive_list = ['A:', 'B:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', 'L:', 'M:', 'N:', 'O:', 'P:', 'Q:', 'R:',
              'S:', 'T:', 'U:', 'V:', 'W:', 'X:', 'Y:', 'Z:']


def os_check():
    if sys.platform == "linux" or sys.platform == "linux2":
        print('')
        print('--------------------------------------------------------------------------------')
        print(OS_String, 'Linux')
        print('--------------------------------------------------------------------------------')
        print('')
        linux()
        print('')
        print('--------------------------------------------------------------------------------')
        print('')
    elif sys.platform == "win32":
        print('')
        print(
            "--------------------------------------------------------------------------------------------------------"
            "---------------")
        print(OS_String, 'Windows')
        print(
            "--------------------------------------------------------------------------------------------------------"
            "---------------")
        print('')
        windows()
        print('')
        print(
            "--------------------------------------------------------------------------------------------------------"
            "---------------")
        print('')
    else:
        print('Operating system not supported:', sys.platform)
        input('Press Enter to Continue')
        sys.exit(1)
    print('Restoration Complete')
    input('Press Enter to continue:')


def linux():
    global username, media_dir, debug
    os.chdir('/media')
    for users in os.listdir('/home'):
        if debug:
            print(users)
        username = users
        media_dir = os.path.join('/media', users)
        for drives in os.listdir(media_dir):
            if debug:
                print('Found Drive', drives)
            mc_path = os.path.join(media_dir, drives, 'FS_Backup', 'Minecraft', 'Java', 'worlds')
            if os.path.exists(mc_path):
                if debug:
                    print('Backup Found')
                destination_folder = os.path.join('/home', username, '.minecraft', 'Mainsurvival', 'saves')
                Unzip(mc_path, destination_folder)
                break
            else:
                print('No backups found')


def Unzip(Backup, Destination):
    for save in os.listdir(Backup):
        if '.md5' in save:
            continue
        shutil.copy(Backup + '/' + save, Destination)
        os.rename(Destination + '/' + save, Destination + '/' + save + '.zip')
        destination_directory = Destination + '/' + save[0:len(save) - 6]
        if os.path.exists(destination_directory):
            shutil.rmtree(destination_directory)
            print('Removing old copies...')
        os.mkdir(destination_directory)
        shutil.unpack_archive(Destination + '/' + save + '.zip', destination_directory)
        os.remove(Destination + '/' + save + '.zip')


def windows():
    global drive_list, debug
    os.chdir(os.path.join('C://', '/Users'))
    for file in os.listdir(os.getcwd()):
        if file != 'All Users' and file != 'Default' and file != 'Default User' and file != 'Desktop.ini' \
                and file != 'desktop.ini' and file != 'Public':
            print('Found User:', file)
            for drive in drive_list:
                if os.path.exists(os.path.join(drive + r'\FS_Backup')):
                    backup_folder = os.path.join(drive, r"\FS_Backup\Minecraft\Java\worlds\\")
                    os.chdir(os.path.join('C://', '/Users', file, 'Appdata', 'Roaming', '.Minecraft', 'Mainsurvival',
                                          "Saves"))
                    Unzip(backup_folder, os.getcwd())
                    break


if __name__ == '__main__':
    os_check()
