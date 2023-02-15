#include <Windows.h>
#include <iostream>

// Declare the function pointer for the add function
typedef int (*AddFunction)(int, int);

int main()
{
    // Load the DLL
    HMODULE hDll = LoadLibrary("mydll.dll");
    if (hDll == NULL) {
        std::cerr << "Failed to load DLL\n";
        return 1;
    }

    // Get the address of the add function
    AddFunction add = (AddFunction)GetProcAddress(hDll, "add");
    if (add == NULL) {
        std::cerr << "Failed to get address of add function\n";
        return 1;
    }

    // Call the add function
    int result = add(2, 3);
    std::cout << "Result: " << result << "\n";

    // Unload the DLL
    FreeLibrary(hDll);

    return 0;
}
