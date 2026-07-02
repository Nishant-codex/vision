from pathlib import Path
import subprocess

def run_cmd(cmd):
    """Run a shell command and raise if it fails."""
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return result.stdout

def main():
    dataset_dir = Path("ds004496")
    subjects = ["sub-01", "sub-02", "sub-03"]

    targets = []

    # ImageNet betas
    for sub in subjects:
        # You can use glob to find all matching run directories
        # or hardcode them if you want
        targets.append(
            f"derivatives/ciftify/{sub}/results/ses-imagenet*_task-imagenet_run-*"
        )

    # COCO betas
    for sub in subjects:
        targets.append(
            f"derivatives/ciftify/{sub}/results/ses-coco_task-coco_run-*"
        )

    # floc ROIs
    for sub in subjects:
        targets.append(
            f"derivatives/ciftify/{sub}/results/ses-floc_task-floc/"
        )

    # BA_exvivo annotations
    for sub in subjects:
        targets.append(f"{sub}/label/lh.BA_exvivo.annot")
        targets.append(f"{sub}/label/rh.BA_exvivo.annot")

    # Stimuli (shared, not per-subject)
    targets.append("stimuli/imagenet/")
    targets.append("stimuli/coco/")

    # Download all targets
    for t in targets:
        print(f"Downloading: {t}")
        run_cmd(["datalad", "get", str(dataset_dir / t)])

if __name__ == "__main__":
    main()