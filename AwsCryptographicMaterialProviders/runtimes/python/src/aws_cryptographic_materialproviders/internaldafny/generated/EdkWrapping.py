import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_materialproviders.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptography_primitives.internaldafny.generated.ExternRandom as ExternRandom
import aws_cryptography_primitives.internaldafny.generated.Random as Random
import aws_cryptography_primitives.internaldafny.generated.AESEncryption as AESEncryption
import aws_cryptography_primitives.internaldafny.generated.ExternDigest as ExternDigest
import aws_cryptography_primitives.internaldafny.generated.Digest as Digest
import aws_cryptography_primitives.internaldafny.generated.HMAC as HMAC
import aws_cryptography_primitives.internaldafny.generated.WrappedHMAC as WrappedHMAC
import aws_cryptography_primitives.internaldafny.generated.HKDF as HKDF
import aws_cryptography_primitives.internaldafny.generated.WrappedHKDF as WrappedHKDF
import aws_cryptography_primitives.internaldafny.generated.Signature as Signature
import aws_cryptography_primitives.internaldafny.generated.KdfCtr as KdfCtr
import aws_cryptography_primitives.internaldafny.generated.RSAEncryption as RSAEncryption
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import standard_library.internaldafny.generated.Unicode as Unicode
import standard_library.internaldafny.generated.Functions as Functions
import standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import standard_library.internaldafny.generated.FileIO as FileIO
import standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import standard_library.internaldafny.generated.MulInternals as MulInternals
import standard_library.internaldafny.generated.Mul as Mul
import standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import standard_library.internaldafny.generated.ModInternals as ModInternals
import standard_library.internaldafny.generated.DivInternals as DivInternals
import standard_library.internaldafny.generated.DivMod as DivMod
import standard_library.internaldafny.generated.Power as Power
import standard_library.internaldafny.generated.Logarithm as Logarithm
import standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.Time as Time
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.SortedSets as SortedSets
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64 as Base64
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import standard_library.internaldafny.generated.Actions as Actions
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_materialproviders.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws as Com_Amazonaws
import com_amazonaws_dynamodb.internaldafny.generated.Com as Com
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStore as KeyStore
import aws_cryptographic_materialproviders.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_materialproviders.internaldafny.generated.Materials as Materials
import aws_cryptographic_materialproviders.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_materialproviders.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_materialproviders.internaldafny.generated.Constants as Constants
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping

