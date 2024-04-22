if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "This script requires administrative privileges. Restarting with elevated permissions..."
    Start-Process powershell.exe -Verb RunAs -ArgumentList ("-File", $MyInvocation.MyCommand.Path) #-WindowStyle Hidden
    Exit
}

function Log-Message {
    param (
        [string]$message
    )
    $logFilePath = "C:\Sl66p Security\log.txt"
    
    if (-not (Test-Path -Path $logFilePath)) {
        $null = New-Item -Path (Split-Path $logFilePath) -ItemType Directory
        $null = New-Item -Path $logFilePath -ItemType File
    }
    
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -Path $logFilePath -Value "$timestamp -- $message"
}

function Run-Command {
    param (
        [string]$command
    )
    try {
        Invoke-Expression -Command $command -ErrorAction Stop
        return $true
    }
    catch {
        Log-Message "Error running command: $command. Error: $_"
        return $false
    }
}

function Update-Windows {
    $Sl66pSecurity = "Sl66p Security"

    function InstallWindowsModules {
        # Installs NuGet with Forced
        Install-PackageProvider -Name NuGet -Force

        # Trusts Microsofts PSGallery
        Set-PSRepository -Name 'PSGallery' -InstallationPolicy Trusted
    
        # Install PSWindowsUpdate Module
        Install-Module PSWindowsUpdate

        # Sets Progress file to 1, to indicate modules etc. are installed.
        Set-Content "C:\Sl66p Security\Windows\modules.txt" -Value 1
    }

    function InstallWindowsUpdates {
        # Gets latest Windows updates
        Get-WindowsUpdate | Out-File C:\$Sl66pSecurity\Windows\logs\Updates_"$((Get-Date).ToString('yyyy-MM-dd_HH-mm-ss'))".txt

        #Installs updates, accepts all automatically and reboots.
        Install-WindowsUpdate -Install -AcceptAll #-AutoReboot
    }

    # Checks if folder "AutoUpdates already exists on the server. If it doesn't it creates it."
    $chkPath = "C:\Sl66p Security\Windows"
    $pathExists = Test-Path $chkPath
    if ($pathExists -eq $false) {
        mkdir "C:\Sl66p Security\Windows"
        mkdir "C:\Sl66p Security\Windows\logs"
    }

    $chkFile = "C:\Sl66p Security\modules.txt"
    $fileExists = Test-Path $chkFile
    if ($fileExists -eq $false) {
        New-Item "C:\Sl66p Security\modules.txt"
        Set-Content "C:\Sl66p Security\modules.txt -Value 0"
    }

    $status = Get-Content "C:\Sl66p Security\modules.txt" -First 1

    if ($status -eq 0) {
        # Installs required modules
        InstallWindowsModules
        InstallWindowsUpdates
    }
    elseif ($status -eq 1) {
        # Installs windows updates
        InstallWindowsUpdates
    }
}


function Update-Drivers {
    Log-Message "Starting Driver Updates..."
    if (Run-Command "pnputil /scan" -and Run-Command "pnputil /update-drivers") {
        Log-Message "Driver Updates completed successfully."
    }
    else {
        Log-Message "Driver Updates encountered errors."
    }
}

function Update-WindowsStore {
    Log-Message "Starting Windows Store Updates..."
    $packages = Get-AppxPackage -AllUsers
    foreach ($package in $packages) {
        $packageName = $package.Name
        $installLocation = $package.InstallLocation
        $manifestPath = "$installLocation\AppXManifest.xml"
        
        $result = Add-AppxPackage -DisableDevelopmentMode -Register "$manifestPath" 2>&1
        $exitCode = $?
        if ($exitCode) {
            Log-Message "Package $packageName updated successfully."
        }
        else {
            Log-Message "Failed to update package $packageName. $result"
        }
    }
    Log-Message "Windows Store Updates completed."
}

function Update-ThirdPartySoftware {
    Log-Message "Starting 3rd Party Software Updates..."
    $output = winget upgrade --all --accept-package-agreements --force 2>&1
    if ($LASTEXITCODE -eq 0) {
        Log-Message "3rd Party Software Updates completed successfully."
    }
    else {
        Log-Message "3rd Party Software Updates encountered errors."
        Log-Message "Detailed output: $output"
    }
}

Update-Windows
#Update-Drivers
#Update-WindowsStore
#Update-ThirdPartySoftware
