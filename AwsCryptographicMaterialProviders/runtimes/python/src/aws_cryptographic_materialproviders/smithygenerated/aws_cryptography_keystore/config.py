# Code generated by smithy-python-codegen DO NOT EDIT.

import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.dafny_to_smithy
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny
from dataclasses import dataclass
import module_
from software_amazon_cryptography_keystore_internaldafny_types import (
    KeyStoreConfig_KeyStoreConfig as DafnyKeyStoreConfig,
)
from typing import Any, Callable, Optional, TypeAlias

from .dafnyImplInterface import DafnyImplInterface
from botocore.client import BaseClient
from smithy_python._private.retries import SimpleRetryStrategy
from smithy_python.interfaces.retries import RetryStrategy

from .models import KMSConfiguration


_ServiceInterceptor = Any
@dataclass(init=False)
class Config:
    """Configuration for KeyStore."""

    interceptors: list[_ServiceInterceptor]
    retry_strategy: RetryStrategy
    dafnyImplInterface: DafnyImplInterface | None

    def __init__(
        self,
        *,
        interceptors: list[_ServiceInterceptor] | None = None,
        retry_strategy: RetryStrategy | None = None,
        dafnyImplInterface: DafnyImplInterface | None = None,
    ):
        """Constructor.

        :param interceptors: The list of interceptors, which are hooks that are called
        during the execution of a request.

        :param retry_strategy: The retry strategy for issuing retry tokens and computing
        retry delays.

        :param dafnyImplInterface:
        """
        self.interceptors = interceptors or []
        self.retry_strategy = retry_strategy or SimpleRetryStrategy()
        self.dafnyImplInterface = dafnyImplInterface

# A callable that allows customizing the config object on each request.
Plugin: TypeAlias = Callable[[Config], None]

class KeyStoreConfig(Config):
    '''
    Smithy-modelled localService Config shape for this localService.
    '''
    ddb_table_name: str
    kms_configuration: KMSConfiguration
    logical_key_store_name: str
    id: Optional[str]
    grant_tokens: Optional[list[str]]
    ddb_client: Optional[BaseClient]
    kms_client: Optional[BaseClient]

    def __init__(
        self,
        ddb_table_name: str,
        kms_configuration: KMSConfiguration,
        logical_key_store_name: str,
        id: Optional[str] = None,
        grant_tokens: Optional[list[str]] = None,
        ddb_client: Optional[BaseClient] = None,
        kms_client: Optional[BaseClient] = None,
    ):
        """Constructor for KeyStoreConfig.

        :param ddb_table_name: The DynamoDB table name that backs this Key Store.
        :param kms_configuration: The AWS KMS Key that protects this Key Store.
        :param logical_key_store_name: The logical name for this Key Store, which is
        cryptographically bound to the keys it holds.
        :param id: An identifier for this Key Store.
        :param grant_tokens: The AWS KMS grant tokens that are used when this Key Store
        calls to AWS KMS.
        :param ddb_client: The DynamoDB client this Key Store uses to call Amazon
        DynamoDB.
        :param kms_client: The KMS client this Key Store uses to call AWS KMS.
        """
        super().__init__()
        self.ddb_table_name = ddb_table_name
        self.kms_configuration = kms_configuration
        self.logical_key_store_name = logical_key_store_name
        self.id = id
        self.grant_tokens = grant_tokens
        self.ddb_client = ddb_client
        self.kms_client = kms_client

def dafny_config_to_smithy_config(dafny_config) -> KeyStoreConfig:
    '''
    Converts the provided Dafny shape for this localService's config
    into the corresponding Smithy-modelled shape.
    '''
    return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.DafnyToSmithy_aws_cryptography_keystore_KeyStoreConfig(dafny_config)

def smithy_config_to_dafny_config(smithy_config) -> DafnyKeyStoreConfig:
    '''
    Converts the provided Smithy-modelled shape for this localService's config
    into the corresponding Dafny shape.
    '''
    return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.SmithyToDafny_aws_cryptography_keystore_KeyStoreConfig(smithy_config)