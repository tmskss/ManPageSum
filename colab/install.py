import subprocess

def install_requirements():
    """Installs the required packages for the project."""

    print("⏳ Installing base requirements ...")
    cmd = ["python", "-m", "pip", "install", "-r"]
    cmd.append("requirements.txt")
    process_install = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if process_install.returncode != 0:
        raise Exception("😭 Failed to install base requirements")
    else:
        print("✅ Base requirements installed!")
       
    transformers_cmd = "python -m pip install datasets==2.0.0".split()
    process_summary = subprocess.run(
        transformers_cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    if process_summary.returncode != 0:
        raise Exception("😭 Failed to install base requirements")
    else:
        print("✅ Summary requirements installed!")