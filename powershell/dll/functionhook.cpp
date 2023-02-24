
//We hoook our custom MyMessageBox function in place of MessageBoxW default function present in the process.
int WINAPI MyMessageBox(HWND hWnd, LPCWSTR lpText, LPCWSTR lpCaption, UINT uType)
{
    // Display a custom message instead of the original message
    LPCWSTR customText = L"Hello from MyMessageBox!";
    return MessageBox(hWnd, customText, lpCaption, uType);
}


BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved)
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
        // Hook the MessageBox function
        DetourTransactionBegin();
        DetourUpdateThread(GetCurrentThread());
        DetourAttach(&(PVOID&)MessageBoxW, MyMessageBox);
        DetourTransactionCommit();
        break;
    case DLL_PROCESS_DETACH:
        // Unhook the MessageBox function
        DetourTransactionBegin();
        DetourUpdateThread(GetCurrentThread());
        DetourDetach(&(PVOID&)MessageBoxW, MyMessageBox);
        DetourTransactionCommit();
        break;
    }
    return TRUE;
}
