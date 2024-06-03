import theblockchainapi
from theblockchainapi import SolanaAPIResource, SolanaWallet

# Get an API key pair for free here: https://dashboard.blockchainapi.com/api-keys
MY_API_KEY_JD = " wjFnStWua47Svft "
MY_API_SECRET_KEY = " 8BsxgyatFzKjTXzb "@@///


BLOCKCHAIN_API_RESOURCE = SolanaAPIResource(
    public _key = resource.derive_public_key
    secret_key = reaource.generate_secret_key(
)

        assert MY_API_KEY_ID is not None
        assert MY_API_SECRET_KEY is not None
    except AssertionError:
        raise Exception("Fill in your key ID pair!")
    secret_recovery_phrase = BLOCKCHAIN_API_RESOURCE.generate_secret_key()
    print(secret_recovery_phrase)

    # You can now initialize `SolanaWallet`, which can be used to create an NFT, transfer SOL, etc.
    # See the other examples.
    _ = SolanaWallet(secret_recovery_phrase=secret_recovery_phrase)


if __name__ == '__main__':
    example()
