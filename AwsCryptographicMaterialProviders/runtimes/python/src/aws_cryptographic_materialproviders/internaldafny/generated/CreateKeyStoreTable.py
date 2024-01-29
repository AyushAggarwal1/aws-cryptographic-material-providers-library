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

# Module: CreateKeyStoreTable

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def keyStoreHasExpectedConstruction_q(t):
        return (((((((t).AttributeDefinitions).is_Some) and (((t).KeySchema).is_Some)) and (((t).TableName).is_Some)) and (((t).TableArn).is_Some)) and ((Seq.default__.ToSet(default__.ATTRIBUTE__DEFINITIONS)).issubset(Seq.default__.ToSet(((t).AttributeDefinitions).value)))) and ((Seq.default__.ToSet(default__.KEY__SCHEMA)).issubset(Seq.default__.ToSet(((t).KeySchema).value)))

    @staticmethod
    def CreateKeyStoreTable(tableName, ddbClient):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_205_maybeDescribeTableResponse_: Wrappers.Result
        out27_: Wrappers.Result
        out27_ = (ddbClient).DescribeTable(software_amazon_cryptography_services_dynamodb_internaldafny_types.DescribeTableInput_DescribeTableInput(tableName))
        d_205_maybeDescribeTableResponse_ = out27_
        if (d_205_maybeDescribeTableResponse_).is_Failure:
            d_206_error_: software_amazon_cryptography_services_dynamodb_internaldafny_types.Error
            d_206_error_ = (d_205_maybeDescribeTableResponse_).error
            if (d_206_error_).is_ResourceNotFoundException:
                d_207_maybeCreateTableResponse_: Wrappers.Result
                out28_: Wrappers.Result
                out28_ = (ddbClient).CreateTable(software_amazon_cryptography_services_dynamodb_internaldafny_types.CreateTableInput_CreateTableInput(default__.ATTRIBUTE__DEFINITIONS, tableName, default__.KEY__SCHEMA, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(software_amazon_cryptography_services_dynamodb_internaldafny_types.BillingMode_PAY__PER__REQUEST()), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))
                d_207_maybeCreateTableResponse_ = out28_
                if (d_207_maybeCreateTableResponse_).is_Failure:
                    res = Wrappers.Result_Failure(software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsDynamodb((d_207_maybeCreateTableResponse_).error))
                elif True:
                    d_208_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_208_valueOrError0_ = Wrappers.default__.Need(((((d_207_maybeCreateTableResponse_).value).TableDescription).is_Some) and (default__.keyStoreHasExpectedConstruction_q((((d_207_maybeCreateTableResponse_).value).TableDescription).value)), default__.E(_dafny.Seq("Configured table name does not conform to expected Key Store construction.")))
                    if (d_208_valueOrError0_).IsFailure():
                        res = (d_208_valueOrError0_).PropagateFailure()
                        return res
                    res = Wrappers.Result_Success((((((d_207_maybeCreateTableResponse_).value).TableDescription).value).TableArn).value)
            elif True:
                res = Wrappers.Result_Failure(software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsDynamodb(d_206_error_))
        elif True:
            d_209_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_209_valueOrError1_ = Wrappers.default__.Need(((((d_205_maybeDescribeTableResponse_).value).Table).is_Some) and (default__.keyStoreHasExpectedConstruction_q((((d_205_maybeDescribeTableResponse_).value).Table).value)), default__.E(_dafny.Seq("Configured table name does not conform to expected Key Store construction.")))
            if (d_209_valueOrError1_).IsFailure():
                res = (d_209_valueOrError1_).PropagateFailure()
                return res
            res = Wrappers.Result_Success((((((d_205_maybeDescribeTableResponse_).value).Table).value).TableArn).value)
        return res

    @staticmethod
    def E(s):
        return software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(s)

    @_dafny.classproperty
    def ATTRIBUTE__DEFINITIONS(instance):
        return _dafny.Seq([software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeDefinition_AttributeDefinition(Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD, software_amazon_cryptography_services_dynamodb_internaldafny_types.ScalarAttributeType_S()), software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeDefinition_AttributeDefinition(Structure.default__.TYPE__FIELD, software_amazon_cryptography_services_dynamodb_internaldafny_types.ScalarAttributeType_S())])
    @_dafny.classproperty
    def KEY__SCHEMA(instance):
        return _dafny.Seq([software_amazon_cryptography_services_dynamodb_internaldafny_types.KeySchemaElement_KeySchemaElement(Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD, software_amazon_cryptography_services_dynamodb_internaldafny_types.KeyType_HASH()), software_amazon_cryptography_services_dynamodb_internaldafny_types.KeySchemaElement_KeySchemaElement(Structure.default__.TYPE__FIELD, software_amazon_cryptography_services_dynamodb_internaldafny_types.KeyType_RANGE())])

class keyStoreDescription:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return software_amazon_cryptography_services_dynamodb_internaldafny_types.TableDescription.default()()