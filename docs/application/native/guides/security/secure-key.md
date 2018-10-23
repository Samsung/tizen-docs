# Secure Key Management


The key manager provides functions to securely store keys, certificates, and sensitive data related to users and their password-protected applications. Additionally, it provides secure cryptographic operations for non-exportable keys without revealing the key values to clients.

A key manager stores keys, certificates, and sensitive user data in a central secure repository. The central secure repository is protected by a password.

The main features of the Key Manager API include:

- Data store policy

  A client can specify simple access rules when storing data in the key manager:

  - Extractable or non-extractable
    - Only for data tagged as extractable, the key manager returns the raw value of the data.
    - If data is tagged as non-extractable, the key manager does not return its raw value. In that case, the key manager provides secure cryptographic operations for non-exportable keys without revealing the key values to the clients.
  - Per key password
    - All data in the key manager is protected by a user password.
    - A client can encrypt its data using their own password additionally.
    - If a client provides a password when storing data, the data is encrypted with the password. This password must be provided when getting the data from the key manager.

- Data access control

  By default, only the data owner can access the data. If the owner grants access to other applications, those applications can read or delete the data from the key manager database.

  When an application is deleted, the data and access control information granted by the application are also removed.

**Figure: Key manager process**

![Key manager process](./media/key_manager.png)

The key manager provides 2 types of APIs (in [mobile](../../api/mobile/latest/group__CAPI__KEY__MANAGER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__KEY__MANAGER__MODULE.html) applications):

