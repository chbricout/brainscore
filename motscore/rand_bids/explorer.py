"""Module implementing function to explore bids data."""

import os
from collections import namedtuple

import bids

Volume = namedtuple("Volume", ["sub_id", "ses_id", "path", "dataset"])


def list_volumes(dataset_path: str, modality: str = r"T1w") -> list[Volume]:
    """Return list of individual volume in dataset.

    Args:
        dataset_path (str): path to dataset
        modality (str): volume acquisition modality. Defaults to "T1w"

    Returns:
        list[Volume]: list of volumes found
    """
    layout = bids.BIDSLayout(dataset_path, validate=False)
    files = layout.get(suffix=modality, extension="nii.gz")
    volumes = []
    ds_name = os.path.basename(dataset_path)
    for bids_volume in files:
        path = bids_volume.path
        sub = bids_volume.entities["subject"]
        ses = bids_volume.entities["session"]
        volumes.append(Volume(sub, ses, path, ds_name))
    return volumes
