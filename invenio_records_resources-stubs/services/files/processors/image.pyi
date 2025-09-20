from invenio_records_resources.records.api import FileRecord

class ImageMetadataExtractor:
    def can_process(self, file_record: FileRecord): ...
