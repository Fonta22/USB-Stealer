import subprocess, os, time

drive_detected = False

print('Scanning for USB drives...')

def compressDrive(letter):
    tar_name = f'{letter}_Drive.tar.gz'

    cwd = os.getcwd()
    cdrive_letter = cwd.split(':')[0]

    start = time.time()
    os.system(f'{letter}: & tar -cvzf {cwd}\\{tar_name} * & {cdrive_letter}:')
    end = time.time()
    
    print(f'\nCompressed {letter}: into {cwd}\\{tar_name} in {round(end - start, 2)} seconds.')

while not drive_detected:
    out = subprocess.check_output('wmic logicaldisk get DriveType, caption', shell=True)
    drives = str(out).strip().split('\\r\\r\\n')

    for drive in drives:
        if '2' in drive:
            drive_detected = True
            drive_letter = drive.split(':')[0]
            drive_type = drive.split(':')[1].strip()

            print(f'Flash drive detected [ {drive_letter}: {drive_type} ]\n')

            compressDrive(drive_letter)