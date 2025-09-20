from .ext import InvenioRecordsPermissions as InvenioRecordsPermissions
from .policies import BasePermissionPolicy as BasePermissionPolicy, RecordPermissionPolicy as RecordPermissionPolicy

__all__ = ['__version__', 'BasePermissionPolicy', 'InvenioRecordsPermissions', 'RecordPermissionPolicy']

__version__: str
