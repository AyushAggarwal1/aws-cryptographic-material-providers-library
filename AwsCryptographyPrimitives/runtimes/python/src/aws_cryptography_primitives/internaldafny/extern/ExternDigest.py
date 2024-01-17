from cryptography.hazmat.primitives import hashes
import Wrappers
import _dafny
import software_amazon_cryptography_primitives_internaldafny_types
import aws_cryptography_primitives.internaldafny.generated.Digest
from aws_cryptography_primitives.internaldafny.generated.Digest import *

class default__:

  @staticmethod
  def get_hash(digest_algorithm):
    if digest_algorithm.is_SHA__256:
      return hashes.Hash(hashes.SHA256())
    elif digest_algorithm.is_SHA__384:
      return hashes.Hash(hashes.SHA384())
    elif digest_algorithm.is_SHA__512:
      return hashes.Hash(hashes.SHA512())
    else:
      raise ValueError(f"Unsupported digest algorithm: {digest_algorithm}")

  @staticmethod
  def internal_digest(digest_algorithm, message):
    try:
      hash = default__.get_hash(digest_algorithm)
      message_bytes = bytes(message)
      hash.update(message_bytes)
      digest = hash.finalize()
      return Wrappers.Result_Success(digest)
    except ValueError as e:
      error = software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(
          message="Requested digest Algorithm is not supported."
      )
      return Wrappers.Result_Failure(error=error)


  @staticmethod
  def Digest(digest_algorithm, message):
    maybe_digest = default__.internal_digest(digest_algorithm, message)
    if maybe_digest.is_Failure:
      return maybe_digest.PropagateFailure()
    else:
      return Wrappers.Result_Success(_dafny.Seq(maybe_digest.value))

aws_cryptography_primitives.internaldafny.generated.Digest.default__ = default__