from pathlib import Path
import subprocess
import glob


def run_cmd(cmd):
    """Run a shell command and raise if it fails."""
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return result.stdout


def download_matches(pattern):
    matched = glob.glob(str(pattern))
    if not matched:
        print(f"WARNING: no matches for {pattern}")
    for m in matched:
        print(f"Downloading: {m}")
        run_cmd(["datalad", "get", m])


def main():
    dataset_dir = Path("ds004496")
    if not dataset_dir.exists():
        raise FileNotFoundError(f"Dataset directory not found: {dataset_dir}")

    subjects = ["sub-02", "sub-03"] #["sub-01"]#, 

    # ImageNet betas
    for sub in subjects:
        pattern = (
            dataset_dir /
            f"derivatives/ciftify/{sub}/results/ses-imagenet*_task-imagenet_run-*"
        )
        download_matches(pattern)

    # COCO betas
    for sub in subjects:
        pattern = (
            dataset_dir /
            f"derivatives/ciftify/{sub}/results/ses-coco_task-coco_run-*"
        )
        download_matches(pattern)

    # floc ROIs
    for sub in subjects:
        pattern = (
            dataset_dir /
            f"derivatives/ciftify/{sub}/results/ses-floc_task-floc"
        )
        download_matches(pattern)

    # BA_exvivo annotations
    for sub in subjects:
        # pattern = dataset_dir / f"{sub}/label/lh.BA_exvivo.annot"
        # download_matches(pattern)

        pattern = dataset_dir / f"{sub}/standard_fsLR_surface/{sub}.BA_exvivo.32k_fs_LR.dlabel.nii"
        download_matches(pattern)

    # Stimuli (shared, not per-subject)
    # pattern = dataset_dir / "stimuli/imagenet/*"
    # download_matches(pattern)

    # pattern = dataset_dir / "stimuli/coco/*"
    # download_matches(pattern)

    # Instead, download only info metadata if available:
    pattern = dataset_dir / "stimuli/imagenet/info/*"
    download_matches(pattern)

    pattern = dataset_dir / "stimuli/coco/info/*"
    download_matches(pattern)

if __name__ == "__main__":
    main()