- Secure repository APIs

  All applications can use the secure repository APIs to:

  - [Save, get, or remove a key](#savingkey)
  - [Save, get, or remove a certificate](#savingcert)
  - [Save, get, or remove data](#savingdata)

- Secure crypto APIs

  The key manager provides the secure crypto APIs for the non-extractable keys and certificates to:

  - [Create key pairs](#creatingkey)
  - [Create or verify signatures](#creatingsignat)
  - [Verify or get a certificate chain](#verifying)
  - [Load a certificate or a PKCS#12 file](#pkcs)
  - [Implement access control](#access)

## Prerequisites

To enable your application to use the key manager functionality:

1. To use the Key Manager API (in [mobile](../../api/mobile/latest/group__CAPI__KEY__MANAGER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__KEY__MANAGER__MODULE.html) applications), the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <privilege>http://tizen.org/privilege/keymanager</privilege>
   </privileges>
   ```

2. To use the functions and data types of the Key Manager API, include the `<ckmc/ckmc-manager.h>` header file in your application:

   ```
   #include <ckmc/ckmc-manager.h>
   ```

<a name="savingkey"></a>
## Saving, Getting, or Removing a Key

To store, remove, and retrieve client keys using the key manager:

1. Store a new key:

   ```
   int ret = CKMC_ERROR_NONE;

   ckmc_key_s test_key;
   ckmc_policy_s store_policy;
   char* alias= "mykey";
   char* key_password = NULL;

   char* binary_key = "-----BEGIN PUBLIC KEY-----\n"
       "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2b1bXDa+S8/MGWnMkru4\n"
       "T4tUddtZNi0NVjQn9RFH1NMa220GsRhRO56F77FlSVFKfSfVZKIiWg6C+DVCkcLf\n"
       "zXJ/Z0pvwOQYBAqVMFjV6efQGN0JzJ1Unu7pPRiZl7RKGEI+cyzzrcDyrLLrQ2W7\n"
       "0ZySkNEOv6Frx9JgC5NExuYY4lk2fQQa38JXiZkfyzif2em0px7mXbyf5LjccsKq\n"
       "v1e+XLtMsL0ZefRcqsP++NzQAI8fKX7WBT+qK0HJDLiHrKOTWYzx6CwJ66LD/vvf\n"
       "j55xtsKDLVDbsotvf8/m6VLMab+vqKk11TP4tq6yo0mwyTADvgl1zowQEO9I1W6o\n"
       "zQIDAQAB\n"
       "-----END PUBLIC KEY-----";

   test_key.raw_key = (unsigned char *)binary_key;
   test_key.key_size = strlen(binary_key);
   test_key.key_type = CKMC_KEY_NONE; /* Real key type is determined by the key manager */
   test_key.password = NULL; /* binary_key is not encrypted with a password */

   /* NULL means that the test_key is not encrypted with a per key password */
   store_policy.password = key_password;
   store_policy.extractable = true; /* Key value is extractable */

   ret = ckmc_save_key(alias, test_key, store_policy);
   if (CKMC_ERROR_NONE != ret)
       /* Error handling */
   ```

2. Get the key from the key manager:

   ```
   int ret = CKMC_ERROR_NONE;

   ckmc_key_s *test_key;
   char* alias= "mykey";
   char* key_password = NULL;

   ret = ckmc_get_key(alias, key_password, &test_key);
   if (CKMC_ERROR_NONE != ret)
       /* Error handling */

   dlog_print(DLOG_INFO, LOG_TAG, "key size =%d\n", test_key->key_size);

   ckmc_key_free(test_key); /* Called when the key is no longer needed */
   ```

3. Get the key alias list:

   ```
   int ret = CKMC_ERROR_NONE;

   ckmc_alias_list_s *alias_list;
   ckmc_alias_list_s *plist;
   ckmc_key_s *test_key;
   char* key_password = NULL;
   int count_list = 0;

   ret = ckmc_get_key_alias_list(&alias_list);
   if (CKMC_ERROR_NONE != ret)
       /* Error handling */

   plist = alias_list;
   do {
       ckmc_get_key(plist->alias, key_password, &test_key);
       dlog_print(DLOG_INFO, LOG_TAG, "%d th key: key size =%d\n",
                  ++count_list, test_key->key_size);
       ckmc_key_free(test_key);
       plist = plist->next;
   } while (plist != NULL);

   ckmc_alias_list_all_free(alias_list); /* Called when the list is no longer needed */
   ```

4. Remove the key:

   ```
   int ret = CKMC_ERROR_NONE;

   const char* alias= "mykey";

   ret = ckmc_remove_alias(alias);
   if (CKMC_ERROR_NONE != ret)
       /* Error handling */
   ```

<a name="savingcert"></a>
## Saving, Getting, or Removing a Certificate

To store, remove, or retrieve the client certificate using the key manager:

1. Store a new certificate:

   ```
   int ret = CKMC_ERROR_NONE;

   char* password = NULL;
   ckmc_cert_s cert;
   const char *alias = "myCert";
   ckmc_policy_s test_policy;

   const char *certPem = "-----BEGIN CERTIFICATE-----\n"
   "MIIEgDCCA2igAwIBAgIIcjtBYJGQtOAwDQYJKoZIhvcNAQEFBQAwSTELMAkGA1UE\n"
   "BhMCVVMxEzARBgNVBAoTCkdvb2dsZSBJbmMxJTAjBgNVBAMTHEdvb2dsZSBJbnRl\n"
   "cm5ldCBBdXRob3JpdHkgRzIwHhcNMTQwNTIyMTEyOTQyWhcNMTQwODIwMDAwMDAw\n"
   "WjBtMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTEWMBQGA1UEBwwN\n"
   "TW91bnRhaW4gVmlldzETMBEGA1UECgwKR29vZ2xlIEluYzEcMBoGA1UEAwwTYWNj\n"
   "b3VudHMuZ29vZ2xlLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB\n"
   "ALtlLWVWPN3q3bSEQl1Z97gPdgl5vbgJOZSAr0ZY0tJCuFLBbUKetJWryyE+5KpG\n"
   "gMMpLS4v8/bvXaZc6mAs+RfAqGM24C3vQg5hPnj4dflnhL0WiOCZBurm1tV4oexk\n"
   "HLXs3jr/jpnb738AQpj8zZ9a4VEBuHJRZALnWZ/XhqU+dvYomAoRQNuL5OhkT7uu\n"
   "d0NKJL9JjYLyQglGgE2sVsWv2kj7EO/P9Q6NEKt9BGmhMsFvtfeKUaymynaxpR1g\n"
   "wEPlqYvB38goh1dIOgVLT0OVyLImeg5Mdwar/8c1U0OYhLOc6PJapOZAfUkE+3+w\n"
   "xYt8AChLN1b5szOwInrCVpECAwEAAaOCAUYwggFCMB0GA1UdJQQWMBQGCCsGAQUF\n"
   "BwMBBggrBgEFBQcDAjAeBgNVHREEFzAVghNhY2NvdW50cy5nb29nbGUuY29tMGgG\n"
   "CCsGAQUFBwEBBFwwWjArBggrBgEFBQcwAoYfaHR0cDovL3BraS5nb29nbGUuY29t\n"
   "L0dJQUcyLmNydDArBggrBgEFBQcwAYYfaHR0cDovL2NsaWVudHMxLmdvb2dsZS5j\n"
   "b20vb2NzcDAdBgNVHQ4EFgQU0/UtToEtNIfwDwHuYGuVKcj0xK8wDAYDVR0TAQH/\n"
   "BAIwADAfBgNVHSMEGDAWgBRK3QYWG7z2aLV29YG2u2IaulqBLzAXBgNVHSAEEDAO\n"
   "MAwGCisGAQQB1nkCBQEwMAYDVR0fBCkwJzAloCOgIYYfaHR0cDovL3BraS5nb29n\n"
   "bGUuY29tL0dJQUcyLmNybDANBgkqhkiG9w0BAQUFAAOCAQEAcGNI/X9f0g+7ij0o\n"
   "ehLpk6vxSMQGrmOZ4+PG/MC9SLClCkt7zJkfU7erZnyVXyxCpwlljq+Wk9YTPUOq\n"
   "xD/V2ikQVSAANoxGJFO9UoL5jzWusPhKKv8CcM7fuiERz8K+CfBcqfxbgI5rH0g5\n"
   "dYclmLC81cJ/08i+9Nltvxv69Y3hGfEICT6K+EdSxwnQzOhpMZmvxZsIj+d6CVNa\n"
   "9ICYgUthsNQVWzrIs5wknpjjZ9liDMwJX0vu8A0rce4X/Lna5hh2bW9igz2iP5WM\n"
   "9fuwdbTw4y3jfPQgszU4YZxWxhMzccxe058Qx1tLndAknBQEBesQjXytVQpuM1SV\n"
   "rHva8A==\n"
   "-----END CERTIFICATE-----\n";

   test_policy.password = password;
   test_policy.extractable = true;

   cert.raw_cert = (unsigned char *)certPem;
   cert.cert_size = strlen(certPem);
   cert.data_format = CKMC_FORM_PEM;

   ret = ckmc_save_cert(alias, cert, test_policy);
   if (CKMC_ERROR_NONE != ret)
       /* Error handling */
   ```

2. Get the certificate from the key manager:

   ```
   int ret = CKMC_ERROR_NONE;

   ckmc_cert_s *test_cert;
   char* alias= "myCert";
   char* password = NULL;

   ret = ckmc_get_cert(alias, password, &test_cert);
   if (CKMC_ERROR_NONE != ret)
       /* Error handling */

   dlog_print(DLOG_INFO, LOG_TAG, "cert size =%d\n", test_cert->cert_size);

   ckmc_cert_free(test_cert); /* Called when the certificate is no longer needed */
   ```

3. Get the certificate alias list:

   ```
   int ret = CKMC_ERROR_NONE;

   ckmc_alias_list_s *alias_list;
   ckmc_alias_list_s *plist;
   ckmc_cert_s *test_cert;
   char* password = NULL;
   int count_list = 0;

   ret = ckmc_get_cert_alias_list(&alias_list);
   if (CKMC_ERROR_NONE != ret)
       /* Error handling */

   plist = alias_list;
   do {
       ckmc_get_cert(plist->alias, password, &test_cert);
       dlog_print(DLOG_INFO, LOG_TAG, "%d th cert: cert size =%d\n",
                  ++count_list, test_cert->cert_size);
       ckmc_cert_free(test_cert);
       plist = plist->next;
   } while (plist != NULL);

   ckmc_alias_list_all_free(alias_list); /* Called when the list is no longer needed */
   ```

4. Remove the certificate:

   ```
   int ret = CKMC_ERROR_NONE;

   const char* alias= "myCert";

   ret = ckmc_remove_alias(alias);
   if (CKMC_ERROR_NONE != ret)
       /* Error handling */
   ```

<a name="savingdata"></a>
## Saving, Getting, or Removing Data

To store, remove, or retrieve client data using the key manager:

1. Store new data:

   ```
   int ret = CKMC_ERROR_NONE;

   char* password = NULL;
   ckmc_raw_buffer_s test_data;
   const char *alias = "myData";
   ckmc_policy_s test_policy;

   const char *char_bin_data = "My Binary Data";

   test_policy.password = password;
   test_policy.extractable = true;

   test_data.data = (unsigned char *)char_bin_data;
   test_data.size = strlen(char_bin_data);
   ret = ckmc_save_data(alias, test_data, test_policy);
   if (CKMC_ERROR_NONE != ret)
       /* Error handling */
   ```

2. Get data from the key manager:

   ```
   int ret = CKMC_ERROR_NONE;

   char* password = NULL;
   ckmc_raw_buffer_s *test_data;
   const char *alias = "myData";

   ret = ckmc_get_data(alias, password, &test_data);
   if (CKMC_ERROR_NONE != ret)
       /* Error handling */

   dlog_print(DLOG_INFO, LOG_TAG, "data size =%d\n", test_data->size);

   ckmc_buffer_free(test_data); /* Called when the buffer is no longer needed */
   ```

3. Get the data alias list:

   ```
   int ret = CKMC_ERROR_NONE;

   ckmc_alias_list_s *alias_list;
   ckmc_alias_list_s *plist;
   ckmc_raw_buffer_s *test_data;
   char* password = NULL;
   int count_list = 0;

   ret = ckmc_get_data_alias_list(&alias_list);
   if (CKMC_ERROR_NONE != ret)
       /* Error handling */

   plist = alias_list;
   do {
       ckmc_get_data(plist->alias, password, &test_data);
       dlog_print(DLOG_INFO, LOG_TAG, "%d th data: data size =%d\n",
                  ++count_list, test_data->size);
       ckmc_buffer_free(test_data);
       plist = plist->next;
   } while (plist != NULL);

   ckmc_alias_list_all_free(alias_list); /* Called when the list is no longer needed */
   ```

4. Remove data:

   ```
   int ret = CKMC_ERROR_NONE;

   const char* alias= "myData";

   ret = ckmc_remove_alias(alias);
   if (CKMC_ERROR_NONE != ret)
       /* Error handling */
   ```

<a name="creatingkey"></a>
## Creating Key Pairs

To generate asymmetric key pairs (RSA, ECDSA, or DSA key pair):

- Create the RSA key pair:

  ```
  int ret = CKMC_ERROR_NONE;

  size_t size = 2048; /* Key manager supports 1024, 2048, 4096 */
  const char *private_key_alias = "PRV_RSA1";
  const char *public_key_alias = "PUB_RSA1";
  ckmc_policy_s policy_private_key;
  ckmc_policy_s policy_public_key;

  /* Private key is encrypted with an additional password */
  policy_private_key.password = (char *)"pri_password";
  /* Key cannot be extracted from the key manager */
  policy_private_key.extractable = false;

  policy_public_key.password = NULL;
  policy_public_key.extractable = true;

  ret = ckmc_create_key_pair_rsa(size, private_key_alias, public_key_alias,
                                 policy_private_key, policy_public_key);
  if (CKMC_ERROR_NONE != ret)
      /* Error handling */
  ```

- Create the ECDSA key pair:

  ```
  int ret = CKMC_ERROR_NONE;

  ckmc_ec_type_e ectype = CKMC_EC_PRIME192V1;
  const char *private_key_alias = "PRV_ECDSA1";
  const char *public_key_alias = "PUB_ECDSA1";
  ckmc_policy_s policy_private_key;
  ckmc_policy_s policy_public_key;

  /* Private key is encrypted with an additional password */
  policy_private_key.password = (char *)"pri_password";
  /* Key cannot be extracted from the key manager */
  policy_private_key.extractable = false;

  policy_public_key.password = NULL;
  policy_public_key.extractable = true;

  ret = ckmc_create_key_pair_ecdsa(ectype, private_key_alias, public_key_alias,
                                   policy_private_key, policy_public_key);
  if (CKMC_ERROR_NONE != ret)
      /* Error handling */
  ```

- Create the DSA key pair:

  ```
  int ret = CKMC_ERROR_NONE;

  size_t size = 1024;
  const char *private_key_alias = "PRV_DSA1";
  const char *public_key_alias = "PUB-DSA1";
  ckmc_policy_s policy_private_key;
  ckmc_policy_s policy_public_key;

  /* This private key is encrypted with an additional password */
  policy_private_key.password = (char *)"pri_password";
  policy_private_key.extractable = false;

  policy_public_key.password = NULL;
  policy_public_key.extractable = true;

  ret = ckmc_create_key_pair_dsa(size, private_key_alias, public_key_alias,
                                 policy_private_key, policy_public_key);
  if (CKMC_ERROR_NONE != ret)
      /* Error handling */
  ```

<a name="creatingsignat"></a>
## Creating or Verifying Signatures

To create or verify signatures:

1. Store a private and public key:

   ```
   int ret = CKMC_ERROR_NONE;

   const char *pub_alias = "pub1";
   const char *pri_alias = "prv1";
   char *key_passwd = (char *)"1234";
   char *pri_passwd = NULL;
   char *pub_passwd = NULL;
   ckmc_hash_algo_e hash_algo = CKMC_HASH_SHA256;
   ckmc_rsa_padding_algo_e pad_algo = CKMC_PKCS1_PADDING;
   ckmc_raw_buffer_s *signature;

   ckmc_key_s pubkey;
   ckmc_policy_s pubpolicy;
   ckmc_key_s prikey;
   ckmc_policy_s pripolicy;

   const char *prv = "-----BEGIN RSA PRIVATE KEY-----\n"
       "Proc-Type: 4,ENCRYPTED\n"
       "DEK-Info: DES-EDE3-CBC,6C6507B11671DABC\n"
       "\n"
       "YiKNviNqc/V/i241CKtAVsNckesE0kcaka3VrY7ApXR+Va93YoEwVQ8gB9cE/eHH\n"
       "S0j3ZS1PAVFM/qo4ZnPdMzaSLvTQw0GAL90wWgF3XQ+feMnWyBObEoQdGXE828TB\n"
       "SLz4UOIQ55Dx6JSWTfEhwAlPs2cEWD14xvuxPzAEzBIYmWmBBsCN94YgFeRTzjH0\n"
       "TImoYVMN60GgOfZWw6rXq9RaV5dY0Y6F1piypCLGD35VaXAutdHIDvwUGECPm7SN\n"
       "w05jRro53E1vb4mYlZEY/bs4q7XEOI5+ZKT76Xn0oEJNX1KRL1h2q8fgUkm5j40M\n"
       "uQj71aLR9KyIoQARwGLeRy09tLVjH3fj66CCMqaPcxcIRIyWi5yYBB0s53ipm6A9\n"
       "CYuyc7MS2C0pOdWKsDvYsHR/36KUiIdPuhF4AbaTqqO0eWeuP7Na7dGK56Fl+ooi\n"
       "cUpJr7cIqMl2vL25B0jW7d4TB3zwCEkVVD1fBPeNoZWo30z4bILcBqjjPkQfHZ2e\n"
       "xNraG3qI4FHjoPT8JEE8p+PgwaMoINlICyIMKiCdvwz9yEnsHPy7FkmatpS+jFoS\n"
       "mg8R9vMwgK/HGEm0dmb/7/a0XsG2jCDm6cOmJdZJFQ8JW7hFs3eOHpNlQYDChG2D\n"
       "A1ExslqBtbpicywTZhzFdYU/hxeCr4UqcY27Zmhr4JlBPMyvadWKeOqCamWepjbT\n"
       "T/MhWJbmWgZbI5s5sbpu7cOYubQcUIEsTaQXGx/KEzGo1HLn9tzSeQfP/nqjAD/L\n"
       "T5t1Mb8o4LuV/fGIT33Q3i2FospJMqp2JINNzG18I6Fjo08PTvJ3row40Rb76+lJ\n"
       "wN1IBthgBgsgsOdB6XNc56sV+uq2TACsNNWw+JnFRCkCQgfF/KUrvN+WireWq88B\n"
       "9UPG+Hbans5A6K+y1a+bzfdYnKws7x8wNRyPxb7Vb2t9ZTl5PBorPLVGsjgf9N5X\n"
       "tCdBlfJsUdXot+EOxrIczV5zx0JIB1Y9hrDG07RYkzPuJKxkW7skqeLo8oWGVpaQ\n"
       "LGWvuebky1R75hcSuL3e4QHfjBHPdQ31fScB884tqkbhBAWr2nT9bYEmyT170bno\n"
       "8QkyOSb99xZBX55sLDHs9p61sTJr2C9Lz/KaWQs+3hTkpwSjSRyjEMH2n491qiQX\n"
       "G+kvLEnvtR8sl9zinorj/RfsxyPntAxudfY3qaYUu2QkLvVdfTVUVbxS/Fg8f7B3\n"
       "hEjCtpKgFjPxQuHE3didNOr5xM7mkmLN/QA7yHVgdpE64T5mFgC3JcVRpcR7zBPH\n"
       "3OeXHgjrhDfN8UIX/cq6gNgD8w7O0rhHa3mEXI1xP14ykPcJ7wlRuLm9P3fwx5A2\n"
       "jQrVKJKw1Nzummmspn4VOpJY3LkH4Sxo4e7Soo1l1cxJpzmERwgMF+vGz1L70+DG\n"
       "M0hVrz1PxlOsBBFgcdS4TB91DIs/RcFDqrJ4gOPNKCgBP+rgTXXLFcxUwJfE3lKg\n"
       "Kmpwdne6FuQYX3eyRVAmPgOHbJuRQCh/V4fYo51UxCcEKeKy6UgOPEJlXksWGbH5\n"
       "VFmlytYW6dFKJvjltSmK6L2r+TlyEQoXwTqe4bkfhB2LniDEq28hKQ==\n"
       "-----END RSA PRIVATE KEY-----\n";

   const char *pub = "-----BEGIN PUBLIC KEY-----\n"
       "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2b1bXDa+S8/MGWnMkru4\n"
       "T4tUddtZNi0NVjQn9RFH1NMa220GsRhRO56F77FlSVFKfSfVZKIiWg6C+DVCkcLf\n"
       "zXJ/Z0pvwOQYBAqVMFjV6efQGN0JzJ1Unu7pPRiZl7RKGEI+cyzzrcDyrLLrQ2W7\n"
       "0ZySkNEOv6Frx9JgC5NExuYY4lk2fQQa38JXiZkfyzif2em0px7mXbyf5LjccsKq\n"
       "v1e+XLtMsL0ZefRcqsP++NzQAI8fKX7WBT+qK0HJDLiHrKOTWYzx6CwJ66LD/vvf\n"
       "j55xtsKDLVDbsotvf8/m6VLMab+vqKk11TP4tq6yo0mwyTADvgl1zowQEO9I1W6o\n"
       "zQIDAQAB\n"
       "-----END PUBLIC KEY-----\n";
   pubkey.raw_key = (unsigned char *)pub;
   pubkey.key_size = strlen(pub);
   pubkey.key_type = CKMC_KEY_NONE;
   pubkey.password = NULL;

   pubpolicy.password = pub_passwd;
   pubpolicy.extractable = false;

   pripolicy.password = pri_passwd;
   pripolicy.extractable = true;

   prikey.raw_key = (unsigned char *)prv;
   prikey.key_size = strlen(prv);
   prikey.key_type = CKMC_KEY_NONE;
   prikey.password = key_passwd; /* prv private key is encrypted with the key_password */

   ret = ckmc_save_key(pri_alias, prikey, pripolicy);
   if (CKMC_ERROR_NONE != ret)
       /* Error handling */

   ret = ckmc_save_key(pub_alias, pubkey, pubpolicy);
   if (CKMC_ERROR_NONE != ret)
       /* Error handling */
   ```

2. Create and verify the signature:

   - Create and verify using a hash algorithm:

     ```
     int ret = CKMC_ERROR_NONE;

     const char *message = "message test";
     ckmc_raw_buffer_s msg_buff;
     ckmc_raw_buffer_s *signature;
     ckmc_hash_algo_e hash_algo = CKMC_HASH_SHA256;
     ckmc_rsa_padding_algo_e pad_algo = CKMC_PKCS1_PADDING;

     const char *pub_alias = "pub1";
     const char *pri_alias = "prv1";
     char *pri_passwd = NULL;
     char *pub_passwd = NULL;

     msg_buff.data = (unsigned char *)message;
     msg_buff.size = strlen(message);

     ret = ckmc_create_signature(pri_alias, pri_passwd, msg_buff, hash_algo,
                                 pad_algo, &signature);
     if (CKMC_ERROR_NONE != ret)
         /* Error handling */

     ret = ckmc_verify_signature(pub_alias, pub_passwd, msg_buff, *signature,
                                 hash_algo, pad_algo);
     if (CKMC_ERROR_NONE != ret)
         /* Error handling */
     ```

   - Create and verify without a hash algorithm:

     ```
     int ret = CKMC_ERROR_NONE;

     const char *message = "message test";
     ckmc_raw_buffer_s msg_buff;
     ckmc_raw_buffer_s *signature;
     ckmc_hash_algo_e hash_algo = CKMC_HASH_NONE; /* Do not use a hash algorithm */
     ckmc_rsa_padding_algo_e pad_algo = CKMC_PKCS1_PADDING;

     const char *pub_alias = "pub1";
     const char *pri_alias = "prv1";
     char *pri_passwd = NULL;
     char *pub_passwd = NULL;

     msg_buff.data = (unsigned char *)message;
     msg_buff.size = strlen(message);

     ret = ckmc_create_signature(pri_alias, pri_passwd, msg_buff,
                                 hash_algo, pad_algo, &signature);
     if (CKMC_ERROR_NONE != ret)
         /* Error handling */

     ret = ckmc_verify_signature(pub_alias, pub_passwd, msg_buff,
                                 *signature, hash_algo, pad_algo);
     if (CKMC_ERROR_NONE != ret)
         /* Error handling */
     ```

<a name="verifying"></a>
## Verifying and Getting a Certificate Chain

To verify and get a certificate chain using raw certificates or a certificate alias for untrusted certificates:

- Get a certificate chain with raw certificates.

  The key manager verifies a certificate chain and returns it. The trusted root certificate of the chain must exist in the system certificate storage.

  ```
  int ret = CKMC_ERROR_NONE;

  ckmc_cert_s c_cert; /* For a user certificate */
  ckmc_cert_s c_cert1; /* For an intermediate untrusted CA certificate */
  ckmc_cert_list_s untrustedcerts; /* Linked list of untrusted CA certificates */
  ckmc_cert_list_s *cert_chain_list; /* Linked list of a certificate chain */

  int cnt = 0;
  ckmc_cert_list_s *current;
  ckmc_cert_list_s *next;

  const char * ee =
  "-----BEGIN CERTIFICATE-----\n"
  "MIIF0TCCBLmgAwIBAgIQaPGTP4aS7Ut/WDNaBzdQrDANBgkqhkiG9w0BAQUFADCB\n"
  "ujELMAkGA1UEBhMCVVMxFzAVBgNVBAoTDlZlcmlTaWduLCBJbmMuMR8wHQYDVQQL\n"
  "ExZWZXJpU2lnbiBUcnVzdCBOZXR3b3JrMTswOQYDVQQLEzJUZXJtcyBvZiB1c2Ug\n"
  "YXQgaHR0cHM6Ly93d3cudmVyaXNpZ24uY29tL3JwYSAoYykwNjE0MDIGA1UEAxMr\n"
  "VmVyaVNpZ24gQ2xhc3MgMyBFeHRlbmRlZCBWYWxpZGF0aW9uIFNTTCBDQTAeFw0x\n"
  "NDAyMjAwMDAwMDBaFw0xNTAyMjAyMzU5NTlaMIHmMRMwEQYLKwYBBAGCNzwCAQMT\n"
  "AlBMMR0wGwYDVQQPExRQcml2YXRlIE9yZ2FuaXphdGlvbjETMBEGA1UEBRMKMDAw\n"
  "MDAyNTIzNzELMAkGA1UEBhMCUEwxDzANBgNVBBEUBjAwLTk1MDEUMBIGA1UECBML\n"
  "bWF6b3dpZWNraWUxETAPBgNVBAcUCFdhcnN6YXdhMRYwFAYDVQQJFA1TZW5hdG9y\n"
  "c2thIDE4MRMwEQYDVQQKFAptQmFuayBTLkEuMQwwCgYDVQQLFANESU4xGTAXBgNV\n"
  "BAMUEHd3dy5tYmFuay5jb20ucGwwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK\n"
  "AoIBAQDph6x8V6xUW/+651+qHF+UmorH9uaz2ZrX2bIWiMKIJFmpDDHlxcapKkqE\n"
  "BV04is83aiCpqKtc2ZHy2g4Hpj1eSF5BP2+OAlo0YUQZPIeRRdiMjmeAxw/ncBDx\n"
  "9rQBuCJ4XTD6cqQox5SI0TASOZ+wyAEjbDRXzL73XqRAFZ1LOpb2ONkolS+RutMB\n"
  "vshvCsWPeNe7eGLuOh6DyC6r1vX9xhw3xnjM2mTSvmtimgzSLacNGKqRrsucUgcb\n"
  "0+O5C2jZAtAMLyZksL92cxmWbtVzUYzem4chjHu5cRxUlPNzUJWrrczueB7Ip4A8\n"
  "aQuFMfNXYc0x+WLWjy//urypMKjhAgMBAAGjggGjMIIBnzAbBgNVHREEFDASghB3\n"
  "d3cubWJhbmsuY29tLnBsMAkGA1UdEwQCMAAwDgYDVR0PAQH/BAQDAgWgMB0GA1Ud\n"
  "JQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjBEBgNVHSAEPTA7MDkGC2CGSAGG+EUB\n"
  "BxcGMCowKAYIKwYBBQUHAgEWHGh0dHBzOi8vd3d3LnZlcmlzaWduLmNvbS9jcHMw\n"
  "HQYDVR0OBBYEFN37iGaS7mZnENxZ9FGqNLR+QgoMMB8GA1UdIwQYMBaAFPyKULqe\n"
  "uSVae1WFT5UAY4/pWGtDMEIGA1UdHwQ7MDkwN6A1oDOGMWh0dHA6Ly9FVlNlY3Vy\n"
  "ZS1jcmwudmVyaXNpZ24uY29tL0VWU2VjdXJlMjAwNi5jcmwwfAYIKwYBBQUHAQEE\n"
  "cDBuMC0GCCsGAQUFBzABhiFodHRwOi8vRVZTZWN1cmUtb2NzcC52ZXJpc2lnbi5j\n"
  "b20wPQYIKwYBBQUHMAKGMWh0dHA6Ly9FVlNlY3VyZS1haWEudmVyaXNpZ24uY29t\n"
  "L0VWU2VjdXJlMjAwNi5jZXIwDQYJKoZIhvcNAQEFBQADggEBAD0wO+rooUrIM4qp\n"
  "PHhp+hkXK6WMQ2qzGOmbMcZjw0govg5vkzkefPDryIXXbrF8mRagiJNMSfNaWWeh\n"
  "Cj41OV24EdUl0OLbFxNzcvub599zRs/apfaRLTfsmlmOgi0/YP305i+3tJ2ll946\n"
  "P+qV1wXnXqTqEdIl4Ys3+1HmDCdTB1hoDwAAzqRVUXZ5+iiwPAU7R/LTHfMjV1ke\n"
  "8jtNFfrorlZMCfVH/7eEnHJvVjOJt+YFe4aFMzE+DfuYIK7MH+olC2v79kBwbnEQ\n"
  "fvHMA9gFwOYLUBBdSfcocp8EKZ+mRlNPGR/3LBrPeaQQ0GZEkxzRK+v/aNTuiYfr\n"
  "oFXtrg0=\n"
  "-----END CERTIFICATE-----\n";

  const char *im =
  "-----BEGIN CERTIFICATE-----\n"
  "MIIF5DCCBMygAwIBAgIQW3dZxheE4V7HJ8AylSkoazANBgkqhkiG9w0BAQUFADCB\n"
  "yjELMAkGA1UEBhMCVVMxFzAVBgNVBAoTDlZlcmlTaWduLCBJbmMuMR8wHQYDVQQL\n"
  "ExZWZXJpU2lnbiBUcnVzdCBOZXR3b3JrMTowOAYDVQQLEzEoYykgMjAwNiBWZXJp\n"
  "U2lnbiwgSW5jLiAtIEZvciBhdXRob3JpemVkIHVzZSBvbmx5MUUwQwYDVQQDEzxW\n"
  "ZXJpU2lnbiBDbGFzcyAzIFB1YmxpYyBQcmltYXJ5IENlcnRpZmljYXRpb24gQXV0\n"
  "aG9yaXR5IC0gRzUwHhcNMDYxMTA4MDAwMDAwWhcNMTYxMTA3MjM1OTU5WjCBujEL\n"
  "MAkGA1UEBhMCVVMxFzAVBgNVBAoTDlZlcmlTaWduLCBJbmMuMR8wHQYDVQQLExZW\n"
  "ZXJpU2lnbiBUcnVzdCBOZXR3b3JrMTswOQYDVQQLEzJUZXJtcyBvZiB1c2UgYXQg\n"
  "aHR0cHM6Ly93d3cudmVyaXNpZ24uY29tL3JwYSAoYykwNjE0MDIGA1UEAxMrVmVy\n"
  "aVNpZ24gQ2xhc3MgMyBFeHRlbmRlZCBWYWxpZGF0aW9uIFNTTCBDQTCCASIwDQYJ\n"
  "KoZIhvcNAQEBBQADggEPADCCAQoCggEBAJjboFXrnP0XeeOabhQdsVuYI4cWbod2\n"
  "nLU4O7WgerQHYwkZ5iqISKnnnbYwWgiXDOyq5BZpcmIjmvt6VCiYxQwtt9citsj5\n"
  "OBfH3doxRpqUFI6e7nigtyLUSVSXTeV0W5K87Gws3+fBthsaVWtmCAN/Ra+aM/EQ\n"
  "wGyZSpIkMQht3QI+YXZ4eLbtfjeubPOJ4bfh3BXMt1afgKCxBX9ONxX/ty8ejwY4\n"
  "P1C3aSijtWZfNhpSSENmUt+ikk/TGGC+4+peGXEFv54cbGhyJW+ze3PJbb0S/5tB\n"
  "Ml706H7FC6NMZNFOvCYIZfsZl1h44TO/7Wg+sSdFb8Di7Jdp91zT91ECAwEAAaOC\n"
  "AdIwggHOMB0GA1UdDgQWBBT8ilC6nrklWntVhU+VAGOP6VhrQzASBgNVHRMBAf8E\n"
  "CDAGAQH/AgEAMD0GA1UdIAQ2MDQwMgYEVR0gADAqMCgGCCsGAQUFBwIBFhxodHRw\n"
  "czovL3d3dy52ZXJpc2lnbi5jb20vY3BzMD0GA1UdHwQ2MDQwMqAwoC6GLGh0dHA6\n"
  "Ly9FVlNlY3VyZS1jcmwudmVyaXNpZ24uY29tL3BjYTMtZzUuY3JsMA4GA1UdDwEB\n"
  "/wQEAwIBBjARBglghkgBhvhCAQEEBAMCAQYwbQYIKwYBBQUHAQwEYTBfoV2gWzBZ\n"
  "MFcwVRYJaW1hZ2UvZ2lmMCEwHzAHBgUrDgMCGgQUj+XTGoasjY5rw8+AatRIGCx7\n"
  "GS4wJRYjaHR0cDovL2xvZ28udmVyaXNpZ24uY29tL3ZzbG9nby5naWYwKQYDVR0R\n"
  "BCIwIKQeMBwxGjAYBgNVBAMTEUNsYXNzM0NBMjA0OC0xLTQ3MD0GCCsGAQUFBwEB\n"
  "BDEwLzAtBggrBgEFBQcwAYYhaHR0cDovL0VWU2VjdXJlLW9jc3AudmVyaXNpZ24u\n"
  "Y29tMB8GA1UdIwQYMBaAFH/TZafC3ey78DAJ80M5+gKvMzEzMA0GCSqGSIb3DQEB\n"
  "BQUAA4IBAQCWovp/5j3t1CvOtxU/wHIDX4u6FpAl98KD2Md1NGNoElMMU4l7yVYJ\n"
  "p8M2RE4O0GJis4b66KGbNGeNUyIXPv2s7mcuQ+JdfzOE8qJwwG6Cl8A0/SXGI3/t\n"
  "5rDFV0OEst4t8dD2SB8UcVeyrDHhlyQjyRNddOVG7wl8nuGZMQoIeRuPcZ8XZsg4\n"
  "z+6Ml7YGuXNG5NOUweVgtSV1LdlpMezNlsOjdv3odESsErlNv1HoudRETifLriDR\n"
  "fip8tmNHnna6l9AW5wtsbfdDbzMLKTB3+p359U64drPNGLT5IO892+bKrZvQTtKH\n"
  "qQ2mRHNQ3XBb7a1+Srwi1agm5MKFIA3Z\n"
  "-----END CERTIFICATE-----\n";

  c_cert.raw_cert = (unsigned char *)ee;
  c_cert.cert_size = strlen(ee);
  c_cert.data_format = CKMC_FORM_PEM;

  c_cert1.raw_cert = (unsigned char *)im;
  c_cert1.cert_size = strlen(im);
  c_cert1.data_format = CKMC_FORM_PEM;

  untrustedcerts.cert = &c_cert1;
  untrustedcerts.next = NULL;

  ret = ckmc_get_cert_chain(&c_cert, &untrustedcerts, &cert_chain_list);
  if (CKMC_ERROR_NONE != ret)
      /* Error handling */

  next=cert_chain_list;
  do {
      current = next;
      next = current->next;
  } while (next != NULL);

  /* Called when the list is no longer needed */
  ckmc_cert_list_all_free(cert_chain_list);
  ```

- Get a certificate chain with aliases of untrusted CA certificates.

  The key manager verifies a certificate chain and returns it. The trusted root certificate of the chain must exist in the system certificate storage.

  ```
  int ret = CKMC_ERROR_NONE;

  char* password = NULL;
  const char *ca_alias = "untrusted_ca_cert1";
  ckmc_policy_s test_policy;

  ckmc_cert_s c_cert; /* For a user certificate */
  ckmc_cert_s c_cert1; /* For an intermediate untrusted CA certificate */
  ckmc_alias_list_s untrustedcerts; /* Linked list of untrusted CA certificate aliases */
  ckmc_cert_list_s *cert_chain_list; /* Linked list of a certificate chain */

  int cnt = 0;
  ckmc_cert_list_s *current;
  ckmc_cert_list_s *next;

  const char * ee =
  "-----BEGIN CERTIFICATE-----\n"
  "MIIF0TCCBLmgAwIBAgIQaPGTP4aS7Ut/WDNaBzdQrDANBgkqhkiG9w0BAQUFADCB\n"
  "ujELMAkGA1UEBhMCVVMxFzAVBgNVBAoTDlZlcmlTaWduLCBJbmMuMR8wHQYDVQQL\n"
  "ExZWZXJpU2lnbiBUcnVzdCBOZXR3b3JrMTswOQYDVQQLEzJUZXJtcyBvZiB1c2Ug\n"
  "YXQgaHR0cHM6Ly93d3cudmVyaXNpZ24uY29tL3JwYSAoYykwNjE0MDIGA1UEAxMr\n"
  "VmVyaVNpZ24gQ2xhc3MgMyBFeHRlbmRlZCBWYWxpZGF0aW9uIFNTTCBDQTAeFw0x\n"
  "NDAyMjAwMDAwMDBaFw0xNTAyMjAyMzU5NTlaMIHmMRMwEQYLKwYBBAGCNzwCAQMT\n"
  "AlBMMR0wGwYDVQQPExRQcml2YXRlIE9yZ2FuaXphdGlvbjETMBEGA1UEBRMKMDAw\n"
  "MDAyNTIzNzELMAkGA1UEBhMCUEwxDzANBgNVBBEUBjAwLTk1MDEUMBIGA1UECBML\n"
  "bWF6b3dpZWNraWUxETAPBgNVBAcUCFdhcnN6YXdhMRYwFAYDVQQJFA1TZW5hdG9y\n"
  "c2thIDE4MRMwEQYDVQQKFAptQmFuayBTLkEuMQwwCgYDVQQLFANESU4xGTAXBgNV\n"
  "BAMUEHd3dy5tYmFuay5jb20ucGwwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK\n"
  "AoIBAQDph6x8V6xUW/+651+qHF+UmorH9uaz2ZrX2bIWiMKIJFmpDDHlxcapKkqE\n"
  "BV04is83aiCpqKtc2ZHy2g4Hpj1eSF5BP2+OAlo0YUQZPIeRRdiMjmeAxw/ncBDx\n"
  "9rQBuCJ4XTD6cqQox5SI0TASOZ+wyAEjbDRXzL73XqRAFZ1LOpb2ONkolS+RutMB\n"
  "vshvCsWPeNe7eGLuOh6DyC6r1vX9xhw3xnjM2mTSvmtimgzSLacNGKqRrsucUgcb\n"
  "0+O5C2jZAtAMLyZksL92cxmWbtVzUYzem4chjHu5cRxUlPNzUJWrrczueB7Ip4A8\n"
  "aQuFMfNXYc0x+WLWjy//urypMKjhAgMBAAGjggGjMIIBnzAbBgNVHREEFDASghB3\n"
  "d3cubWJhbmsuY29tLnBsMAkGA1UdEwQCMAAwDgYDVR0PAQH/BAQDAgWgMB0GA1Ud\n"
  "JQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjBEBgNVHSAEPTA7MDkGC2CGSAGG+EUB\n"
  "BxcGMCowKAYIKwYBBQUHAgEWHGh0dHBzOi8vd3d3LnZlcmlzaWduLmNvbS9jcHMw\n"
  "HQYDVR0OBBYEFN37iGaS7mZnENxZ9FGqNLR+QgoMMB8GA1UdIwQYMBaAFPyKULqe\n"
  "uSVae1WFT5UAY4/pWGtDMEIGA1UdHwQ7MDkwN6A1oDOGMWh0dHA6Ly9FVlNlY3Vy\n"
  "ZS1jcmwudmVyaXNpZ24uY29tL0VWU2VjdXJlMjAwNi5jcmwwfAYIKwYBBQUHAQEE\n"
  "cDBuMC0GCCsGAQUFBzABhiFodHRwOi8vRVZTZWN1cmUtb2NzcC52ZXJpc2lnbi5j\n"
  "b20wPQYIKwYBBQUHMAKGMWh0dHA6Ly9FVlNlY3VyZS1haWEudmVyaXNpZ24uY29t\n"
  "L0VWU2VjdXJlMjAwNi5jZXIwDQYJKoZIhvcNAQEFBQADggEBAD0wO+rooUrIM4qp\n"
  "PHhp+hkXK6WMQ2qzGOmbMcZjw0govg5vkzkefPDryIXXbrF8mRagiJNMSfNaWWeh\n"
  "Cj41OV24EdUl0OLbFxNzcvub599zRs/apfaRLTfsmlmOgi0/YP305i+3tJ2ll946\n"
  "P+qV1wXnXqTqEdIl4Ys3+1HmDCdTB1hoDwAAzqRVUXZ5+iiwPAU7R/LTHfMjV1ke\n"
  "8jtNFfrorlZMCfVH/7eEnHJvVjOJt+YFe4aFMzE+DfuYIK7MH+olC2v79kBwbnEQ\n"
  "fvHMA9gFwOYLUBBdSfcocp8EKZ+mRlNPGR/3LBrPeaQQ0GZEkxzRK+v/aNTuiYfr\n"
  "oFXtrg0=\n"
  "-----END CERTIFICATE-----\n";

  const char *im =
  "-----BEGIN CERTIFICATE-----\n"
  "MIIF5DCCBMygAwIBAgIQW3dZxheE4V7HJ8AylSkoazANBgkqhkiG9w0BAQUFADCB\n"
  "yjELMAkGA1UEBhMCVVMxFzAVBgNVBAoTDlZlcmlTaWduLCBJbmMuMR8wHQYDVQQL\n"
  "ExZWZXJpU2lnbiBUcnVzdCBOZXR3b3JrMTowOAYDVQQLEzEoYykgMjAwNiBWZXJp\n"
  "U2lnbiwgSW5jLiAtIEZvciBhdXRob3JpemVkIHVzZSBvbmx5MUUwQwYDVQQDEzxW\n"
  "ZXJpU2lnbiBDbGFzcyAzIFB1YmxpYyBQcmltYXJ5IENlcnRpZmljYXRpb24gQXV0\n"
  "aG9yaXR5IC0gRzUwHhcNMDYxMTA4MDAwMDAwWhcNMTYxMTA3MjM1OTU5WjCBujEL\n"
  "MAkGA1UEBhMCVVMxFzAVBgNVBAoTDlZlcmlTaWduLCBJbmMuMR8wHQYDVQQLExZW\n"
  "ZXJpU2lnbiBUcnVzdCBOZXR3b3JrMTswOQYDVQQLEzJUZXJtcyBvZiB1c2UgYXQg\n"
  "aHR0cHM6Ly93d3cudmVyaXNpZ24uY29tL3JwYSAoYykwNjE0MDIGA1UEAxMrVmVy\n"
  "aVNpZ24gQ2xhc3MgMyBFeHRlbmRlZCBWYWxpZGF0aW9uIFNTTCBDQTCCASIwDQYJ\n"
  "KoZIhvcNAQEBBQADggEPADCCAQoCggEBAJjboFXrnP0XeeOabhQdsVuYI4cWbod2\n"
  "nLU4O7WgerQHYwkZ5iqISKnnnbYwWgiXDOyq5BZpcmIjmvt6VCiYxQwtt9citsj5\n"
  "OBfH3doxRpqUFI6e7nigtyLUSVSXTeV0W5K87Gws3+fBthsaVWtmCAN/Ra+aM/EQ\n"
  "wGyZSpIkMQht3QI+YXZ4eLbtfjeubPOJ4bfh3BXMt1afgKCxBX9ONxX/ty8ejwY4\n"
  "P1C3aSijtWZfNhpSSENmUt+ikk/TGGC+4+peGXEFv54cbGhyJW+ze3PJbb0S/5tB\n"
  "Ml706H7FC6NMZNFOvCYIZfsZl1h44TO/7Wg+sSdFb8Di7Jdp91zT91ECAwEAAaOC\n"
  "AdIwggHOMB0GA1UdDgQWBBT8ilC6nrklWntVhU+VAGOP6VhrQzASBgNVHRMBAf8E\n"
  "CDAGAQH/AgEAMD0GA1UdIAQ2MDQwMgYEVR0gADAqMCgGCCsGAQUFBwIBFhxodHRw\n"
  "czovL3d3dy52ZXJpc2lnbi5jb20vY3BzMD0GA1UdHwQ2MDQwMqAwoC6GLGh0dHA6\n"
  "Ly9FVlNlY3VyZS1jcmwudmVyaXNpZ24uY29tL3BjYTMtZzUuY3JsMA4GA1UdDwEB\n"
  "/wQEAwIBBjARBglghkgBhvhCAQEEBAMCAQYwbQYIKwYBBQUHAQwEYTBfoV2gWzBZ\n"
  "MFcwVRYJaW1hZ2UvZ2lmMCEwHzAHBgUrDgMCGgQUj+XTGoasjY5rw8+AatRIGCx7\n"
  "GS4wJRYjaHR0cDovL2xvZ28udmVyaXNpZ24uY29tL3ZzbG9nby5naWYwKQYDVR0R\n"
  "BCIwIKQeMBwxGjAYBgNVBAMTEUNsYXNzM0NBMjA0OC0xLTQ3MD0GCCsGAQUFBwEB\n"
  "BDEwLzAtBggrBgEFBQcwAYYhaHR0cDovL0VWU2VjdXJlLW9jc3AudmVyaXNpZ24u\n"
  "Y29tMB8GA1UdIwQYMBaAFH/TZafC3ey78DAJ80M5+gKvMzEzMA0GCSqGSIb3DQEB\n"
  "BQUAA4IBAQCWovp/5j3t1CvOtxU/wHIDX4u6FpAl98KD2Md1NGNoElMMU4l7yVYJ\n"
  "p8M2RE4O0GJis4b66KGbNGeNUyIXPv2s7mcuQ+JdfzOE8qJwwG6Cl8A0/SXGI3/t\n"
  "5rDFV0OEst4t8dD2SB8UcVeyrDHhlyQjyRNddOVG7wl8nuGZMQoIeRuPcZ8XZsg4\n"
  "z+6Ml7YGuXNG5NOUweVgtSV1LdlpMezNlsOjdv3odESsErlNv1HoudRETifLriDR\n"
  "fip8tmNHnna6l9AW5wtsbfdDbzMLKTB3+p359U64drPNGLT5IO892+bKrZvQTtKH\n"
  "qQ2mRHNQ3XBb7a1+Srwi1agm5MKFIA3Z\n"
  "-----END CERTIFICATE-----\n";

  c_cert.raw_cert = (unsigned char *)ee;
  c_cert.cert_size = strlen(ee);
  c_cert.data_format = CKMC_FORM_PEM;

  c_cert1.raw_cert = (unsigned char *)im;
  c_cert1.cert_size = strlen(im);
  c_cert1.data_format = CKMC_FORM_PEM;

  test_policy.password = password;
  test_policy.extractable = true;

  ret = ckmc_save_cert(ca_alias, c_cert1, test_policy);
  if (CKMC_ERROR_NONE != ret)
      /* Error handling */

  untrustedcerts.alias = (char *)ca_alias;
  untrustedcerts.next = NULL;

  ret = ckmc_get_cert_chain_with_alias(&c_cert, &untrustedcerts, &cert_chain_list);
  if (CKMC_ERROR_NONE != ret)
      /* Error handling */

  next=cert_chain_list;
  do {
      current = next;
      next = current->next;
  } while (next != NULL);

  /* Called when the list is no longer needed */
  ckmc_cert_list_all_free(cert_chain_list);
  ```

<a name="pkcs"></a>
## Loading a Certificate or a PKCS#12 File

To load certificates (from a file with the DER or PEM format) or a private key, a certificate, or CA certificates (from a PKCS#12 file):

- Load from a certificate file:

  ```
  int ret = CKMC_ERROR_NONE;

  ckmc_cert_s *pcert;
  /*
     defined_media_storage_directory can be obtained
     with the storage_get_directory() function
  */
  const char *file_name = "<defined_media_storage_directory>/ckmc_test_cert.pem";

  ret = ckmc_load_cert_from_file(file_name, &pcert);
  if (CKMC_ERROR_NONE != ret)
      /* Error handling */

  dlog_print(DLOG_INFO, LOG_TAG, "cert size =%d\n", pcert->cert_size);

  ckmc_cert_free(pcert); /* Called when the certificate is no longer needed */
  ```

- Load from a PKCS#12 file:

  ```
  int ret = CKMC_ERROR_NONE;

  ckmc_pkcs12_s *ppkcs12 = NULL;
  /*
     defined_media_storage_directory can be obtained
     with the storage_get_directory() function
  */
  const char *p12file = "<defined_media_storage_directory>/ckmc_p12_test.p12";
  const char *password = "password"; /* PKCS#12 file can be protected by a password */

  ret = ckmc_pkcs12_load(p12file, password, &ppkcs12);
  if (CKMC_ERROR_NONE != ret || ppkcs12 == NULL)
      /* Error handling */

  if (ppkcs12->priv_key != NULL)
      /* Check a private key */

  if (ppkcs12->cert != NULL)
      /* Check a certificate */

  int cnt = 0;
  ckmc_cert_list_s *tmp_list = ppkcs12->ca_chain;
  while (tmp_list!= NULL) {
      /* Check a certificate list */

      tmp_list = tmp_list->next;
  }
  ckmc_pkcs12_free(ppkcs12); /* Called when the pkcs12 data is no longer needed */
  ```

<a name="access"></a>
## Implementing Access Control

To implement access control rules for each individual client's data, certificates, and keys:

1. Store test data:

   ```
   int ret = CKMC_ERROR_NONE;

   char* password = NULL;
   ckmc_raw_buffer_s test_data;
   const char *alias = "targetData";
   ckmc_policy_s test_policy;

   const char *char_bin_data = "Access control test Data";

   test_policy.password = password;
   test_policy.extractable = true;

   test_data.data = (unsigned char *)char_bin_data;
   test_data.size = strlen(char_bin_data);
   ret = ckmc_save_data(alias, test_data, test_policy);
   if (CKMC_ERROR_NONE != ret)
       /* Error handling */
   ```

2. Set a rule to allow access:

   ```
   int ret = CKMC_ERROR_NONE;

   const char *target1 = "accessor-allow-1";
   const char *target2 = "accessor-allow-2";
   const char *alias = "targetData";

   /* Only allow reading data */
   ret = ckmc_set_permission(alias, target1, CKMC_PERMISSION_READ);
   if (CKMC_ERROR_NONE != ret)
       /* Error handling */

   /* Allow reading and deleting data */
   ret = ckmc_set_permission(alias, target2, CKMC_PERMISSION_READ | CKMC_PERMISSION_REMOVE);
   if (CKMC_ERROR_NONE != ret)
       /* Error handling */
   ```

3. Set a rule to deny access:

   ```
   int ret = CKMC_ERROR_NONE;

   const char *target = "denied-accessor";
   const char *alias = "targetData";

   /* Allow the target user to a read (alias) */
   ret = ckmc_set_permission(alias, target, CKMC_PERMISSION_READ);
   if (CKMC_ERROR_NONE != ret)
       /* Error handling */

   /* Deny the target user access to data (alias) */
   ret = ckmc_set_permission(alias, target, CKMC_PERMISSION_NONE);
   if (CKMC_ERROR_NONE != ret)
       /* Error handling */
   ```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
