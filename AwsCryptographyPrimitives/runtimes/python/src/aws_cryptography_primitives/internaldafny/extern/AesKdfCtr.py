from cryptography.hazmat.primitives.ciphers import algorithms, modes
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.exceptions import AlreadyFinalized
from software_amazon_cryptography_primitives_internaldafny_types import Error_AwsCryptographicPrimitivesError
import Wrappers
import _dafny

class default__:

  @staticmethod
  def AesKdfCtrStream(nonce, key, length):
    cipher = Cipher(
        algorithms.AES(bytes(key)), modes.CTR(bytes(nonce)),
    )
    plaintext = bytearray(length)
    encryptor = cipher.encryptor()
    try:
      ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    except ValueError:
      return Wrappers.Result_Failure(Error_AwsCryptographicPrimitivesError(
        message="Cannot finalize an encryptor when the plaintext data is not a multiple of the algorithm block size"
      ))
    except AlreadyFinalized:
      return Wrappers.Result_Failure(Error_AwsCryptographicPrimitivesError(
        message="Cannot update or finalize an encryptor which was already finalized"
      ))
    return Wrappers.Result_Success(_dafny.Seq(ciphertext))