import os
import sys
import json
import shutil
import subprocess

def get_hardware_info():
    info = {}
    
    # Python & Torch
    info["python_version"] = sys.version
    try:
        import torch
        info["torch_version"] = torch.__version__
        info["cuda_available"] = torch.cuda.is_available()
        if torch.cuda.is_available():
            info["gpu_name"] = torch.cuda.get_device_name(0)
            info["gpu_count"] = torch.cuda.device_count()
            info["gpu_vram_mb"] = round(torch.cuda.get_device_properties(0).total_memory / (1024**2), 2)
            info["cuda_version"] = torch.version.cuda
            info["cudnn_version"] = torch.backends.cudnn.version()
    except Exception as e:
        info["torch_error"] = str(e)

    # Disk Info
    for drive in ["C:\\", "D:\\"]:
        try:
            total, used, free = shutil.disk_usage(drive)
            info[f"disk_{drive[0]}"] = {
                "total_gb": round(total / (1024**3), 2),
                "used_gb": round(used / (1024**3), 2),
                "free_gb": round(free / (1024**3), 2)
            }
        except Exception:
            pass

    # CPU and Memory via PowerShell
    try:
        cpu_cmd = 'powershell -Command "Get-CimInstance Win32_Processor | Select-Object -Property Name, NumberOfCores, NumberOfLogicalProcessors | ConvertTo-Json"'
        res = subprocess.run(cpu_cmd, shell=True, capture_output=True, text=True)
        if res.returncode == 0:
            info["cpu"] = json.loads(res.stdout)
    except Exception as e:
        info["cpu_error"] = str(e)

    try:
        mem_cmd = 'powershell -Command "Get-CimInstance Win32_OperatingSystem | Select-Object -Property TotalVisibleMemorySize, FreePhysicalMemory | ConvertTo-Json"'
        res = subprocess.run(mem_cmd, shell=True, capture_output=True, text=True)
        if res.returncode == 0:
            mem_data = json.loads(res.stdout)
            info["ram"] = {
                "total_gb": round(int(mem_data["TotalVisibleMemorySize"]) / (1024**2), 2),
                "free_gb": round(int(mem_data["FreePhysicalMemory"]) / (1024**2), 2)
            }
    except Exception as e:
        info["ram_error"] = str(e)

    # nvidia-smi
    try:
        smi_cmd = 'nvidia-smi --query-gpu=name,driver_version,memory.total,memory.free,memory.used,temperature.gpu,power.draw --format=csv,noheader,nounits'
        res = subprocess.run(smi_cmd, shell=True, capture_output=True, text=True)
        if res.returncode == 0:
            parts = [p.strip() for p in res.stdout.strip().split(",")]
            if len(parts) >= 7:
                info["nvidia_smi"] = {
                    "name": parts[0],
                    "driver_version": parts[1],
                    "vram_total_mb": float(parts[2]),
                    "vram_free_mb": float(parts[3]),
                    "vram_used_mb": float(parts[4]),
                    "gpu_temp_c": float(parts[5]),
                    "power_draw_w": float(parts[6])
                }
    except Exception as e:
        info["nvidia_smi_error"] = str(e)

    return info

if __name__ == "__main__":
    hw = get_hardware_info()
    print(json.dumps(hw, indent=2))
    with open("reports/HARDWARE_CAPABILITY.json", "w", encoding="utf-8") as f:
        json.dump(hw, f, indent=2)
