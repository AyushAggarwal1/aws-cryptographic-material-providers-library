import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary
import UTF8
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest
import HMAC
import WrappedHMAC
import HKDF
import WrappedHKDF
import Signature
import KdfCtr
import RSAEncryption
import AwsCryptographyPrimitivesOperations
import Relations
import Seq_MergeSort
import Math
import Seq
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import DafnyLibraries
import FileIO
import GeneralInternals
import MulInternalsNonlinear
import MulInternals
import Mul
import ModInternalsNonlinear
import DivInternalsNonlinear
import ModInternals
import DivInternals
import DivMod
import Power
import Logarithm
import UUID
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AwsArnParsing
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com
import software_amazon_cryptography_keystore_internaldafny
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
import software_amazon_cryptography_primitives_internaldafny
import Aws_Cryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import AwsKmsHierarchicalKeyring
import AwsKmsRsaKeyring
import RawAESKeyring
import RawRSAKeyring
import CMM
import Defaults

# Module: Commitment

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ValidateCommitmentPolicyOnEncrypt(algorithm, commitmentPolicy):
        d_1143_suite_ = AlgorithmSuites.default__.GetSuite(algorithm)
        if ((commitmentPolicy) == (software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKCommitmentPolicy_FORBID__ENCRYPT__ALLOW__DECRYPT()))) and (not(((d_1143_suite_).commitment).is_None)):
            return Wrappers.Outcome_Fail(software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidAlgorithmSuiteInfoOnEncrypt(_dafny.Seq("Configuration conflict. Commitment policy requires only non-committing algorithm suites")))
        elif ((((commitmentPolicy) == (software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKCommitmentPolicy_REQUIRE__ENCRYPT__ALLOW__DECRYPT()))) or ((commitmentPolicy) == (software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKCommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT())))) or ((commitmentPolicy) == (software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_DBE(software_amazon_cryptography_materialproviders_internaldafny_types.DBECommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT())))) and (((d_1143_suite_).commitment).is_None):
            return Wrappers.Outcome_Fail(software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidAlgorithmSuiteInfoOnEncrypt(_dafny.Seq("Configuration conflict. Commitment policy requires only committing algorithm suites")))
        elif True:
            return Wrappers.Outcome_Pass()

    @staticmethod
    def ValidateCommitmentPolicyOnDecrypt(algorithm, commitmentPolicy):
        d_1144_suite_ = AlgorithmSuites.default__.GetSuite(algorithm)
        if ((True) and (((commitmentPolicy) == (software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKCommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT()))) or ((commitmentPolicy) == (software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_DBE(software_amazon_cryptography_materialproviders_internaldafny_types.DBECommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT()))))) and (((d_1144_suite_).commitment).is_None):
            return Wrappers.Outcome_Fail(software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidAlgorithmSuiteInfoOnDecrypt(_dafny.Seq("Configuration conflict. Commitment policy requires only committing algorithm suites")))
        elif True:
            return Wrappers.Outcome_Pass()
