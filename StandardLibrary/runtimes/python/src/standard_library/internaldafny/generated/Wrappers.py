import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_

# Module: Wrappers

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Need(condition, error):
        if condition:
            return Outcome_Pass()
        elif True:
            return Outcome_Fail(error)


class Option:
    @classmethod
    def default(cls, ):
        return lambda: Option_None()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_None(self) -> bool:
        return isinstance(self, Option_None)
    @property
    def is_Some(self) -> bool:
        return isinstance(self, Option_Some)
    def ToResult(self):
        source0_ = self
        if source0_.is_None:
            return Result_Failure(_dafny.Seq("Option is None"))
        elif True:
            d_0___mcc_h0_ = source0_.value
            d_1_v_ = d_0___mcc_h0_
            return Result_Success(d_1_v_)

    def ToResult_k(self, error):
        source1_ = self
        if source1_.is_None:
            return Result_Failure(error)
        elif True:
            d_2___mcc_h0_ = source1_.value
            d_3_v_ = d_2___mcc_h0_
            return Result_Success(d_3_v_)

    def UnwrapOr(self, default):
        source2_ = self
        if source2_.is_None:
            return default
        elif True:
            d_4___mcc_h0_ = source2_.value
            d_5_v_ = d_4___mcc_h0_
            return d_5_v_

    def IsFailure(self):
        return (self).is_None

    def PropagateFailure(self):
        return Option_None()

    def Extract(self):
        return (self).value


class Option_None(Option, NamedTuple('None_', [])):
    def __dafnystr__(self) -> str:
        return f'Wrappers.Option.None'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Option_None)
    def __hash__(self) -> int:
        return super().__hash__()

class Option_Some(Option, NamedTuple('Some', [('value', Any)])):
    def __dafnystr__(self) -> str:
        return f'Wrappers.Option.Some({_dafny.string_of(self.value)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Option_Some) and self.value == __o.value
    def __hash__(self) -> int:
        return super().__hash__()


class Result:
    @classmethod
    def default(cls, default_T):
        return lambda: Result_Success(default_T())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Success(self) -> bool:
        return isinstance(self, Result_Success)
    @property
    def is_Failure(self) -> bool:
        return isinstance(self, Result_Failure)
    def ToOption(self):
        source3_ = self
        if source3_.is_Success:
            d_6___mcc_h0_ = source3_.value
            d_7_s_ = d_6___mcc_h0_
            return Option_Some(d_7_s_)
        elif True:
            d_8___mcc_h1_ = source3_.error
            d_9_e_ = d_8___mcc_h1_
            return Option_None()

    def UnwrapOr(self, default):
        source4_ = self
        if source4_.is_Success:
            d_10___mcc_h0_ = source4_.value
            d_11_s_ = d_10___mcc_h0_
            return d_11_s_
        elif True:
            d_12___mcc_h1_ = source4_.error
            d_13_e_ = d_12___mcc_h1_
            return default

    def IsFailure(self):
        return (self).is_Failure

    def PropagateFailure(self):
        return Result_Failure((self).error)

    def MapFailure(self, reWrap):
        source5_ = self
        if source5_.is_Success:
            d_14___mcc_h0_ = source5_.value
            d_15_s_ = d_14___mcc_h0_
            return Result_Success(d_15_s_)
        elif True:
            d_16___mcc_h1_ = source5_.error
            d_17_e_ = d_16___mcc_h1_
            return Result_Failure(reWrap(d_17_e_))

    def Extract(self):
        return (self).value


class Result_Success(Result, NamedTuple('Success', [('value', Any)])):
    def __dafnystr__(self) -> str:
        return f'Wrappers.Result.Success({_dafny.string_of(self.value)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Result_Success) and self.value == __o.value
    def __hash__(self) -> int:
        return super().__hash__()

class Result_Failure(Result, NamedTuple('Failure', [('error', Any)])):
    def __dafnystr__(self) -> str:
        return f'Wrappers.Result.Failure({_dafny.string_of(self.error)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Result_Failure) and self.error == __o.error
    def __hash__(self) -> int:
        return super().__hash__()


class Outcome:
    @classmethod
    def default(cls, ):
        return lambda: Outcome_Pass()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Pass(self) -> bool:
        return isinstance(self, Outcome_Pass)
    @property
    def is_Fail(self) -> bool:
        return isinstance(self, Outcome_Fail)
    def IsFailure(self):
        return (self).is_Fail

    def PropagateFailure(self):
        return Result_Failure((self).error)


class Outcome_Pass(Outcome, NamedTuple('Pass', [])):
    def __dafnystr__(self) -> str:
        return f'Wrappers.Outcome.Pass'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Outcome_Pass)
    def __hash__(self) -> int:
        return super().__hash__()

class Outcome_Fail(Outcome, NamedTuple('Fail', [('error', Any)])):
    def __dafnystr__(self) -> str:
        return f'Wrappers.Outcome.Fail({_dafny.string_of(self.error)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Outcome_Fail) and self.error == __o.error
    def __hash__(self) -> int:
        return super().__hash__()
