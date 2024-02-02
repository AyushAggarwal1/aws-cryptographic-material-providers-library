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
import JSON_Utils_Views_Core
import JSON_Utils_Views_Writers
import JSON_Utils_Views
import JSON_Utils_Lexers_Core
import JSON_Utils_Lexers_Strings
import JSON_Utils_Lexers
import JSON_Utils_Cursors
import JSON_Utils_Parsers
import JSON_Utils_Str_CharStrConversion
import JSON_Utils_Str_CharStrEscaping
import JSON_Utils_Str
import JSON_Utils_Seq
import JSON_Utils_Vectors
import JSON_Utils
import JSON_Errors
import JSON_Values
import JSON_Spec
import JSON_Grammar
import JSON_Serializer_ByteStrConversion
import JSON_Serializer
import JSON_Deserializer_Uint16StrConversion
import JSON_Deserializer_ByteStrConversion
import JSON_Deserializer
import JSON_ConcreteSyntax_Spec
import JSON_ConcreteSyntax_SpecProperties
import JSON_ConcreteSyntax

# Module: JSON_ZeroCopy_Serializer

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Serialize(js):
        rbs: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.pointer)()
        d_590_writer_: JSON_Utils_Views_Writers.Writer__
        d_590_writer_ = default__.Text(js)
        d_591_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_591_valueOrError0_ = Wrappers.default__.Need((d_590_writer_).Unsaturated_q, JSON_Errors.SerializationError_OutOfMemory())
        if (d_591_valueOrError0_).IsFailure():
            rbs = (d_591_valueOrError0_).PropagateFailure()
            return rbs
        d_592_bs_: _dafny.Array
        out24_: _dafny.Array
        out24_ = (d_590_writer_).ToArray()
        d_592_bs_ = out24_
        rbs = Wrappers.Result_Success(d_592_bs_)
        return rbs
        return rbs

    @staticmethod
    def SerializeTo(js, dest):
        len: Wrappers.Result = Wrappers.Result.default(BoundedInts.uint32.default)()
        d_593_writer_: JSON_Utils_Views_Writers.Writer__
        d_593_writer_ = default__.Text(js)
        d_594_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_594_valueOrError0_ = Wrappers.default__.Need((d_593_writer_).Unsaturated_q, JSON_Errors.SerializationError_OutOfMemory())
        if (d_594_valueOrError0_).IsFailure():
            len = (d_594_valueOrError0_).PropagateFailure()
            return len
        d_595_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_595_valueOrError1_ = Wrappers.default__.Need(((d_593_writer_).length) <= ((dest).length(0)), JSON_Errors.SerializationError_OutOfMemory())
        if (d_595_valueOrError1_).IsFailure():
            len = (d_595_valueOrError1_).PropagateFailure()
            return len
        (d_593_writer_).CopyTo(dest)
        len = Wrappers.Result_Success((d_593_writer_).length)
        return len
        return len

    @staticmethod
    def Text(js):
        return default__.JSON(js, JSON_Utils_Views_Writers.Writer__.Empty)

    @staticmethod
    def JSON(js, writer):
        def lambda47_(d_596_js_):
            def lambda48_(d_597_wr_):
                return default__.Value((d_596_js_).t, d_597_wr_)

            return lambda48_

        return (((writer).Append((js).before)).Then(lambda47_(js))).Append((js).after)

    @staticmethod
    def Value(v, writer):
        source19_ = v
        if source19_.is_Null:
            d_598___mcc_h0_ = source19_.n
            d_599_n_ = d_598___mcc_h0_
            return (writer).Append(d_599_n_)
        elif source19_.is_Bool:
            d_600___mcc_h1_ = source19_.b
            d_601_b_ = d_600___mcc_h1_
            d_602_wr_ = (writer).Append(d_601_b_)
            return d_602_wr_
        elif source19_.is_String:
            d_603___mcc_h2_ = source19_.str
            d_604_str_ = d_603___mcc_h2_
            d_605_wr_ = default__.String(d_604_str_, writer)
            return d_605_wr_
        elif source19_.is_Number:
            d_606___mcc_h3_ = source19_.num
            d_607_num_ = d_606___mcc_h3_
            d_608_wr_ = default__.Number(d_607_num_, writer)
            return d_608_wr_
        elif source19_.is_Object:
            d_609___mcc_h4_ = source19_.obj
            d_610_obj_ = d_609___mcc_h4_
            d_611_wr_ = default__.Object(d_610_obj_, writer)
            return d_611_wr_
        elif True:
            d_612___mcc_h5_ = source19_.arr
            d_613_arr_ = d_612___mcc_h5_
            d_614_wr_ = default__.Array(d_613_arr_, writer)
            return d_614_wr_

    @staticmethod
    def String(str, writer):
        return (((writer).Append((str).lq)).Append((str).contents)).Append((str).rq)

    @staticmethod
    def Number(num, writer):
        d_615_wr_ = ((writer).Append((num).minus)).Append((num).num)
        d_616_wr_ = (((d_615_wr_).Append((((num).frac).t).period)).Append((((num).frac).t).num) if ((num).frac).is_NonEmpty else d_615_wr_)
        d_617_wr_ = ((((d_616_wr_).Append((((num).exp).t).e)).Append((((num).exp).t).sign)).Append((((num).exp).t).num) if ((num).exp).is_NonEmpty else d_616_wr_)
        return d_617_wr_

    @staticmethod
    def StructuralView(st, writer):
        return (((writer).Append((st).before)).Append((st).t)).Append((st).after)

    @staticmethod
    def Object(obj, writer):
        d_618_wr_ = default__.StructuralView((obj).l, writer)
        d_619_wr_ = default__.Members(obj, d_618_wr_)
        d_620_wr_ = default__.StructuralView((obj).r, d_619_wr_)
        return d_620_wr_

    @staticmethod
    def Array(arr, writer):
        d_621_wr_ = default__.StructuralView((arr).l, writer)
        d_622_wr_ = default__.Items(arr, d_621_wr_)
        d_623_wr_ = default__.StructuralView((arr).r, d_622_wr_)
        return d_623_wr_

    @staticmethod
    def Members(obj, writer):
        wr: JSON_Utils_Views_Writers.Writer__ = JSON_Utils_Views_Writers.Writer.default()
        out25_: JSON_Utils_Views_Writers.Writer__
        out25_ = default__.MembersImpl(obj, writer)
        wr = out25_
        return wr

    @staticmethod
    def Items(arr, writer):
        wr: JSON_Utils_Views_Writers.Writer__ = JSON_Utils_Views_Writers.Writer.default()
        out26_: JSON_Utils_Views_Writers.Writer__
        out26_ = default__.ItemsImpl(arr, writer)
        wr = out26_
        return wr

    @staticmethod
    def MembersImpl(obj, writer):
        wr: JSON_Utils_Views_Writers.Writer__ = JSON_Utils_Views_Writers.Writer.default()
        wr = writer
        d_624_members_: _dafny.Seq
        d_624_members_ = (obj).data
        hi9_ = len(d_624_members_)
        for d_625_i_ in range(0, hi9_):
            wr = default__.Member((d_624_members_)[d_625_i_], wr)
        return wr

    @staticmethod
    def ItemsImpl(arr, writer):
        wr: JSON_Utils_Views_Writers.Writer__ = JSON_Utils_Views_Writers.Writer.default()
        wr = writer
        d_626_items_: _dafny.Seq
        d_626_items_ = (arr).data
        hi10_ = len(d_626_items_)
        for d_627_i_ in range(0, hi10_):
            wr = default__.Item((d_626_items_)[d_627_i_], wr)
        return wr

    @staticmethod
    def Member(m, writer):
        d_628_wr_ = default__.String(((m).t).k, writer)
        d_629_wr_ = default__.StructuralView(((m).t).colon, d_628_wr_)
        d_630_wr_ = default__.Value(((m).t).v, d_629_wr_)
        d_631_wr_ = (d_630_wr_ if ((m).suffix).is_Empty else default__.StructuralView(((m).suffix).t, d_630_wr_))
        return d_631_wr_

    @staticmethod
    def Item(m, writer):
        d_632_wr_ = default__.Value((m).t, writer)
        d_633_wr_ = (d_632_wr_ if ((m).suffix).is_Empty else default__.StructuralView(((m).suffix).t, d_632_wr_))
        return d_633_wr_
