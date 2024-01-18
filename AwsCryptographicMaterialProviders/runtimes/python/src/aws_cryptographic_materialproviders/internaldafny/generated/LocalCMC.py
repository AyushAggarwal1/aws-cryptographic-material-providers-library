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

# Module: LocalCMC

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def RemoveValue(k0, m):
        d_755_m_k_: _dafny.Map
        d_755_m_k_ = (m) - (_dafny.Set({k0}))

    @_dafny.classproperty
    def NULL(instance):
        return Ref_Null()
    @_dafny.classproperty
    def INT32__MAX__VALUE(instance):
        return 2040109465
    @_dafny.classproperty
    def INT64__MAX__VALUE(instance):
        return 8762203435012037017

class Ref:
    @classmethod
    def default(cls, ):
        return lambda: Ref_Null()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Ptr(self) -> bool:
        return isinstance(self, Ref_Ptr)
    @property
    def is_Null(self) -> bool:
        return isinstance(self, Ref_Null)

class Ref_Ptr(Ref, NamedTuple('Ptr', [('deref', Any)])):
    def __dafnystr__(self) -> str:
        return f'LocalCMC.Ref.Ptr({_dafny.string_of(self.deref)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Ref_Ptr) and self.deref == __o.deref
    def __hash__(self) -> int:
        return super().__hash__()

class Ref_Null(Ref, NamedTuple('Null', [])):
    def __dafnystr__(self) -> str:
        return f'LocalCMC.Ref.Null'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Ref_Null)
    def __hash__(self) -> int:
        return super().__hash__()


class CacheEntry:
    def  __init__(self):
        self.prev: Ref = Ref.default()()
        self.next: Ref = Ref.default()()
        self.messagesUsed: int = None
        self.bytesUsed: int = None
        self._identifier: _dafny.Seq = _dafny.Seq({})
        self._materials: software_amazon_cryptography_materialproviders_internaldafny_types.Materials = None
        self._creationTime: int = None
        self._expiryTime: int = None
        pass

    def __dafnystr__(self) -> str:
        return "LocalCMC.CacheEntry"
    def ctor__(self, materials_k, identifier_k, creationTime_k, expiryTime_k, messagesUsed_k, bytesUsed_k):
        (self)._materials = materials_k
        (self)._identifier = identifier_k
        (self)._creationTime = creationTime_k
        (self)._expiryTime = expiryTime_k
        (self).messagesUsed = messagesUsed_k
        (self).bytesUsed = bytesUsed_k
        (self).prev = default__.NULL
        (self).next = default__.NULL

    @property
    def identifier(self):
        return self._identifier
    @property
    def materials(self):
        return self._materials
    @property
    def creationTime(self):
        return self._creationTime
    @property
    def expiryTime(self):
        return self._expiryTime

class DoublyLinkedCacheEntryList:
    def  __init__(self):
        self.head: Ref = Ref.default()()
        self.tail: Ref = Ref.default()()
        pass

    def __dafnystr__(self) -> str:
        return "LocalCMC.DoublyLinkedCacheEntryList"
    def ctor__(self):
        (self).head = Ref_Null()
        (self).tail = Ref_Null()

    def pushCell(self, toPush):
        d_756_cRef_: Ref
        d_756_cRef_ = Ref_Ptr(toPush)
        if (self.head).is_Ptr:
            obj0_ = (self.head).deref
            obj0_.prev = d_756_cRef_
            (toPush).next = self.head
            (self).head = d_756_cRef_
        elif True:
            (self).head = d_756_cRef_
            (self).tail = self.head

    def moveToFront(self, c):
        if ((self.head).deref) != (c):
            d_757_toPush_: Ref
            d_757_toPush_ = Ref_Ptr(c)
            (self).remove(c)
            if (self.head).is_Ptr:
                obj1_ = (self.head).deref
                obj1_.prev = d_757_toPush_
                obj2_ = (d_757_toPush_).deref
                obj2_.next = self.head
                (self).head = d_757_toPush_
            elif True:
                (self).head = d_757_toPush_
                (self).tail = self.head

    def remove(self, toRemove):
        if (toRemove.prev).is_Null:
            (self).head = toRemove.next
        elif True:
            obj3_ = (toRemove.prev).deref
            obj3_.next = toRemove.next
        if (toRemove.next).is_Null:
            (self).tail = toRemove.prev
        elif True:
            obj4_ = (toRemove.next).deref
            obj4_.prev = toRemove.prev
        with _dafny.label("0"):
            pass
        (toRemove).next = default__.NULL
        (toRemove).prev = default__.NULL


