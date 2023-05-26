from os import PathLike
from pathlib import Path
from typing import Optional

from pydra.mark import annotate, task

__all__ = ["gzip"]


@task
@annotate({"return": {"output_file": Path}})
def gzip(
    input_file: PathLike,
    output_file: Optional[PathLike] = None,
    decompress: bool = False,
) -> Path:
    import gzip as _gzip
    import shutil

    output_file = output_file or (
        Path(input_file).name.split(".gz")[0] if decompress
        else f"{Path(input_file).name}.gz"
    )

    if decompress:
        with _gzip.open(input_file, mode="rb") as fsrc:
            with open(output_file, mode="wb") as fdst:
                shutil.copyfileobj(fsrc, fdst)
    else:
        with open(input_file, mode="rb") as fsrc:
            with _gzip.open(output_file, mode="wb") as fdst:
                shutil.copyfileobj(fsrc, fdst)

    return Path(output_file).resolve()
