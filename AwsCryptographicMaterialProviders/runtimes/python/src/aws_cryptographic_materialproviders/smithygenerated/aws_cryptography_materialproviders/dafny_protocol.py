# Code generated by smithy-python-codegen DO NOT EDIT.

import module_
from software_amazon_cryptography_materialproviders_internaldafny_types import (
    AlgorithmSuiteInfo_AlgorithmSuiteInfo as DafnyAlgorithmSuiteInfo,
    CreateAwsKmsDiscoveryKeyringInput_CreateAwsKmsDiscoveryKeyringInput as DafnyCreateAwsKmsDiscoveryKeyringInput,
    CreateAwsKmsDiscoveryMultiKeyringInput_CreateAwsKmsDiscoveryMultiKeyringInput as DafnyCreateAwsKmsDiscoveryMultiKeyringInput,
    CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput as DafnyCreateAwsKmsHierarchicalKeyringInput,
    CreateAwsKmsKeyringInput_CreateAwsKmsKeyringInput as DafnyCreateAwsKmsKeyringInput,
    CreateAwsKmsMrkDiscoveryKeyringInput_CreateAwsKmsMrkDiscoveryKeyringInput as DafnyCreateAwsKmsMrkDiscoveryKeyringInput,
    CreateAwsKmsMrkDiscoveryMultiKeyringInput_CreateAwsKmsMrkDiscoveryMultiKeyringInput as DafnyCreateAwsKmsMrkDiscoveryMultiKeyringInput,
    CreateAwsKmsMrkKeyringInput_CreateAwsKmsMrkKeyringInput as DafnyCreateAwsKmsMrkKeyringInput,
    CreateAwsKmsMrkMultiKeyringInput_CreateAwsKmsMrkMultiKeyringInput as DafnyCreateAwsKmsMrkMultiKeyringInput,
    CreateAwsKmsMultiKeyringInput_CreateAwsKmsMultiKeyringInput as DafnyCreateAwsKmsMultiKeyringInput,
    CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput as DafnyCreateAwsKmsRsaKeyringInput,
    CreateCryptographicMaterialsCacheInput_CreateCryptographicMaterialsCacheInput as DafnyCreateCryptographicMaterialsCacheInput,
    CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput as DafnyCreateDefaultClientSupplierInput,
    CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput as DafnyCreateDefaultCryptographicMaterialsManagerInput,
    CreateMultiKeyringInput_CreateMultiKeyringInput as DafnyCreateMultiKeyringInput,
    CreateRawAesKeyringInput_CreateRawAesKeyringInput as DafnyCreateRawAesKeyringInput,
    CreateRawRsaKeyringInput_CreateRawRsaKeyringInput as DafnyCreateRawRsaKeyringInput,
    CreateRequiredEncryptionContextCMMInput_CreateRequiredEncryptionContextCMMInput as DafnyCreateRequiredEncryptionContextCMMInput,
    DecryptionMaterials_DecryptionMaterials as DafnyDecryptionMaterials,
    EncryptionMaterials_EncryptionMaterials as DafnyEncryptionMaterials,
    InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput as DafnyInitializeDecryptionMaterialsInput,
    InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput as DafnyInitializeEncryptionMaterialsInput,
    ValidDecryptionMaterialsTransitionInput_ValidDecryptionMaterialsTransitionInput as DafnyValidDecryptionMaterialsTransitionInput,
    ValidEncryptionMaterialsTransitionInput_ValidEncryptionMaterialsTransitionInput as DafnyValidEncryptionMaterialsTransitionInput,
    ValidateCommitmentPolicyOnDecryptInput_ValidateCommitmentPolicyOnDecryptInput as DafnyValidateCommitmentPolicyOnDecryptInput,
    ValidateCommitmentPolicyOnEncryptInput_ValidateCommitmentPolicyOnEncryptInput as DafnyValidateCommitmentPolicyOnEncryptInput,
)


import Wrappers
from typing import Union

class DafnyRequest:
    operation_name: str

    # dafny_operation_input can take on any one of the types
    # of the input values passed to the Dafny implementation
    dafny_operation_input: Union[
        DafnyValidEncryptionMaterialsTransitionInput,
        DafnyAlgorithmSuiteInfo,
        DafnyCreateDefaultClientSupplierInput,
        DafnyCreateRequiredEncryptionContextCMMInput,
        DafnyCreateAwsKmsKeyringInput,
        DafnyCreateAwsKmsMrkMultiKeyringInput,
        DafnyInitializeEncryptionMaterialsInput,
        DafnyEncryptionMaterials,
        DafnyCreateAwsKmsDiscoveryKeyringInput,
        DafnyInitializeDecryptionMaterialsInput,
        DafnyValidateCommitmentPolicyOnDecryptInput,
        DafnyCreateAwsKmsDiscoveryMultiKeyringInput,
        DafnyCreateAwsKmsMrkDiscoveryMultiKeyringInput,
        DafnyCreateAwsKmsRsaKeyringInput,
        DafnyValidDecryptionMaterialsTransitionInput,
        DafnyCreateDefaultCryptographicMaterialsManagerInput,
        DafnyCreateRawRsaKeyringInput,
        DafnyValidateCommitmentPolicyOnEncryptInput,
        DafnyCreateAwsKmsMrkKeyringInput,
        DafnyCreateAwsKmsHierarchicalKeyringInput,
        DafnyCreateAwsKmsMrkDiscoveryKeyringInput,
        DafnyCreateAwsKmsMultiKeyringInput,
        DafnyCreateRawAesKeyringInput,
        DafnyCreateCryptographicMaterialsCacheInput,
        DafnyCreateMultiKeyringInput,
        DafnyDecryptionMaterials,
    ]

    def __init__(self, operation_name, dafny_operation_input):
        self.operation_name = operation_name
        self.dafny_operation_input = dafny_operation_input

class DafnyResponse(Wrappers.Result):
    def __init__(self):
        super().__init__(self)