import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_MergeSort
import Math
import Seq
import BoundedInts
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
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary
import UUID
import UTF8
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
import software_amazon_cryptography_services_dynamodb_internaldafny_types

# Module: software_amazon_cryptography_services_dynamodb_internaldafny

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DefaultDynamoDBClientConfigType():
        return DynamoDBClientConfigType_DynamoDBClientConfigType()

    @staticmethod
    def CreateSuccessOfClient(client):
        return Wrappers.Result_Success(client)

    @staticmethod
    def CreateFailureOfError(error):
        return Wrappers.Result_Failure(error)


class DynamoDBClientConfigType:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [DynamoDBClientConfigType_DynamoDBClientConfigType()]
    @classmethod
    def default(cls, ):
        return lambda: DynamoDBClientConfigType_DynamoDBClientConfigType()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DynamoDBClientConfigType(self) -> bool:
        return isinstance(self, DynamoDBClientConfigType_DynamoDBClientConfigType)

class DynamoDBClientConfigType_DynamoDBClientConfigType(DynamoDBClientConfigType, NamedTuple('DynamoDBClientConfigType', [])):
    def __dafnystr__(self) -> str:
        return f'Com_Amazonaws_Dynamodb.DynamoDBClientConfigType.DynamoDBClientConfigType'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DynamoDBClientConfigType_DynamoDBClientConfigType)
    def __hash__(self) -> int:
        return super().__hash__()
