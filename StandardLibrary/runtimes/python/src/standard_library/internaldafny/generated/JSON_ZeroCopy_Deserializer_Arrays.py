import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import standard_library.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
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
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.UTF8 as UTF8
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
import standard_library.internaldafny.generated.JSON_Utils_Views_Core as JSON_Utils_Views_Core
import standard_library.internaldafny.generated.JSON_Utils_Views_Writers as JSON_Utils_Views_Writers
import standard_library.internaldafny.generated.JSON_Utils_Views as JSON_Utils_Views
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import standard_library.internaldafny.generated.JSON_Utils_Lexers as JSON_Utils_Lexers
import standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq
import standard_library.internaldafny.generated.JSON_Utils_Vectors as JSON_Utils_Vectors
import standard_library.internaldafny.generated.JSON_Utils as JSON_Utils
import standard_library.internaldafny.generated.JSON_Errors as JSON_Errors
import standard_library.internaldafny.generated.JSON_Values as JSON_Values
import standard_library.internaldafny.generated.JSON_Spec as JSON_Spec
import standard_library.internaldafny.generated.JSON_Grammar as JSON_Grammar
import standard_library.internaldafny.generated.JSON_Serializer_ByteStrConversion as JSON_Serializer_ByteStrConversion
import standard_library.internaldafny.generated.JSON_Serializer as JSON_Serializer
import standard_library.internaldafny.generated.JSON_Deserializer_Uint16StrConversion as JSON_Deserializer_Uint16StrConversion
import standard_library.internaldafny.generated.JSON_Deserializer_ByteStrConversion as JSON_Deserializer_ByteStrConversion
import standard_library.internaldafny.generated.JSON_Deserializer as JSON_Deserializer
import standard_library.internaldafny.generated.JSON_ConcreteSyntax_Spec as JSON_ConcreteSyntax_Spec
import standard_library.internaldafny.generated.JSON_ConcreteSyntax_SpecProperties as JSON_ConcreteSyntax_SpecProperties
import standard_library.internaldafny.generated.JSON_ConcreteSyntax as JSON_ConcreteSyntax
import standard_library.internaldafny.generated.JSON_ZeroCopy_Serializer as JSON_ZeroCopy_Serializer
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Core as JSON_ZeroCopy_Deserializer_Core
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Strings as JSON_ZeroCopy_Deserializer_Strings
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Numbers as JSON_ZeroCopy_Deserializer_Numbers
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ObjectParams as JSON_ZeroCopy_Deserializer_ObjectParams
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Objects as JSON_ZeroCopy_Deserializer_Objects
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ArrayParams as JSON_ZeroCopy_Deserializer_ArrayParams

