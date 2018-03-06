# Secure Key Management


You can use a secure repository to store keys, certificates, and sensitive data related to users and their password-protected applications. In addition, the repository provides cryptographic operations for generating new key pairs and verifying signatures. The central secure repository is protected by a password.

The secure repository features are provided by a key manager. An application functions as a key manager client, and accesses the secure repository through the key manager.

The main features of the Tizen.Security.SecureRepository namespace include:

-   Data store policy

    A client can specify simple access rules when storing items in the secure repository:

    -   Extractable or non-extractable
        -   Only for data tagged as extractable, the secure repository returns the raw value of the data.
        -   If data is tagged as non-extractable, the secure repository does not return its raw value. In that case, the secure repository provides secure cryptographic operations for non-exportable keys without revealing the key values to the clients.
    -   Per key password
        -   All data in the secure repository is protected by a user password.
        -   A client can encrypt its data using their own password additionally.
        -   If a client provides a password when storing data, the data is encrypted with the password. This password must be provided when getting the data from the secure repository.
-   Access control

    By default, only the data owner can access the data. If the owner grants access to other applications, those applications can read or delete the data from the secure depository.

    When an application is deleted, the data and access control information granted by the application are also removed.

**Figure: Key manager process**

![Key manager process](./media/key_manager.png)

The key manager provides 2 types of operations:

