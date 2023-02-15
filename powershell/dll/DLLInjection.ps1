# Specify the name of the process to inject the DLL into
$processName = "notepad.exe"

# Get the process ID of the target process
$processId = (Get-Process -Name $processName).Id

# Load the DLL into memory
$dllPath = "C:\path\to\mydll.dll"
$bytes = [System.IO.File]::ReadAllBytes($dllPath)

# Open a handle to the target process
$processHandle = OpenProcess -ProcessId $processId -AccessRights PROCESS_CREATE_THREAD -PassThru

# Allocate memory in the target process to store the DLL path
$memSize = $bytes.Length
$memAddress = VirtualAllocEx -ProcessHandle $processHandle -Size $memSize -AllocationType MEM_COMMIT -Protect PAGE_READWRITE

# Write the DLL path to the allocated memory
WriteProcessMemory -ProcessHandle $processHandle -BaseAddress $memAddress -Buffer $bytes -BufferSize $bytes.Length

# Get the address of the LoadLibrary function in kernel32.dll
$loadLibraryAddress = GetProcAddress -ModuleName kernel32.dll -FunctionName LoadLibraryA

# Create a remote thread in the target process to load the DLL
$remoteThread = CreateRemoteThread -ProcessHandle $processHandle -StartAddress $loadLibraryAddress -Parameter $memAddress -PassThru

# Wait for the remote thread to finish
WaitForSingleObject -Handle $remoteThread -Timeout INFINITE

# Clean up
CloseHandle -Object $remoteThread
VirtualFreeEx -ProcessHandle $processHandle -BaseAddress $memAddress -Size $memSize -FreeType MEM_RELEASE
CloseHandle -Object $processHandle