class LocalCMC(software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsCache):
    def  __init__(self):
        self.queue: DoublyLinkedCacheEntryList = None
        self.cache: DafnyLibraries.MutableMap = None
        self._entryCapacity: int = int(0)
        self._entryPruningTailSize: int = int(0)
        pass

    def __dafnystr__(self) -> str:
        return "LocalCMC.LocalCMC"
    def PutCacheEntry(self, input):
        out113_: Wrappers.Result
        out113_ = software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsCache.PutCacheEntry(self, input)
        return out113_

    def UpdateUsageMetadata(self, input):
        out114_: Wrappers.Result
        out114_ = software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsCache.UpdateUsageMetadata(self, input)
        return out114_

    def GetCacheEntry(self, input):
        out115_: Wrappers.Result
        out115_ = software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsCache.GetCacheEntry(self, input)
        return out115_

    def DeleteCacheEntry(self, input):
        out116_: Wrappers.Result
        out116_ = software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsCache.DeleteCacheEntry(self, input)
        return out116_

    def ctor__(self, entryCapacity_k, entryPruningTailSize_k):
        (self)._entryCapacity = entryCapacity_k
        (self)._entryPruningTailSize = entryPruningTailSize_k
        nw28_ = DafnyLibraries.MutableMap()
        (self).cache = nw28_
        nw29_ = DoublyLinkedCacheEntryList()
        nw29_.ctor__()
        (self).queue = nw29_

    def GetCacheEntry_k(self, input):
        output: Wrappers.Result = None
        d_758_now_: int
        out117_: int
        out117_ = Time.default__.CurrentRelativeTime()
        d_758_now_ = out117_
        out118_: Wrappers.Result
        out118_ = (self).GetCacheEntryWithTime(input, d_758_now_)
        output = out118_
        return output

    def GetCacheEntryWithTime(self, input, now):
        output: Wrappers.Result = None
        if (self.cache).HasKey((input).identifier):
            d_759_entry_: CacheEntry
            d_759_entry_ = (self.cache).Select((input).identifier)
            if (now) <= ((d_759_entry_).expiryTime):
                (self.queue).moveToFront(d_759_entry_)
                output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryOutput_GetCacheEntryOutput((d_759_entry_).materials, (d_759_entry_).creationTime, (d_759_entry_).expiryTime, d_759_entry_.messagesUsed, d_759_entry_.bytesUsed))
                d_760___v0_: tuple
                d_761_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
                out119_: Wrappers.Result
                out119_ = (self).pruning(now)
                d_761_valueOrError0_ = out119_
                if (d_761_valueOrError0_).IsFailure():
                    output = (d_761_valueOrError0_).PropagateFailure()
                    return output
                d_760___v0_ = (d_761_valueOrError0_).Extract()
            elif True:
                d_762___v1_: tuple
                d_763_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
                out120_: Wrappers.Result
                out120_ = (self).DeleteCacheEntry_k(software_amazon_cryptography_materialproviders_internaldafny_types.DeleteCacheEntryInput_DeleteCacheEntryInput((input).identifier))
                d_763_valueOrError1_ = out120_
                if (d_763_valueOrError1_).IsFailure():
                    output = (d_763_valueOrError1_).PropagateFailure()
                    return output
                d_762___v1_ = (d_763_valueOrError1_).Extract()
                output = Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_EntryDoesNotExist(_dafny.Seq("Entry past TTL")))
        elif True:
            output = Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_EntryDoesNotExist(_dafny.Seq("Entry does not exist")))
        return output

    def PutCacheEntry_k(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        if ((self).entryCapacity) == (0):
            output = Wrappers.Result_Success(())
            return output
        if (self.cache).HasKey((input).identifier):
            d_764___v2_: tuple
            d_765_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            out121_: Wrappers.Result
            out121_ = (self).DeleteCacheEntry_k(software_amazon_cryptography_materialproviders_internaldafny_types.DeleteCacheEntryInput_DeleteCacheEntryInput((input).identifier))
            d_765_valueOrError0_ = out121_
            if (d_765_valueOrError0_).IsFailure():
                output = (d_765_valueOrError0_).PropagateFailure()
                return output
            d_764___v2_ = (d_765_valueOrError0_).Extract()
        if ((self).entryCapacity) == ((self.cache).Size()):
            d_766___v3_: tuple
            d_767_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            out122_: Wrappers.Result
            out122_ = (self).DeleteCacheEntry_k(software_amazon_cryptography_materialproviders_internaldafny_types.DeleteCacheEntryInput_DeleteCacheEntryInput(((self.queue.tail).deref).identifier))
            d_767_valueOrError1_ = out122_
            if (d_767_valueOrError1_).IsFailure():
                output = (d_767_valueOrError1_).PropagateFailure()
                return output
            d_766___v3_ = (d_767_valueOrError1_).Extract()
        d_768_cell_: CacheEntry
        nw30_ = CacheEntry()
        nw30_.ctor__((input).materials, (input).identifier, (input).creationTime, (input).expiryTime, ((input).messagesUsed).UnwrapOr(0), ((input).bytesUsed).UnwrapOr(0))
        d_768_cell_ = nw30_
        (self.queue).pushCell(d_768_cell_)
        (self.cache).Put((input).identifier, d_768_cell_)
        output = Wrappers.Result_Success(())
        return output

    def DeleteCacheEntry_k(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        if (self.cache).HasKey((input).identifier):
            d_769_cell_: CacheEntry
            d_769_cell_ = (self.cache).Select((input).identifier)
            with _dafny.label("1"):
                (self.cache).Remove((input).identifier)
                pass
            (self.queue).remove(d_769_cell_)
        output = Wrappers.Result_Success(())
        return output

    def UpdateUsageMetadata_k(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        if (self.cache).HasKey((input).identifier):
            d_770_cell_: CacheEntry
            d_770_cell_ = (self.cache).Select((input).identifier)
            if ((d_770_cell_.messagesUsed) <= ((default__.INT32__MAX__VALUE) - (1))) and ((d_770_cell_.bytesUsed) <= ((default__.INT32__MAX__VALUE) - ((input).bytesUsed))):
                rhs0_ = (d_770_cell_.messagesUsed) + (1)
                rhs1_ = (d_770_cell_.bytesUsed) + ((input).bytesUsed)
                lhs0_ = d_770_cell_
                lhs1_ = d_770_cell_
                lhs0_.messagesUsed = rhs0_
                lhs1_.bytesUsed = rhs1_
            elif True:
                d_771___v4_: tuple
                d_772_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
                out123_: Wrappers.Result
                out123_ = (self).DeleteCacheEntry_k(software_amazon_cryptography_materialproviders_internaldafny_types.DeleteCacheEntryInput_DeleteCacheEntryInput((input).identifier))
                d_772_valueOrError0_ = out123_
                if (d_772_valueOrError0_).IsFailure():
                    output = (d_772_valueOrError0_).PropagateFailure()
                    return output
                d_771___v4_ = (d_772_valueOrError0_).Extract()
        output = Wrappers.Result_Success(())
        return output
        return output

    def pruning(self, now):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        hi6_ = (self).entryPruningTailSize
        for d_773_i_ in range(0, hi6_):
            if (self.queue.tail).is_Ptr:
                if (((self.queue.tail).deref).expiryTime) < (now):
                    d_774___v5_: tuple
                    d_775_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
                    out124_: Wrappers.Result
                    out124_ = (self).DeleteCacheEntry_k(software_amazon_cryptography_materialproviders_internaldafny_types.DeleteCacheEntryInput_DeleteCacheEntryInput(((self.queue.tail).deref).identifier))
                    d_775_valueOrError0_ = out124_
                    if (d_775_valueOrError0_).IsFailure():
                        output = (d_775_valueOrError0_).PropagateFailure()
                        return output
                    d_774___v5_ = (d_775_valueOrError0_).Extract()
                elif True:
                    output = Wrappers.Result_Success(())
                    return output
            elif True:
                output = Wrappers.Result_Success(())
                return output
        output = Wrappers.Result_Success(())
        return output
        return output

    @property
    def entryCapacity(self):
        return self._entryCapacity
    @property
    def entryPruningTailSize(self):
        return self._entryPruningTailSize