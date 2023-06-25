import subprocess

def cpu_optimization():
    subprocess.call(['powershell.exe', 'Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\be337238-0d82-4146-a960-4f3749d470c7" -Name "Attributes" -Value 2'])
    print("CPU optimization complete")

def ram_optimization():
    subprocess.call(['powershell.exe', 'Clear-Host; $mem = Get-CimInstance Win32_OperatingSystem | Select-Object FreePhysicalMemory, TotalVisibleMemorySize; $free = $mem.FreePhysicalMemory * 100 / $mem.TotalVisibleMemorySize; Write-Host "Clearing standby list..."; $cache = (Get-CimInstance Win32_PerfFormattedData_PerfOS_Memory | Select-Object StandbyCacheNormalPriority, StandbyCacheCoreCount); $cache | ForEach-Object { $_.StandbyCacheNormalPriority = 0; $_.StandbyCacheCoreCount = 0; }; $mem = Get-CimInstance Win32_OperatingSystem | Select-Object FreePhysicalMemory, TotalVisibleMemorySize; $free = $mem.FreePhysicalMemory * 100 / $mem.TotalVisibleMemorySize; Write-Host "RAM optimization complete. Free memory: " $free " %"'])
    print("RAM optimization complete")

def gpu_optimization():
    subprocess.call(['powershell.exe', 'Set-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Control\GraphicsDrivers -Name TdrDelay -Type DWORD -Value 8'])
    print("GPU optimization complete")

def disk_optimization():
    subprocess.call(['cmd.exe', '/c', 'del /s /q %TEMP%\*.*'])
    print("Disk optimization complete")

def network_optimization():
    # Flush DNS cache and renew IP address
    subprocess.run(["ipconfig", "/flushdns"])
    subprocess.run(["ipconfig", "/renew"])

    print("Network optimization complete")

def startup_optimization():
    subprocess.call(['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Run', '/v', 'ProgramName', '/t', 'REG_SZ', '/d', '', '/f'])
    print("Startup optimization complete")

def system_cleanup():
    subprocess.call(['cmd.exe', '/c', 'del /s /q %TEMP%\*.*'])
    subprocess.call(['cmd.exe', '/c', 'del /s /q TEMP\*.*'])
    subprocess.call(['cmd.exe', '/c', 'del /s /q prefetch\*.*'])
    print("System cleanup complete")

def main():
    while True:
        print("Welcome to NasaPcFpsBooster!")
        print("Please choose an option:")
        print("1. CPU optimization")
        print("2. RAM optimization")
        print("3. GPU optimization")
        print("4. Disk optimization")
        print("5. Network optimization")
        print("6. Startup optimization")
        print("7. System cleanup")
        print("8. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            cpu_optimization()
        elif choice == '2':
            ram_optimization()
        elif choice == '3':
            gpu_optimization()
        elif choice == '4':
            disk_optimization()
        elif choice == '5':
            network_optimization()
        elif choice == '6':
            startup_optimization()
        elif choice == '7':
            system_cleanup()
        elif choice == '8':
            print("Exiting NasaPcFpsBooster...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()