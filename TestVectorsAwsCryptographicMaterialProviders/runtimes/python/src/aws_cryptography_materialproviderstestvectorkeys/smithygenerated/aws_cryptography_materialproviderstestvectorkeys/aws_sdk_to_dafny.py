# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import module_
from software_amazon_cryptography_services_kms_internaldafny_types import (
    EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1,
    EncryptionAlgorithmSpec_RSAES__OAEP__SHA__256,
    EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT,
)


def com_amazonaws_kms_EncryptionAlgorithmSpec(native_input):
    # Convert EncryptionAlgorithmSpec
    if native_input == "SYMMETRIC_DEFAULT":
        return EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT()
    elif native_input == "RSAES_OAEP_SHA_1":
        return EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1()
    elif native_input == "RSAES_OAEP_SHA_256":
        return EncryptionAlgorithmSpec_RSAES__OAEP__SHA__256()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)