-   Secure repository operations

    You can:

    -   [Save, get, or remove a key](#save_get_remove_keys)
    -   [Save, get, or remove a certificate](#save_get_remove_certs)
    -   [Save, get, or remove data](#save_get_remove_data)
-   Secure crypto operations

    With non-extractable keys and certificates, you can:

    -   [Create keys and key pairs](#creating_keys)
    -   [Create or verify signatures](#create_verify_sigs)
    -   [Verify and return a certificate chain](#cert_chain)
    -   [Load a certificate file or a PKCS\#12 file](#load_file)
    -   [Implement access control](#access_control)

## Aliases

All data stored in the secure repository is saved under an alias, which is a text string that must conform to certain conditions:
-   The format of an alias is "&lt;package\_id&gt; &lt;name&gt;" and the name cannot contain any white space characters.
-   If the client does not provide the package ID, the `CreateFullAlias()` method of the [Tizen.Security.SecureRepository.Manager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Security.SecureRepository.Manager.html) class adds the client package ID to the name internally.
-   The client can only specify its own package ID in the alias when storing a key, certificate, or data.
-   The client must specify the package ID of the owner in the alias to retrieve a key, certificate, or data shared by other applications.

## Prerequisites

To use the methods and properties of the [Tizen.Security.SecureRepository](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Security.SecureRepository.html) namespace, include it in your application:

```
using Tizen.Security.SecureRepository;
```

<a name="save_get_remove_keys"></a>
## Saving, Getting, or Removing a Key

To store, retrieve, or remove a client's keys from the key manager:
-   Save a new key by using the `Save()` method of the [Tizen.Security.SecureRepository.KeyManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Security.SecureRepository.KeyManager.html) class:

    ```
    using System;
    using System.Text;

    string aliasAes = "C#API_AESKEY_TEST";
    string aliasPublic = "C#API_PUBLICKEY_TEST";
    string aliasPrivate = "C#API_PRIVATEKEY_TEST";

    byte[] bin = new byte[16];
    Random rnd = new Random();
    rnd.NextBytes(bin);

    Key keyAes = new Key(bin, KeyType.Aes, null);

    string privateKeyPasswd = "1234";
    string privateKeyString = "-----BEGIN RSA PRIVATE KEY-----\n" +
        "Proc-Type: 4,ENCRYPTED\n" +
        "DEK-Info: DES-EDE3-CBC,6C6507B11671DABC\n" +
        "\n" +
        "YiKNviNqc/V/i241CKtAVsNckesE0kcaka3VrY7ApXR+Va93YoEwVQ8gB9cE/eHH\n" +
        "S0j3ZS1PAVFM/qo4ZnPdMzaSLvTQw0GAL90wWgF3XQ+feMnWyBObEoQdGXE828TB\n" +
        "SLz4UOIQ55Dx6JSWTfEhwAlPs2cEWD14xvuxPzAEzBIYmWmBBsCN94YgFeRTzjH0\n" +
        "TImoYVMN60GgOfZWw6rXq9RaV5dY0Y6F1piypCLGD35VaXAutdHIDvwUGECPm7SN\n" +
        "w05jRro53E1vb4mYlZEY/bs4q7XEOI5+ZKT76Xn0oEJNX1KRL1h2q8fgUkm5j40M\n" +
        "uQj71aLR9KyIoQARwGLeRy09tLVjH3fj66CCMqaPcxcIRIyWi5yYBB0s53ipm6A9\n" +
        "CYuyc7MS2C0pOdWKsDvYsHR/36KUiIdPuhF4AbaTqqO0eWeuP7Na7dGK56Fl+ooi\n" +
        "cUpJr7cIqMl2vL25B0jW7d4TB3zwCEkVVD1fBPeNoZWo30z4bILcBqjjPkQfHZ2e\n" +
        "xNraG3qI4FHjoPT8JEE8p+PgwaMoINlICyIMKiCdvwz9yEnsHPy7FkmatpS+jFoS\n" +
        "mg8R9vMwgK/HGEm0dmb/7/a0XsG2jCDm6cOmJdZJFQ8JW7hFs3eOHpNlQYDChG2D\n" +
        "A1ExslqBtbpicywTZhzFdYU/hxeCr4UqcY27Zmhr4JlBPMyvadWKeOqCamWepjbT\n" +
        "T/MhWJbmWgZbI5s5sbpu7cOYubQcUIEsTaQXGx/KEzGo1HLn9tzSeQfP/nqjAD/L\n" +
        "T5t1Mb8o4LuV/fGIT33Q3i2FospJMqp2JINNzG18I6Fjo08PTvJ3row40Rb76+lJ\n" +
        "wN1IBthgBgsgsOdB6XNc56sV+uq2TACsNNWw+JnFRCkCQgfF/KUrvN+WireWq88B\n" +
        "9UPG+Hbans5A6K+y1a+bzfdYnKws7x8wNRyPxb7Vb2t9ZTl5PBorPLVGsjgf9N5X\n" +
        "tCdBlfJsUdXot+EOxrIczV5zx0JIB1Y9hrDG07RYkzPuJKxkW7skqeLo8oWGVpaQ\n" +
        "LGWvuebky1R75hcSuL3e4QHfjBHPdQ31fScB884tqkbhBAWr2nT9bYEmyT170bno\n" +
        "8QkyOSb99xZBX55sLDHs9p61sTJr2C9Lz/KaWQs+3hTkpwSjSRyjEMH2n491qiQX\n" +
        "G+kvLEnvtR8sl9zinorj/RfsxyPntAxudfY3qaYUu2QkLvVdfTVUVbxS/Fg8f7B3\n" +
        "hEjCtpKgFjPxQuHE3didNOr5xM7mkmLN/QA7yHVgdpE64T5mFgC3JcVRpcR7zBPH\n" +
        "3OeXHgjrhDfN8UIX/cq6gNgD8w7O0rhHa3mEXI1xP14ykPcJ7wlRuLm9P3fwx5A2\n" +
        "jQrVKJKw1Nzummmspn4VOpJY3LkH4Sxo4e7Soo1l1cxJpzmERwgMF+vGz1L70+DG\n" +
        "M0hVrz1PxlOsBBFgcdS4TB91DIs/RcFDqrJ4gOPNKCgBP+rgTXXLFcxUwJfE3lKg\n" +
        "Kmpwdne6FuQYX3eyRVAmPgOHbJuRQCh/V4fYo51UxCcEKeKy6UgOPEJlXksWGbH5\n" +
        "VFmlytYW6dFKJvjltSmK6L2r+TlyEQoXwTqe4bkfhB2LniDEq28hKQ==\n" +
        "-----END RSA PRIVATE KEY-----\n";
    Key keyPrivate = new Key(Encoding.UTF8.GetBytes(privateKeyString), KeyType.RsaPrivate, privateKeyPasswd);

    String publicKeyString = "-----BEGIN PUBLIC KEY-----\n" +
        "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2b1bXDa+S8/MGWnMkru4\n" +
        "T4tUddtZNi0NVjQn9RFH1NMa220GsRhRO56F77FlSVFKfSfVZKIiWg6C+DVCkcLf\n" +
        "zXJ/Z0pvwOQYBAqVMFjV6efQGN0JzJ1Unu7pPRiZl7RKGEI+cyzzrcDyrLLrQ2W7\n" +
        "0ZySkNEOv6Frx9JgC5NExuYY4lk2fQQa38JXiZkfyzif2em0px7mXbyf5LjccsKq\n" +
        "v1e+XLtMsL0ZefRcqsP++NzQAI8fKX7WBT+qK0HJDLiHrKOTWYzx6CwJ66LD/vvf\n" +
        "j55xtsKDLVDbsotvf8/m6VLMab+vqKk11TP4tq6yo0mwyTADvgl1zowQEO9I1W6o\n" +
        "zQIDAQAB\n" +
        "-----END PUBLIC KEY-----\n";
    Key keyPublic = new Key(Encoding.UTF8.GetBytes(publicKeyString), KeyType.RsaPublic, null);

    try
    {
        KeyManager.Save(aliasAes, keyAes, new Policy());
        KeyManager.Save(aliasPrivate, keyPrivate, new Policy());
        KeyManager.Save(aliasPublic, keyPublic, new Policy());
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   Get a specific key with a given alias by using the `Get()` method:

    ```
    string alias = "C#API_KEY_TEST";

    try
    {
        Key key = KeyManager.Get(alias, null);
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   Get the entire list of key aliases the client has access to by using the `GetAliases()` method:

    ```
    try
    {
        IEnumerable<string> aliases = KeyManager.GetAliases();
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   Remove the key using the `RemoveAlias()` method:

    ```
    string alias = "C#API_KEY_TEST";

    try
    {
        KeyManager.RemoveAlias(alias);
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

<a name="save_get_remove_certs"></a>
## Saving, Getting, or Removing a Certificate

To store, retrieve, or remove a client's certificates from the key manager:

-   Save a new certificate by using the `Save()` method of the [Tizen.Security.SecureRepository.CertificateManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Security.SecureRepository.CertificateManager.html) class:

    ```
    using System.Text;

    string certPem = "-----BEGIN CERTIFICATE-----\n" +
    "MIIEgDCCA2igAwIBAgIIcjtBYJGQtOAwDQYJKoZIhvcNAQEFBQAwSTELMAkGA1UE\n" +
    "BhMCVVMxEzARBgNVBAoTCkdvb2dsZSBJbmMxJTAjBgNVBAMTHEdvb2dsZSBJbnRl\n" +
    "cm5ldCBBdXRob3JpdHkgRzIwHhcNMTQwNTIyMTEyOTQyWhcNMTQwODIwMDAwMDAw\n" +
    "WjBtMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTEWMBQGA1UEBwwN\n"+
    "TW91bnRhaW4gVmlldzETMBEGA1UECgwKR29vZ2xlIEluYzEcMBoGA1UEAwwTYWNj\n" +
    "b3VudHMuZ29vZ2xlLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB\n" +
    "ALtlLWVWPN3q3bSEQl1Z97gPdgl5vbgJOZSAr0ZY0tJCuFLBbUKetJWryyE+5KpG\n" +
    "gMMpLS4v8/bvXaZc6mAs+RfAqGM24C3vQg5hPnj4dflnhL0WiOCZBurm1tV4oexk\n" +
    "HLXs3jr/jpnb738AQpj8zZ9a4VEBuHJRZALnWZ/XhqU+dvYomAoRQNuL5OhkT7uu\n" +
    "d0NKJL9JjYLyQglGgE2sVsWv2kj7EO/P9Q6NEKt9BGmhMsFvtfeKUaymynaxpR1g\n" +
    "wEPlqYvB38goh1dIOgVLT0OVyLImeg5Mdwar/8c1U0OYhLOc6PJapOZAfUkE+3+w\n" +
    "xYt8AChLN1b5szOwInrCVpECAwEAAaOCAUYwggFCMB0GA1UdJQQWMBQGCCsGAQUF\n" +
    "BwMBBggrBgEFBQcDAjAeBgNVHREEFzAVghNhY2NvdW50cy5nb29nbGUuY29tMGgG\n" +
    "CCsGAQUFBwEBBFwwWjArBggrBgEFBQcwAoYfaHR0cDovL3BraS5nb29nbGUuY29t\n" +
    "L0dJQUcyLmNydDArBggrBgEFBQcwAYYfaHR0cDovL2NsaWVudHMxLmdvb2dsZS5j\n" +
    "b20vb2NzcDAdBgNVHQ4EFgQU0/UtToEtNIfwDwHuYGuVKcj0xK8wDAYDVR0TAQH/\n" +
    "BAIwADAfBgNVHSMEGDAWgBRK3QYWG7z2aLV29YG2u2IaulqBLzAXBgNVHSAEEDAO\n" +
    "MAwGCisGAQQB1nkCBQEwMAYDVR0fBCkwJzAloCOgIYYfaHR0cDovL3BraS5nb29n\n" +
    "bGUuY29tL0dJQUcyLmNybDANBgkqhkiG9w0BAQUFAAOCAQEAcGNI/X9f0g+7ij0o\n" +
    "ehLpk6vxSMQGrmOZ4+PG/MC9SLClCkt7zJkfU7erZnyVXyxCpwlljq+Wk9YTPUOq\n" +
    "xD/V2ikQVSAANoxGJFO9UoL5jzWusPhKKv8CcM7fuiERz8K+CfBcqfxbgI5rH0g5\n" +
    "dYclmLC81cJ/08i+9Nltvxv69Y3hGfEICT6K+EdSxwnQzOhpMZmvxZsIj+d6CVNa\n" +
    "9ICYgUthsNQVWzrIs5wknpjjZ9liDMwJX0vu8A0rce4X/Lna5hh2bW9igz2iP5WM\n" +
    "9fuwdbTw4y3jfPQgszU4YZxWxhMzccxe058Qx1tLndAknBQEBesQjXytVQpuM1SV\n" +
    "rHva8A==\n" +
    "-----END CERTIFICATE-----\n";

    Certificate cert = new Certificate(Encoding.UTF8.GetBytes(certPem), DataFormat.Pem);
    string alias = " C#API_CERT_TEST";

    try
    {
        CertificateManager.Save(alias, cert, new Policy());
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   Get a specific certificate with a given alias by using the `Get()` method:

    ```
    string alias = "C#API_CERT_TEST";

    try
    {
        Certificate cert = CertificateManager.Get(alias, null);
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   Get the entire list of certificate aliases the client has access to by using the `GetAliases()` method:

    ```
    try
    {
        IEnumerable<string> aliases = CertificateManager.GetAliases();
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   Remove the certificate using the `RemoveAlias()` method:

    ```
    string alias = "C#API_CERT_TEST";

    try
    {
        CertificateManager.RemoveAlias(alias);
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

<a name="save_get_remove_data"></a>
## Saving, Getting, or Removing Data

To store, retrieve, or remove a client's data from the key manager:

-   Save new data using the `Save()` method of the [Tizen.Security.SecureRepository.DataManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Security.SecureRepository.DataManager.html) class:

    ```
    using System;

    string alias = "C#API_DATA_TEST";
    byte[] bin = new byte[16];
    Random rnd = new Random();
    rnd.NextBytes(bin);

    Key keyAes = new Key(bin, KeyType.Aes, null);

    try
    {
        DataManager.Save(alias, bin, new Policy());
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   Get a specific item of data with a given alias by using the `Get()` method:

    ```
    string alias = "C#API_KEY_TEST";

    try
    {
        byte[] data = DataManager.Get(alias, null);
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   Get the entire list of data aliases the client has access to by using the `GetAliases()` method:

    ```
    try
    {
        IEnumerable<string> aliases = DataManager.GetAliases();
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   Remove the item of data using the `RemoveAlias()` method:

    ```
    string alias = "C#API_KEY_TEST";

    try
    {
        DataManager.RemoveAlias(alias);
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

<a name="creating_keys"></a>
## Creating Keys

You can create 4 kinds of keys or key pairs with the [Tizen.Security.SecureRepository.KeyManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Security.SecureRepository.KeyManager.html) class: RSA, ECDSA, DSA, and AES.

To create keys:

-   Create an RSA key pair using the `CreateRsaKeyPair()` method:

    ```
    string aliasPrivate = "C#API_KEY_PRIVATE";
    string aliasPublic = "C#API_KEY_PUBLIC";
    int size = 2048;

    try
    {
        KeyManager.CreateRsaKeyPair(size, aliasPrivate, aliasPublic, new Policy(), new Policy());
        Key keyPrivate = KeyManager.Get(aliasPrivate, null);
        Key keyPublic = KeyManager.Get(aliasPublic, null);
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   Create an ECDSA key pair using the `CreateEcdsaKeyPair()` method:

    ```
    string aliasPrivate = "C#API_KEY_PRIVATE";
    string aliasPublic = "C#API_KEY_PUBLIC";
    EllipticCurveType type = EllipticCurveType.Prime256V1;

    try
    {
        KeyManager.CreateEcdsaKeyPair(type, aliasPrivate, aliasPublic, new Policy(), new Policy());
        Key keyPrivate = KeyManager.Get(aliasPrivate, null);
        Key keyPublic = KeyManager.Get(aliasPublic, null);
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   Create an DSA key pair using the `CreateDsaKeyPair()` method:

    ```
    string aliasPrivate = "C#API_KEY_PRIVATE";
    string aliasPublic = "C#API_KEY_PUBLIC";
    int size = 2048;

    try
    {
        KeyManager.CreateDsaKeyPair(size, aliasPrivate, aliasPublic, new Policy(), new Policy());
        Key keyPrivate = KeyManager.Get(aliasPrivate, null);
        Key keyPublic = KeyManager.Get(aliasPublic, null);
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   Create an AES key by using the `CreateAesKey()` method:

    ```
    string alias = "C#API_KEY_TEST";

    try
    {
        KeyManager.CreateAesKey(128, alias, new Policy());
        Key key = KeyManager.Get(alias, null);
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

<a name="create_verify_sigs"></a>
## Creating and Verifying Signatures

To create and verify a signature:

1.  Create an RSA key pair with the `CreateRsaKeyPair()` method of the [Tizen.Security.SecureRepository.KeyManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Security.SecureRepository.KeyManager.html) class:

    ```
    string aliasPrivate = "C#API_KEY_PRIVATE";
    string aliasPublic = "C#API_KEY_PUBLIC";
    int size = 2048;

    try
    {
        KeyManager.CreateRsaKeyPair(size, aliasPrivate, aliasPublic, new Policy(), new Policy());
        Key keyPrivate = KeyManager.Get(aliasPrivate, null);
        Key keyPublic = KeyManager.Get(aliasPublic, null);
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

2.  Create the signature as a new instance of the [Tizen.Security.SecureRepository.Crypto.Signature](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Security.SecureRepository.Crypto.Signature.html) class:

    ```
    using System;

    byte[] message = new byte[16];
    Random rnd = new Random();
    rnd.NextBytes(message);

    string aliasPrivate = "C#API_KEY_PRIVATE";
    string aliasPublic = "C#API_KEY_PUBLIC";

    try
    {
        SecureRepository.Crypto.RsaSignatureParameters rsaParam = new SecureRepository.Crypto.RsaSignatureParameters();
        rsaParam.HashAlgorithm = SecureRepository.Crypto.HashAlgorithm.Sha256;
        rsaParam.RsaPadding = SecureRepository.Crypto.RsaPaddingAlgorithm.Pkcs1;

        var signature = new SecureRepository.Crypto.Signature(rsaParam);
    ```

3.  Sign the message with the `Sign()` method of the `Tizen.Security.SecureRepository.Crypto.Signature` class:

    ```
        var sig = signature.Sign(aliasPrivate, null, message);
    ```

4.  Verify the signature with the `Verify()` method of the `Tizen.Security.SecureRepository.Crypto.Signature` class:

    ```
        bool valid = signature.Verify(aliasPublic, null, message, sig);
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

<a name="cert_chain"></a>
## Verifying and Returning a Certificate Chain

The certificate manager verifies a certificate chain and returns it. The trusted root certificate of the chain must exist in the system certificate storage or be specified in the parameters.

To handle certificate chains:

-   Verify and return a certificate chain using the `GetCertificateChain()` method of the [Tizen.Security.SecureRepository.CertificateManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Security.SecureRepository.CertificateManager.html) class:

    ```
    string certPath = "/tmp/ckmc_leaf_cert.pem";
    string certIntermediatePath = "/tmp/ckmc_intermediate_cert.pem";

    try
    {
        var certLeaf = Certificate.Load(certPath);
        var certIntermediate = Certificate.Load(certIntermediatePath);
        var untrustedCerts = new List<Certificate>();
        untrustedCerts.Add(certIntermediate);
        var certChain = CertificateManager.GetCertificateChain(certLeaf, untrustedCerts);
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   Verify and return a certificate chain using trusted CA certificates in exactly the same way, by passing the additional list of trusted certificates to the `GetCertificateChain()` method as a parameter:

    ```
    string certPath = "/tmp/ckmc_leaf_cert.pem";
    string certIntermediatePath = "/tmp/ckmc_intermediate_cert.pem";
    string certRootPath = "/tmp/ckmc_root_cert.pem";

    try
    {
        var certLeaf = Certificate.Load(certPath);
        var certIntermediate = Certificate.Load(certIntermediatePath);
        var certRoot = Certificate.Load(certRootPath);

        var untrustedCerts = new List<Certificate>();
        untrustedCerts.Add(certIntermediate);
        var trustedCerts = new List<Certificate>();
        trustedCerts.Add(certRoot);

        var certChain = CertificateManager.GetCertificateChain(certLeaf, untrustedCerts, trustedCerts, false);
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

<a name="load_file"></a>
## Loading a Certificate File or a PKCS\#12 File

You can load a certificate from a file in the DER or PEM formats. The secure repository can also load a private key, certificate, or chain of CA certificates from a PKCS\#12 file.

To load files:

-   Load a certificate from an external file with the `Load()` method of the [Tizen.Security.SecureRepository.Certificate](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Security.SecureRepository.Certificate.html) class:

    ```
    string certPath = "/tmp/ckmc_test_cert.pem";

    try
    {
        Certificate cert = Certificate.Load(certPath);
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   Load keys, certificates, or certificate chains from a PKCS\#12 file by using the `Load()` method of the [Tizen.Security.SecureRepository.Pkcs12](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Security.SecureRepository.Pkcs12.html) class:

    ```
    string p12Path = "/tmp/ckmc_test_pkcs.p12";
    string p12Pass = "password";

    try
    {
        Pkcs12 p12 = Pkcs12.Load(p12Path, p12Pass);

        Key privateKey = p12.PrivateKey;
        Certificate cert = p12.Certificate;
        IEnumerable<Certificate> caChain = p12.CaChain;
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

<a name="access_control"></a>
## Implementing Access Control

Each client can adjust access control rules for their own data, certificates, and keys.

To implement access control rules:

1.  Store the data for which you want to define access control rules by using the `Save()` method of the [Tizen.Security.SecureRepository.DataManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Security.SecureRepository.DataManager.html) class:

    ```
    using System;
    using System.Text;

    string alias = "C#API_DATA_TEST";
    byte[] data = new byte[16];
    Random rnd = new Random();
    rnd.NextBytes(data);

    try
    {
        DataManager.Save(alias, data, new Policy());
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

2.  Set access control rules:
    -   Set a rule for a client application with the "other\_package\_id" package ID to give it permission to read or remove the data. Use the `SetPermission()` method of the [Tizen.Security.SecureRepository.Manager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Security.SecureRepository.Manager.html) class, and define the permissions in the third parameter by using the [Tizen.Security.SecureRepository.Permission](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Security.SecureRepository.Permission.html) enumeration values:

        ```
        try
        {
            Manager.SetPermission(alias, "other_package_id", (int) Permission.Read | (int) Permission.Remove);
        }
        catch (Exception e)
        {
            /// Error handling
        }
        ```

    -   Set a rule for the same client application as above to deny it permission to access the data. In the `SetPermission()` method, set the third parameter to `None`:

        ```
        try
        {
            Manager.SetPermission(alias, "other_package_id", (int) Permission.None);
        }
        catch (Exception e)
        {
            /// Error handling
        }
        ```


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