# Module: aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def WrapEdkMaterial(encryptionMaterials, wrap, generateAndWrap):
        ret: Wrappers.Result = None
        d_504_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_504_valueOrError0_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterials(encryptionMaterials), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid materials for encryption.")))
        if (d_504_valueOrError0_).IsFailure():
            ret = (d_504_valueOrError0_).PropagateFailure()
            return ret
        if (((encryptionMaterials).plaintextDataKey).is_Some) and ((((encryptionMaterials).algorithmSuite).edkWrapping).is_DIRECT__KEY__WRAPPING):
            d_505_directOutput_: MaterialWrapping.WrapOutput
            d_506_valueOrError1_: Wrappers.Result = None
            out75_: Wrappers.Result
            out75_ = (wrap).Invoke(MaterialWrapping.WrapInput_WrapInput(((encryptionMaterials).plaintextDataKey).value, (encryptionMaterials).algorithmSuite, (encryptionMaterials).encryptionContext))
            d_506_valueOrError1_ = out75_
            if (d_506_valueOrError1_).IsFailure():
                ret = (d_506_valueOrError1_).PropagateFailure()
                return ret
            d_505_directOutput_ = (d_506_valueOrError1_).Extract()
            ret = Wrappers.Result_Success(WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput((d_505_directOutput_).wrappedMaterial, Wrappers.Option_None(), (d_505_directOutput_).wrapInfo))
            return ret
        elif (((encryptionMaterials).plaintextDataKey).is_Some) and ((((encryptionMaterials).algorithmSuite).edkWrapping).is_IntermediateKeyWrapping):
            d_507_intermediateOutput_: IntermediateKeyWrapping.IntermediateWrapOutput
            d_508_valueOrError2_: Wrappers.Result = None
            out76_: Wrappers.Result
            out76_ = IntermediateKeyWrapping.default__.IntermediateWrap(generateAndWrap, ((encryptionMaterials).plaintextDataKey).value, (encryptionMaterials).algorithmSuite, (encryptionMaterials).encryptionContext)
            d_508_valueOrError2_ = out76_
            if (d_508_valueOrError2_).IsFailure():
                ret = (d_508_valueOrError2_).PropagateFailure()
                return ret
            d_507_intermediateOutput_ = (d_508_valueOrError2_).Extract()
            ret = Wrappers.Result_Success(WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput((d_507_intermediateOutput_).wrappedMaterial, Wrappers.Option_Some((d_507_intermediateOutput_).symmetricSigningKey), (d_507_intermediateOutput_).wrapInfo))
            return ret
        elif (((encryptionMaterials).plaintextDataKey).is_None) and ((((encryptionMaterials).algorithmSuite).edkWrapping).is_DIRECT__KEY__WRAPPING):
            d_509_directOutput_: MaterialWrapping.GenerateAndWrapOutput
            d_510_valueOrError3_: Wrappers.Result = None
            out77_: Wrappers.Result
            out77_ = (generateAndWrap).Invoke(MaterialWrapping.GenerateAndWrapInput_GenerateAndWrapInput((encryptionMaterials).algorithmSuite, (encryptionMaterials).encryptionContext))
            d_510_valueOrError3_ = out77_
            if (d_510_valueOrError3_).IsFailure():
                ret = (d_510_valueOrError3_).PropagateFailure()
                return ret
            d_509_directOutput_ = (d_510_valueOrError3_).Extract()
            ret = Wrappers.Result_Success(WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput((d_509_directOutput_).plaintextMaterial, (d_509_directOutput_).wrappedMaterial, Wrappers.Option_None(), (d_509_directOutput_).wrapInfo))
            return ret
        elif (((encryptionMaterials).plaintextDataKey).is_None) and ((((encryptionMaterials).algorithmSuite).edkWrapping).is_IntermediateKeyWrapping):
            d_511_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_511_valueOrError4_ = Wrappers.default__.Need((((encryptionMaterials).algorithmSuite).commitment).is_HKDF, AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid algorithm suite: suites with intermediate key wrapping must use key commitment.")))
            if (d_511_valueOrError4_).IsFailure():
                ret = (d_511_valueOrError4_).PropagateFailure()
                return ret
            d_512_intermediateOutput_: IntermediateKeyWrapping.IntermediateGenerateAndWrapOutput
            d_513_valueOrError5_: Wrappers.Result = None
            out78_: Wrappers.Result
            out78_ = IntermediateKeyWrapping.default__.IntermediateGenerateAndWrap(generateAndWrap, (encryptionMaterials).algorithmSuite, (encryptionMaterials).encryptionContext)
            d_513_valueOrError5_ = out78_
            if (d_513_valueOrError5_).IsFailure():
                ret = (d_513_valueOrError5_).PropagateFailure()
                return ret
            d_512_intermediateOutput_ = (d_513_valueOrError5_).Extract()
            ret = Wrappers.Result_Success(WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput((d_512_intermediateOutput_).plaintextDataKey, (d_512_intermediateOutput_).wrappedMaterial, Wrappers.Option_Some((d_512_intermediateOutput_).symmetricSigningKey), (d_512_intermediateOutput_).wrapInfo))
            return ret
        elif True:
            pass
        return ret

    @staticmethod
    def UnwrapEdkMaterial(wrappedMaterial, decryptionMaterials, unwrap):
        ret: Wrappers.Result = None
        d_514_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_514_valueOrError0_ = Wrappers.default__.Need(Materials.default__.ValidDecryptionMaterials(decryptionMaterials), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid materials for decryption.")))
        if (d_514_valueOrError0_).IsFailure():
            ret = (d_514_valueOrError0_).PropagateFailure()
            return ret
        if (((decryptionMaterials).algorithmSuite).edkWrapping).is_DIRECT__KEY__WRAPPING:
            d_515_directOutput_: MaterialWrapping.UnwrapOutput
            d_516_valueOrError1_: Wrappers.Result = None
            out79_: Wrappers.Result
            out79_ = (unwrap).Invoke(MaterialWrapping.UnwrapInput_UnwrapInput(wrappedMaterial, (decryptionMaterials).algorithmSuite, (decryptionMaterials).encryptionContext))
            d_516_valueOrError1_ = out79_
            if (d_516_valueOrError1_).IsFailure():
                ret = (d_516_valueOrError1_).PropagateFailure()
                return ret
            d_515_directOutput_ = (d_516_valueOrError1_).Extract()
            ret = Wrappers.Result_Success(UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput((d_515_directOutput_).unwrappedMaterial, Wrappers.Option_None(), (d_515_directOutput_).unwrapInfo))
            return ret
        elif (((decryptionMaterials).algorithmSuite).edkWrapping).is_IntermediateKeyWrapping:
            d_517_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_517_valueOrError2_ = Wrappers.default__.Need((len(wrappedMaterial)) >= ((((((decryptionMaterials).algorithmSuite).encrypt).AES__GCM).keyLength) + (((((decryptionMaterials).algorithmSuite).encrypt).AES__GCM).tagLength)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid material for Intermediate Unwrapping")))
            if (d_517_valueOrError2_).IsFailure():
                ret = (d_517_valueOrError2_).PropagateFailure()
                return ret
            d_518_intermediateOutput_: IntermediateKeyWrapping.IntermediateUnwrapOutput
            d_519_valueOrError3_: Wrappers.Result = None
            out80_: Wrappers.Result
            out80_ = IntermediateKeyWrapping.default__.IntermediateUnwrap(unwrap, wrappedMaterial, (decryptionMaterials).algorithmSuite, (decryptionMaterials).encryptionContext)
            d_519_valueOrError3_ = out80_
            if (d_519_valueOrError3_).IsFailure():
                ret = (d_519_valueOrError3_).PropagateFailure()
                return ret
            d_518_intermediateOutput_ = (d_519_valueOrError3_).Extract()
            ret = Wrappers.Result_Success(UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput((d_518_intermediateOutput_).plaintextDataKey, Wrappers.Option_Some((d_518_intermediateOutput_).symmetricSigningKey), (d_518_intermediateOutput_).unwrapInfo))
            return ret
        elif True:
            pass
        return ret

    @staticmethod
    def GetProviderWrappedMaterial(material, algSuite):
        if ((algSuite).edkWrapping).is_DIRECT__KEY__WRAPPING:
            return Wrappers.Result_Success(material)
        elif True:
            d_520_deserializedWrappedRes_ = IntermediateKeyWrapping.default__.DeserializeIntermediateWrappedMaterial(material, algSuite)
            if (d_520_deserializedWrappedRes_).is_Failure:
                return Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to deserialize Intermediate Key Wrapped material.")))
            elif True:
                return Wrappers.Result_Success(((d_520_deserializedWrappedRes_).value).providerWrappedIkm)


class WrapEdkMaterialOutput:
    @classmethod
    def default(cls, default_T):
        return lambda: WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput(_dafny.Seq({}), Wrappers.Option.default()(), default_T())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_WrapOnlyEdkMaterialOutput(self) -> bool:
        return isinstance(self, WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput)
    @property
    def is_GenerateAndWrapEdkMaterialOutput(self) -> bool:
        return isinstance(self, WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput)

class WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput(WrapEdkMaterialOutput, NamedTuple('WrapOnlyEdkMaterialOutput', [('wrappedMaterial', Any), ('symmetricSigningKey', Any), ('wrapInfo', Any)])):
    def __dafnystr__(self) -> str:
        return f'EdkWrapping.WrapEdkMaterialOutput.WrapOnlyEdkMaterialOutput({_dafny.string_of(self.wrappedMaterial)}, {_dafny.string_of(self.symmetricSigningKey)}, {_dafny.string_of(self.wrapInfo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput) and self.wrappedMaterial == __o.wrappedMaterial and self.symmetricSigningKey == __o.symmetricSigningKey and self.wrapInfo == __o.wrapInfo
    def __hash__(self) -> int:
        return super().__hash__()

class WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput(WrapEdkMaterialOutput, NamedTuple('GenerateAndWrapEdkMaterialOutput', [('plaintextDataKey', Any), ('wrappedMaterial', Any), ('symmetricSigningKey', Any), ('wrapInfo', Any)])):
    def __dafnystr__(self) -> str:
        return f'EdkWrapping.WrapEdkMaterialOutput.GenerateAndWrapEdkMaterialOutput({_dafny.string_of(self.plaintextDataKey)}, {_dafny.string_of(self.wrappedMaterial)}, {_dafny.string_of(self.symmetricSigningKey)}, {_dafny.string_of(self.wrapInfo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput) and self.plaintextDataKey == __o.plaintextDataKey and self.wrappedMaterial == __o.wrappedMaterial and self.symmetricSigningKey == __o.symmetricSigningKey and self.wrapInfo == __o.wrapInfo
    def __hash__(self) -> int:
        return super().__hash__()


class UnwrapEdkMaterialOutput:
    @classmethod
    def default(cls, default_T):
        return lambda: UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput(_dafny.Seq({}), Wrappers.Option.default()(), default_T())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UnwrapEdkMaterialOutput(self) -> bool:
        return isinstance(self, UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput)

class UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput(UnwrapEdkMaterialOutput, NamedTuple('UnwrapEdkMaterialOutput', [('plaintextDataKey', Any), ('symmetricSigningKey', Any), ('unwrapInfo', Any)])):
    def __dafnystr__(self) -> str:
        return f'EdkWrapping.UnwrapEdkMaterialOutput.UnwrapEdkMaterialOutput({_dafny.string_of(self.plaintextDataKey)}, {_dafny.string_of(self.symmetricSigningKey)}, {_dafny.string_of(self.unwrapInfo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput) and self.plaintextDataKey == __o.plaintextDataKey and self.symmetricSigningKey == __o.symmetricSigningKey and self.unwrapInfo == __o.unwrapInfo
    def __hash__(self) -> int:
        return super().__hash__()
