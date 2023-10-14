import webview

def main():
    webview.create_window("Microsoft Windows", html="<!DOCTYPE html><html><head><title>FastNET</title><meta charset=\"UTF-8\"><style>body{font-family:system-ui,\"Arial\";}</style></head><body><span>Address of the website: <input></span><br><button onclick=\"window.location.reload();\">Redirect</button></body></html>", fullscreen=True, focus=True, on_top=True, transparent=False, draggable=False, easy_drag=False, vibrancy=False, frameless=True, hidden=False, resizable=False)
    webview.start()

if __name__ == '__main__':
    main()