# Module: standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Arrays

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Array(cs, json):
        d_845_valueOrError0_ = default__.Bracketed(cs, json)
        if (d_845_valueOrError0_).IsFailure():
            return (d_845_valueOrError0_).PropagateFailure()
        elif True:
            d_846_sp_ = (d_845_valueOrError0_).Extract()
            return Wrappers.Result_Success(d_846_sp_)

    @staticmethod
    def Open(cs):
        d_847_valueOrError0_ = (cs).AssertByte(JSON_ZeroCopy_Deserializer_ArrayParams.default__.OPEN)
        if (d_847_valueOrError0_).IsFailure():
            return (d_847_valueOrError0_).PropagateFailure()
        elif True:
            d_848_cs_ = (d_847_valueOrError0_).Extract()
            return Wrappers.Result_Success((d_848_cs_).Split())

    @staticmethod
    def Close(cs):
        d_849_valueOrError0_ = (cs).AssertByte(JSON_ZeroCopy_Deserializer_ArrayParams.default__.CLOSE)
        if (d_849_valueOrError0_).IsFailure():
            return (d_849_valueOrError0_).PropagateFailure()
        elif True:
            d_850_cs_ = (d_849_valueOrError0_).Extract()
            return Wrappers.Result_Success((d_850_cs_).Split())

    @staticmethod
    def BracketedFromParts(open, elems, close):
        d_851_sp_ = JSON_Utils_Cursors.Split_SP(JSON_Grammar.Bracketed_Bracketed((open).t, (elems).t, (close).t), (close).cs)
        return d_851_sp_

    @staticmethod
    def AppendWithSuffix(elems, elem, sep):
        d_852_suffixed_ = JSON_Grammar.Suffixed_Suffixed((elem).t, JSON_Grammar.Maybe_NonEmpty((sep).t))
        d_853_elems_k_ = JSON_Utils_Cursors.Split_SP(((elems).t) + (_dafny.Seq([d_852_suffixed_])), (sep).cs)
        return d_853_elems_k_

    @staticmethod
    def AppendLast(elems, elem, sep):
        d_854_suffixed_ = JSON_Grammar.Suffixed_Suffixed((elem).t, JSON_Grammar.Maybe_Empty())
        d_855_elems_k_ = JSON_Utils_Cursors.Split_SP(((elems).t) + (_dafny.Seq([d_854_suffixed_])), (elem).cs)
        return d_855_elems_k_

    @staticmethod
    def Elements(json, open, elems):
        while True:
            with _dafny.label():
                d_856_valueOrError0_ = JSON_ZeroCopy_Deserializer_ArrayParams.default__.Element((elems).cs, json)
                if (d_856_valueOrError0_).IsFailure():
                    return (d_856_valueOrError0_).PropagateFailure()
                elif True:
                    d_857_elem_ = (d_856_valueOrError0_).Extract()
                    if ((d_857_elem_).cs).EOF_q:
                        return Wrappers.Result_Failure(JSON_Utils_Cursors.CursorError_EOF())
                    elif True:
                        d_858_sep_ = JSON_ZeroCopy_Deserializer_Core.default__.TryStructural((d_857_elem_).cs)
                        d_859_s0_ = (((d_858_sep_).t).t).Peek()
                        if ((d_859_s0_) == (default__.SEPARATOR)) and (((((d_858_sep_).t).t).Length()) == (1)):
                            d_860_sep_ = d_858_sep_
                            d_861_elems_ = default__.AppendWithSuffix(elems, d_857_elem_, d_860_sep_)
                            in229_ = json
                            in230_ = open
                            in231_ = d_861_elems_
                            json = in229_
                            open = in230_
                            elems = in231_
                            raise _dafny.TailCall()
                        elif ((d_859_s0_) == (JSON_ZeroCopy_Deserializer_ArrayParams.default__.CLOSE)) and (((((d_858_sep_).t).t).Length()) == (1)):
                            d_862_sep_ = d_858_sep_
                            d_863_elems_k_ = default__.AppendLast(elems, d_857_elem_, d_862_sep_)
                            d_864_bracketed_ = default__.BracketedFromParts(open, d_863_elems_k_, d_862_sep_)
                            return Wrappers.Result_Success(d_864_bracketed_)
                        elif True:
                            d_865_separator_ = default__.SEPARATOR
                            d_866_pr_ = Wrappers.Result_Failure(JSON_Utils_Cursors.CursorError_ExpectingAnyByte(_dafny.Seq([JSON_ZeroCopy_Deserializer_ArrayParams.default__.CLOSE, d_865_separator_]), d_859_s0_))
                            return d_866_pr_
                break

    @staticmethod
    def Bracketed(cs, json):
        d_867_valueOrError0_ = JSON_ZeroCopy_Deserializer_Core.default__.Structural(cs, JSON_Utils_Parsers.Parser___Parser(default__.Open))
        if (d_867_valueOrError0_).IsFailure():
            return (d_867_valueOrError0_).PropagateFailure()
        elif True:
            d_868_open_ = (d_867_valueOrError0_).Extract()
            d_869_elems_ = JSON_Utils_Cursors.Split_SP(_dafny.Seq([]), (d_868_open_).cs)
            if (((d_868_open_).cs).Peek()) == (JSON_ZeroCopy_Deserializer_ArrayParams.default__.CLOSE):
                d_870_p_ = JSON_Utils_Parsers.Parser___Parser(default__.Close)
                d_871_valueOrError1_ = JSON_ZeroCopy_Deserializer_Core.default__.Structural((d_868_open_).cs, d_870_p_)
                if (d_871_valueOrError1_).IsFailure():
                    return (d_871_valueOrError1_).PropagateFailure()
                elif True:
                    d_872_close_ = (d_871_valueOrError1_).Extract()
                    return Wrappers.Result_Success(default__.BracketedFromParts(d_868_open_, d_869_elems_, d_872_close_))
            elif True:
                return default__.Elements(json, d_868_open_, d_869_elems_)

    @_dafny.classproperty
    def SpecViewOpen(instance):
        return JSON_ZeroCopy_Deserializer_Core.default__.SpecView
    @_dafny.classproperty
    def SpecViewClose(instance):
        return JSON_ZeroCopy_Deserializer_Core.default__.SpecView
    @_dafny.classproperty
    def SEPARATOR(instance):
        return ord(',')

class jopen:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_Utils_Views_Core.View__.OfBytes(_dafny.Seq([JSON_ZeroCopy_Deserializer_ArrayParams.default__.OPEN]))

class jclose:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_Utils_Views_Core.View__.OfBytes(_dafny.Seq([JSON_ZeroCopy_Deserializer_ArrayParams.default__.CLOSE]))