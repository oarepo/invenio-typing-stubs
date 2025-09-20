from _hashlib import HASH
from s3fs.core import S3File


def compute_checksum(file_stream: S3File, object_checksum: HASH, part_size: int) -> bytes: ...


def fetch_file(service_id: str, record_id: str, file_key: str): ...


def recompute_multipart_checksum_task(file_instance_id: str): ...
