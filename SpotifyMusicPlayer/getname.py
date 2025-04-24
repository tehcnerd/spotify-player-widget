import win32gui
import win32process
import psutil

def get_spotify_title():
    def enum_handler(hwnd, result):
        if win32gui.IsWindowVisible(hwnd):
            tid, pid = win32process.GetWindowThreadProcessId(hwnd)
            try:
                proc = psutil.Process(pid)
                if "spotify" in proc.name().lower():
                    title = win32gui.GetWindowText(hwnd)
                    if title and " - " in title:
                        result.append(title)
                    else:
                        result.append('NAN - Play a Song')        
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass  # Ignore processes that cannot be accessed

    result = []
    win32gui.EnumWindows(enum_handler, result)
    
    # If result is empty, return 'NAN - Play a Song'
    if not result:
        return 'NAN - Play a Song'
    
    return result[0]