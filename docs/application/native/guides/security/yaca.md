# Cryptographic Operations



Previously, Tizen has offered cryptographic functionalities using only external open sources, such as OpenSSL. This meant that when the functionalities of the external open sources changed, it affected your applications. To mitigate this situation, support for YACA (Yet Another Crypto API) has been added, providing your application stable cryptographic functions, such as key management, data integrity, and data encryption and decryption.

The main features of the YACA API include:

- Key management

  You can [manage secure keys](#keymanagement). You can generate secure keys, import a key trying to match it to a specified key type, and export a key to an arbitrary format.

- Data integrity

  The data integrity features provide simple and advanced functionalities for integrity handling. You can [create digital signatures](#signature) and [use message digests](#messagedigest).

- Data encryption and decryption

  The encryption and decryption features provide simple and advanced functionalities for encrypting and decrypting data, and creating an IV. You can use [symmetric](#symmetric) or [asymmetric](#asymmetric) keys for the encryption.

- Certificate handling

  You can [manage X.509 certificates](#certificate), including Certificate Signing Requests (CSRs), attributes, and extensions. You can create and sign CSRs, issue certificates, import and export them, read their contents, and verify them against trusted CA certificates.

## Prerequisites

To enable your application to use the YACA functionality:

1. To use the functions and data types of the [YACA API](../../api/common/latest/group__CAPI__YACA__MODULE.html), include the `<yaca_crypto.h>`, `<yaca_error.h>`, `<yaca_key.h>`, `<yaca_digest.h>`, `<yaca_encrypt.h>`, `<yaca_seal.h>`, `<yaca_sign.h>`, `<yaca_simple.h>`, `<yaca_x509.h>`, `<yaca_x509_req.h>`, `<yaca_x509_attr.h>`, and `<yaca_x509_ext.h>` header files in your application:

   ```
   /* Needed for general operations */
   #include <yaca_crypto.h>
   #include <yaca_error.h>

   /* Needed for key management, digital signatures, and encryption */
   #include <yaca_key.h>

   /* Needed for digital signatures */
   #include <yaca_sign.h>

   /*
      Needed for digital signatures, message digests,
      and encryption with simple functions
   */
   #include <yaca_simple.h>

   /* Needed for message digests */
   #include <yaca_digest>

   /* Needed for symmetric encryption */
   #include <yaca_encrypt.h>

   /* Needed for asymmetric encryption */
   #include <yaca_seal.h>

   /* Needed for X.509 certificates */
   #include <yaca_x509.h>

   /* Needed for X.509 Certificate Signing Requests (CSRs) */
   #include <yaca_x509_req.h>

   /* Needed for X.509 attributes */
   #include <yaca_x509_attr.h>

   /* Needed for X.509 extensions */
   #include <yaca_x509_ext.h>
   ```

2. Initialize and clean up the library:

   1. Initialize the library.

      This function must be called in each thread that uses YACA.

      ```
      int ret = yaca_initialize();
      if (ret != YACA_ERROR_NONE)
          /* Error handling */
      ```

   2. Clean up the library when no longer needed.

      This function must be called before exiting the thread.

      ```
      yaca_cleanup();
      ```

<a name="keymanagement"></a>
## Managing Keys

To generate, import, export, and derive keys:

- Generate and destroy a key:

  ```
  int ret;
  yaca_key_h key = YACA_KEY_NULL;

  ret = yaca_key_generate(YACA_KEY_TYPE_SYMMETRIC, YACA_KEY_LENGTH_256BIT, &key);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */
  yaca_key_destroy(key);

  ret = yaca_key_generate(YACA_KEY_TYPE_DES, YACA_KEY_LENGTH_192BIT, &key);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */
  yaca_key_destroy(key);

  ret = yaca_key_generate(YACA_KEY_TYPE_RSA_PRIV, YACA_KEY_LENGTH_1024BIT, &key);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */
  yaca_key_destroy(key);

  ret = yaca_key_generate(YACA_KEY_TYPE_DSA_PRIV, YACA_KEY_LENGTH_512BIT, &key);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */
  yaca_key_destroy(key);

  ret = yaca_key_generate(YACA_KEY_TYPE_DH_PRIV, YACA_KEY_LENGTH_DH_GENERATOR_2 | 333, &key);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */
  yaca_key_destroy(key);

  ret = yaca_key_generate(YACA_KEY_TYPE_DH_PRIV, YACA_KEY_LENGTH_DH_RFC_2048_224, &key);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */
  yaca_key_destroy(key);

  ret = yaca_key_generate(YACA_KEY_TYPE_EC_PRIV, YACA_KEY_LENGTH_EC_SECP384R1, &key);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */
  yaca_key_destroy(key);
  ```

- Generate the parameters and a key:

  ```
  int ret;
  yaca_key_h key = YACA_KEY_NULL;
  yaca_key_h key_params = YACA_KEY_NULL;

  ret = yaca_key_generate(YACA_KEY_TYPE_DSA_PARAMS, YACA_KEY_LENGTH_512BIT, &key_params);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */

  ret = yaca_key_generate_from_parameters(key_params, &key);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */
  yaca_key_destroy(key);
  yaca_key_destroy(key_params);

  ret = yaca_key_generate(YACA_KEY_TYPE_DH_PARAMS,
                          YACA_KEY_LENGTH_DH_GENERATOR_5 | YACA_KEY_LENGTH_2048BIT, &key_params);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */
  ret = yaca_key_generate_from_parameters(key_params, &key);
  if (ret != YACA_ERROR_NONE)
      goto error;
  yaca_key_destroy(key);
  yaca_key_destroy(key_params);

  ret = yaca_key_generate(YACA_KEY_TYPE_DH_PARAMS, YACA_KEY_LENGTH_DH_RFC_2048_256, &key_params);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */
  ret = yaca_key_generate_from_parameters(key_params, &key);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */
  yaca_key_destroy(key);
  yaca_key_destroy(key_params);

  ret = yaca_key_generate(YACA_KEY_TYPE_EC_PARAMS, YACA_KEY_LENGTH_EC_PRIME256V1, &key_params);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */
  ret = yaca_key_generate_from_parameters(key_params, &key);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */
  yaca_key_destroy(key);
  yaca_key_destroy(key_params);
  ```

- Import and export a symmetric key:

  ```
  int ret;

  char *raw = NULL;
  size_t raw_len;
  char *b64 = NULL;
  size_t b64_len;

  yaca_key_h raw_imported = YACA_KEY_NULL;
  yaca_key_h b64_imported = YACA_KEY_NULL;

  /* BASE64 */
  ret = yaca_key_export(sym, YACA_KEY_FORMAT_DEFAULT, YACA_KEY_FILE_FORMAT_BASE64, NULL, &b64, &b64_len);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */

  ret = yaca_key_import(YACA_KEY_TYPE_SYMMETRIC, NULL, b64, b64_len, &b64_imported);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */

  yaca_free(b64);
  b64 = NULL;
  yaca_key_destroy(b64_imported);

  /* RAW */
  ret = yaca_key_export(sym, YACA_KEY_FORMAT_DEFAULT, YACA_KEY_FILE_FORMAT_RAW, NULL, &raw, &raw_len);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */
  ret = yaca_key_import(YACA_KEY_TYPE_SYMMETRIC, NULL, raw, raw_len, &raw_imported);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */

  yaca_free(raw);
  raw = NULL;
  yaca_key_destroy(raw_imported);
  ```

- Import and export an asymmetric key:

  ```
  int ret;

  char *pem_prv = NULL;
  size_t pem_prv_len;
  char *der_prv = NULL;
  size_t der_prv_len;

  char *pem_pub = NULL;
  size_t pem_pub_len;
  char *der_pub = NULL;
  size_t der_pub_len;

  yaca_key_h pem_prv_imported = YACA_KEY_NULL;
  yaca_key_h der_prv_imported = YACA_KEY_NULL;
  yaca_key_h pem_pub_imported = YACA_KEY_NULL;
  yaca_key_h der_pub_imported = YACA_KEY_NULL;

  /* PEM private */
  ret = yaca_key_export(priv, YACA_KEY_FORMAT_DEFAULT, YACA_KEY_FILE_FORMAT_PEM, NULL, &pem_prv, &pem_prv_len);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */

  ret = yaca_key_import(priv_type, NULL, pem_prv, pem_prv_len, &pem_prv_imported);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */

  yaca_free(pem_prv);
  pem_prv = NULL;
  yaca_key_destroy(pem_prv_imported);

  /* DER private */
  ret = yaca_key_export(priv, YACA_KEY_FORMAT_DEFAULT, YACA_KEY_FILE_FORMAT_DER, NULL, &der_prv, &der_prv_len);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */
  ret = yaca_key_import(priv_type, NULL, der_prv, der_prv_len, &der_prv_imported);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */

  yaca_free(der_prv);
  der_prv = NULL;
  yaca_key_destroy(der_prv_imported);

  /* PEM public */
  ret = yaca_key_export(pub, YACA_KEY_FORMAT_DEFAULT, YACA_KEY_FILE_FORMAT_PEM, NULL, &pem_pub, &pem_pub_len);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */
  ret = yaca_key_import(pub_type, NULL, pem_pub, pem_pub_len, &pem_pub_imported);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */

  yaca_free(pem_pub);
  pem_pub = NULL;
  yaca_key_destroy(pem_pub_imported);

  /* DER public */
  ret = yaca_key_export(pub, YACA_KEY_FORMAT_DEFAULT, YACA_KEY_FILE_FORMAT_DER, NULL, &der_pub, &der_pub_len);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */
  ret = yaca_key_import(pub_type, NULL, der_pub, der_pub_len, &der_pub_imported);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */

  yaca_free(der_pub);
  der_pub = NULL;
  yaca_key_destroy(der_pub_imported);
  ```

- Exchange keys with the DH algorithm:

  ```
  yaca_key_h peer_public_key;

  int ret;
  char *secret = NULL;
  size_t secret_len;
  char *temp_material = NULL;
  size_t temp_material_len;
  char *key_material = NULL;
  size_t key_material_len;
  char *iv_material = NULL;
  size_t iv_material_len;

  yaca_key_h private_key = YACA_KEY_NULL;
  yaca_key_h public_key = YACA_KEY_NULL;
  yaca_key_h params = YACA_KEY_NULL;
  yaca_key_h aes_key = YACA_KEY_NULL;
  yaca_key_h iv = YACA_KEY_NULL;

  ret = yaca_key_extract_parameters(peer_public_key, &params);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */

  ret = yaca_key_generate_from_parameters(params, &private_key);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */

  ret = yaca_key_extract_public(private_key, &public_key);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */

  /* Derive secret */
  ret = yaca_key_derive_dh(private_key, peer_public_key, &secret, &secret_len);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */

  key_material_len = YACA_KEY_LENGTH_192BIT / 8;
  iv_material_len = YACA_KEY_LENGTH_IV_128BIT / 8;
  temp_material_len = key_material_len + iv_material_len;
  ret = yaca_key_derive_kdf(YACA_KDF_X962, YACA_DIGEST_SHA512, secret, secret_len,
                            NULL, 0, temp_material_len, &temp_material);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */

  key_material = temp_material;
  iv_material = temp_material + key_material_len;

  ret = yaca_key_import(YACA_KEY_TYPE_SYMMETRIC, NULL, key_material, key_material_len, &aes_key);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */

  ret = yaca_key_import(YACA_KEY_TYPE_IV, NULL, iv_material, iv_material_len, &iv);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */

  yaca_key_destroy(private_key);
  yaca_key_destroy(public_key);
  yaca_key_destroy(params);
  yaca_key_destroy(aes_key);
  yaca_key_destroy(iv);
  yaca_free(secret);
  yaca_free(temp_material);
  ```

<a name="signature"></a>
## Creating Digital Signatures

To create and verify a signature with an asymmetric algorithm, CMAC, or HMAC:

- Create and verify a signature with an asymmetric algorithm:

  ```
  size_t LOREM4096_SIZE = 4096;
  char lorem4096[LOREM4096_SIZE]; /* Target data for encryption and decryption */

  char *signature = NULL;
  size_t signature_len;

  yaca_key_type_e type = YACA_KEY_TYPE_DSA_PRIV;
  yaca_context_h ctx = YACA_CONTEXT_NULL;
  yaca_key_h prv = YACA_KEY_NULL;
  yaca_key_h pub = YACA_KEY_NULL;
  yaca_padding_e padding = YACA_PADDING_PKCS1_PSS;

  /* Generation */
  if (yaca_key_generate(type, YACA_KEY_LENGTH_1024BIT, &prv) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_key_extract_public(prv, &pub) != YACA_ERROR_NONE)
      /* Error handling */

  /* Signing */
  if (yaca_sign_initialize(&ctx, YACA_DIGEST_SHA512, prv) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_context_set_property(ctx, YACA_PROPERTY_PADDING, (char*)(&padding), sizeof(padding)) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_sign_update(ctx, lorem4096, LOREM4096_SIZE) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_context_get_output_length(ctx, 0, &signature_len) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_malloc(signature_len, (void**)&signature) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_sign_finalize(ctx, signature, &signature_len) != YACA_ERROR_NONE)
      /* Error handling */

  /* Cleanup */
  yaca_context_destroy(ctx);
  ctx = YACA_CONTEXT_NULL;

  /* Verification */
  if (yaca_verify_initialize(&ctx, YACA_DIGEST_SHA512, pub) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_context_set_property(ctx, YACA_PROPERTY_PADDING, (char*)(&padding), sizeof(padding)) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_verify_update(ctx, lorem4096, LOREM4096_SIZE) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_verify_finalize(ctx, signature, signature_len) != YACA_ERROR_NONE)
      /* Verification failed */

  yaca_free(signature);
  yaca_key_destroy(prv);
  yaca_key_destroy(pub);
  yaca_context_destroy(ctx);
  ```

- Create and verify a signature with HMAC:

  ```
  char *signature1 = NULL;
  char *signature2 = NULL;
  size_t signature_len;

  yaca_context_h ctx = YACA_CONTEXT_NULL;
  yaca_key_h key = YACA_KEY_NULL;

  /* Generation */
  if (yaca_key_generate(YACA_KEY_TYPE_SYMMETRIC, YACA_KEY_LENGTH_256BIT, &key) != YACA_ERROR_NONE)
      /* Error handling */

  /* Signing */
  if (yaca_sign_initialize_hmac(&ctx, YACA_DIGEST_SHA512, key) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_sign_update(ctx, lorem4096, LOREM4096_SIZE) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_context_get_output_length(ctx, 0, &signature_len) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_malloc(signature_len, (void**)&signature1) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_sign_finalize(ctx, signature1, &signature_len) != YACA_ERROR_NONE)
      /* Error handling */

  /* Cleanup */
  yaca_context_destroy(ctx);
  ctx = YACA_CONTEXT_NULL;

  /* Verification */
  if (yaca_sign_initialize_hmac(&ctx, YACA_DIGEST_SHA512, key) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_sign_update(ctx, lorem4096, LOREM4096_SIZE) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_context_get_output_length(ctx, 0, &signature_len) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_malloc(signature_len, (void**)&signature2) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_sign_finalize(ctx, signature2, &signature_len) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_memcmp(signature1, signature2, signature_len) != YACA_ERROR_NONE)
      /* HMAC verification failed */

  yaca_free(signature1);
  yaca_free(signature2);
  yaca_key_destroy(key);
  yaca_context_destroy(ctx);
  ```

- Create and verify a signature with CMAC:

  ```
  char *signature1 = NULL;
  char *signature2 = NULL;
  size_t signature_len;

  yaca_context_h ctx = YACA_CONTEXT_NULL;
  yaca_key_h key = YACA_KEY_NULL;

  /* Generation */
  if (yaca_key_generate(YACA_KEY_TYPE_SYMMETRIC, YACA_KEY_LENGTH_256BIT, &key))
      /* Error handling */

  /* Signing */
  if (yaca_sign_initialize_cmac(&ctx, YACA_ENCRYPT_AES, key) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_sign_update(ctx, lorem4096, LOREM4096_SIZE))
      /* Error handling */

  if (yaca_context_get_output_length(ctx, 0, &signature_len) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_malloc(signature_len, (void**)&signature1) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_sign_finalize(ctx, signature1, &signature_len))
      /* Error handling */

  /* Cleanup */
  yaca_context_destroy(ctx);
  ctx = YACA_CONTEXT_NULL;

  /* Verification */
  if (yaca_sign_initialize_cmac(&ctx, YACA_ENCRYPT_AES, key) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_sign_update(ctx, lorem4096, LOREM4096_SIZE))
      /* Error handling */

  if (yaca_context_get_output_length(ctx, 0, &signature_len) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_malloc(signature_len, (void**)&signature2) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_sign_finalize(ctx, signature2, &signature_len))
      /* Error handling */

  if (yaca_memcmp(signature1, signature2, signature_len) != YACA_ERROR_NONE)
      /* CMAC verification failed */

  yaca_free(signature1);
  yaca_free(signature2);
  yaca_key_destroy(key);
  yaca_context_destroy(ctx);
  ```

- Create and verify a signature with the simple functions:

  ```
  size_t LOREM4096_SIZE = 4096;
  char lorem4096[LOREM4096_SIZE]; /* Target data for encryption and decryption */

  yaca_key_type_e type = YACA_KEY_TYPE_RSA_PRIV;

  char *signature = NULL;
  size_t signature_len;

  yaca_key_h prv = YACA_KEY_NULL;
  yaca_key_h pub = YACA_KEY_NULL;

  /* Generation */
  if (yaca_key_generate(type, YACA_KEY_LENGTH_1024BIT, &prv) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_key_extract_public(prv, &pub) != YACA_ERROR_NONE)
      /* Error handling */

  /* Signing */
  if (yaca_simple_calculate_signature(YACA_DIGEST_SHA512, prv, lorem4096, LOREM4096_SIZE, &signature, &signature_len) != YACA_ERROR_NONE)
      /* Error handling */

  /* Verification */
  if (yaca_simple_verify_signature(YACA_DIGEST_SHA512, pub, lorem4096, LOREM4096_SIZE, signature, signature_len) != YACA_ERROR_NONE)
      /* Error handling */

  yaca_free(signature);
  yaca_key_destroy(prv);
  yaca_key_destroy(pub);
  ```

<a name="messagedigest"></a>
## Using Digest Messages

To digest messages:

- Digest a message with the advanced functions:

  ```
  int ret = YACA_ERROR_NONE;
  yaca_context_h ctx;

  ret = yaca_digest_initialize(&ctx, YACA_DIGEST_SHA256);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */

  ret = yaca_digest_update(ctx, lorem1024, 1024);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */

  size_t digest_len;
  ret = yaca_context_get_output_length(ctx, 0, &digest_len);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */

  {
      char digest[digest_len];

      ret = yaca_digest_finalize(ctx, digest, &digest_len);
      if (ret != YACA_ERROR_NONE)
          /* Error handling */
  }

  yaca_context_destroy(ctx);
  ```

- Digest a message with the simple function:

  ```
  int ret = YACA_ERROR_NONE;
  char *digest;
  size_t digest_len;

  ret = yaca_simple_calculate_digest(YACA_DIGEST_SHA256,
                                     lorem1024,
                                     1024, &digest, &digest_len);
  if (ret != YACA_ERROR_NONE)
      /* Error handling */

  yaca_free(digest);
  ```

<a name="symmetric"></a>
## Managing Symmetric Encryption

To encrypt and decrypt data with symmetric keys:

- Encrypt and decrypt with the advanced functions:

    ```
    yaca_encrypt_algorithm_e algo = YACA_ENCRYPT_AES;
    yaca_block_cipher_mode_e bcm = YACA_BCM_ECB;
    yaca_key_type_e key_type = YACA_KEY_TYPE_SYMMETRIC;
    size_t key_bit_len = YACA_KEY_LENGTH_256BIT;

    size_t LOREM4096_SIZE = 4096;
    char lorem4096[LOREM4096_SIZE]; /* Target data for encryption and decryption */

    yaca_context_h ctx = YACA_CONTEXT_NULL;
    yaca_key_h key = YACA_KEY_NULL;
    yaca_key_h iv = YACA_KEY_NULL;
    size_t iv_bit_len;

    char *enc = NULL;
    char *dec = NULL;
    size_t enc_len;
    size_t dec_len;

    size_t block_len;
    size_t output_len;
    size_t written_len;

    /* Key generation */
    if (yaca_key_generate(key_type, key_bit_len, &key) != YACA_ERROR_NONE)
        /* Error handling */

    if (yaca_encrypt_get_iv_bit_length(algo, bcm, key_bit_len, &iv_bit_len) != YACA_ERROR_NONE)
        /* Error handling */

    if (iv_bit_len > 0 && yaca_key_generate(YACA_KEY_TYPE_IV, iv_bit_len, &iv) != YACA_ERROR_NONE)
        /* Error handling */

    /* Encryption */
    {
        if (yaca_encrypt_initialize(&ctx, algo, bcm, key, iv) != YACA_ERROR_NONE)
            /* Error handling */

        /* For the update */
        if (yaca_context_get_output_length(ctx, LOREM4096_SIZE, &output_len) != YACA_ERROR_NONE)
            /* Error handling */

        /* For finalizing */
        if (yaca_context_get_output_length(ctx, 0, &block_len) != YACA_ERROR_NONE)
            /* Error handling */

        /* Calculate the max output: size of update + final chunks */
        enc_len = output_len + block_len;
        if (yaca_malloc(enc_len, (void**)&enc) != YACA_ERROR_NONE)
            /* Error handling */

        if (yaca_encrypt_update(ctx, lorem4096, LOREM4096_SIZE, enc, &written_len) != YACA_ERROR_NONE)
            /* Error handling */

        enc_len = written_len;

        if (yaca_encrypt_finalize(ctx, enc + written_len, &written_len) != YACA_ERROR_NONE)
            /* Error handling */

        enc_len += written_len;

        yaca_context_destroy(ctx);
        ctx = YACA_CONTEXT_NULL;
    }

    /* Decryption */
    {
        if (yaca_decrypt_initialize(&ctx, algo, bcm, key, iv) != YACA_ERROR_NONE)
            /* Error handling */

        /* For the update */
        if (yaca_context_get_output_length(ctx, LOREM4096_SIZE, &output_len) != YACA_ERROR_NONE)
            /* Error handling */

        /* For finalizing */
        if (yaca_context_get_output_length(ctx, 0, &block_len) != YACA_ERROR_NONE)
            /* Error handling */

        /* Calculate the max output: size of update + final chunks */
        dec_len = output_len + block_len;
        if (yaca_malloc(dec_len, (void**)&dec) != YACA_ERROR_NONE)
            /* Error handling */

        if (yaca_decrypt_update(ctx, enc, enc_len, dec, &written_len) != YACA_ERROR_NONE)
            /* Error handling */

        dec_len = written_len;

        if (yaca_decrypt_finalize(ctx, dec + written_len, &written_len) != YACA_ERROR_NONE)
            /* Error handling */

        dec_len += written_len;
    }

    yaca_free(dec);
    yaca_free(enc);
    yaca_context_destroy(ctx);
    yaca_key_destroy(iv);
    yaca_key_destroy(key);
    ```

- Encrypt and decrypt in the AES GCM mode with the advanced functions:

  ```
  size_t LOREM4096_SIZE = 4096;
  char lorem4096[LOREM4096_SIZE]; /* Target data for encryption and decryption */

  yaca_encrypt_algorithm_e algo = YACA_ENCRYPT_AES;
  yaca_block_cipher_mode_e bcm = YACA_BCM_GCM;
  yaca_key_type_e key_type = YACA_KEY_TYPE_SYMMETRIC;
  size_t key_bit_len = YACA_KEY_LENGTH_256BIT;
  size_t iv_bit_len = YACA_KEY_LENGTH_IV_128BIT;

  yaca_context_h ctx = YACA_CONTEXT_NULL;
  yaca_key_h key = YACA_KEY_NULL;
  yaca_key_h iv = YACA_KEY_NULL;

  char *enc = NULL;
  char *dec = NULL;
  size_t enc_len;
  size_t dec_len;

  char *aad = NULL;
  char *tag = NULL;
  size_t aad_len = 16;
  size_t tag_len = 16;

  size_t block_len;
  size_t output_len;
  size_t written_len;

  /* Key generation */
  if (yaca_key_generate(key_type, key_bit_len, &key) != YACA_ERROR_NONE))
      /* Error handling */

  /* IV generation */
  if (yaca_key_generate(YACA_KEY_TYPE_IV, iv_bit_len, &iv) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_zalloc(aad_len, (void**)&aad) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_randomize_bytes(aad, aad_len) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_zalloc(tag_len, (void**)&tag) != YACA_ERROR_NONE)
      /* Error handling */

  /* Encryption */
  {
      if (yaca_encrypt_initialize(&ctx, algo, bcm, key, iv) != YACA_ERROR_NONE)
          /* Error handling */

      /* Provide any AAD data */
      if (yaca_context_set_property(ctx, YACA_PROPERTY_GCM_AAD, aad, aad_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* For the update */
      if (yaca_context_get_output_length(ctx, LOREM4096_SIZE, &output_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* For finalizing */
      if (yaca_context_get_output_length(ctx, 0, &block_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* Calculate the max output: size of update + final chunks */
      enc_len = output_len + block_len;
      if (yaca_malloc(enc_len, (void**)&enc) != YACA_ERROR_NONE)
          /* Error handling */

      if (yaca_encrypt_update(ctx, lorem4096, LOREM4096_SIZE, enc, &written_len) != YACA_ERROR_NONE)
          /* Error handling */

      enc_len = written_len;

      if (yaca_encrypt_finalize(ctx, enc + written_len, &written_len) != YACA_ERROR_NONE)
          /* Error handling */

      enc_len += written_len;

      /* Set the tag length and get the tag after final encryption */
      if (yaca_context_set_property(ctx, YACA_PROPERTY_GCM_TAG_LEN,
                                    (void*)&tag_len, sizeof(tag_len)) != YACA_ERROR_NONE)
          /* Error handling */

      if (yaca_context_get_property(ctx, YACA_PROPERTY_GCM_TAG, (void**)tag, &tag_len) != YACA_ERROR_NONE)
          /* Error handling */

      dump_hex(enc, 16, "Encrypted data (16 of %zu bytes): ", enc_len);

      yaca_context_destroy(ctx);
      ctx = YACA_CONTEXT_NULL;
  }

  /* Decryption */
  {
      if (yaca_decrypt_initialize(&ctx, algo, bcm, key, iv) != YACA_ERROR_NONE)
          /* Error handling */

      /* Provide any AAD data */
      if (yaca_context_set_property(ctx, YACA_PROPERTY_GCM_AAD, aad, aad_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* For the update */
      if (yaca_context_get_output_length(ctx, LOREM4096_SIZE, &output_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* For finalizing */
      if (yaca_context_get_output_length(ctx, 0, &block_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* Calculate the max output: size of update + final chunks */
      dec_len = output_len + block_len;
      if (yaca_malloc(dec_len, (void**)&dec) != YACA_ERROR_NONE)
          /* Error handling */

      if (yaca_decrypt_update(ctx, enc, enc_len, dec, &written_len) != YACA_ERROR_NONE)
          /* Error handling */

      dec_len = written_len;

      /* Set the expected tag value before final decryption */
      if (yaca_context_set_property(ctx, YACA_PROPERTY_GCM_TAG, tag, tag_len) != YACA_ERROR_NONE)
          /* Error handling */

      if (yaca_decrypt_finalize(ctx, dec + written_len, &written_len) != YACA_ERROR_NONE)
          /* Error handling */

      dec_len += written_len;
  }

  yaca_free(enc);
  yaca_free(dec);
  yaca_free(tag);
  yaca_free(aad);
  yaca_context_destroy(ctx);
  yaca_key_destroy(iv);
  yaca_key_destroy(key);
  ```

- Encrypt and decrypt in the AES CCM mode with the advanced functions:

  ```
  size_t LOREM4096_SIZE = 4096;
  char lorem4096[LOREM4096_SIZE]; /* Target data for encryption and decryption */

  yaca_encrypt_algorithm_e algo = YACA_ENCRYPT_AES;
  yaca_block_cipher_mode_e bcm = YACA_BCM_GCM;
  yaca_key_type_e key_type = YACA_KEY_TYPE_SYMMETRIC;
  size_t key_bit_len = YACA_KEY_LENGTH_256BIT;
  size_t iv_bit_len = YACA_KEY_LENGTH_IV_128BIT;

  yaca_context_h ctx = YACA_CONTEXT_NULL;
  yaca_key_h key = YACA_KEY_NULL;
  yaca_key_h iv = YACA_KEY_NULL;

  char *enc = NULL;
  char *dec = NULL;
  size_t enc_len;
  size_t dec_len;

  char *aad = NULL;
  char *tag = NULL;
  size_t aad_len = 16;
  size_t tag_len = 16;

  size_t block_len;
  size_t output_len;
  size_t written_len;

  /* Key generation */
  if (yaca_key_generate(key_type, key_bit_len, &key) != YACA_ERROR_NONE))
      /* Error handling */

  /* IV generation */
  if (yaca_key_generate(YACA_KEY_TYPE_IV, iv_bit_len, &iv) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_zalloc(aad_len, (void**)&aad) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_randomize_bytes(aad, aad_len) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_zalloc(tag_len, (void**)&tag) != YACA_ERROR_NONE)
      /* Error handling */

  /* Encryption */
  {
      if (yaca_encrypt_initialize(&ctx, algo, bcm, key, iv) != YACA_ERROR_NONE)
          /* Error handling */

      /* Provide any AAD data */
      if (yaca_context_set_property(ctx, YACA_PROPERTY_GCM_AAD, aad, aad_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* For the update */
      if (yaca_context_get_output_length(ctx, LOREM4096_SIZE, &output_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* For finalizing */
      if (yaca_context_get_output_length(ctx, 0, &block_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* Calculate the max output: size of update + final chunks */
      enc_len = output_len + block_len;
      if (yaca_malloc(enc_len, (void**)&enc) != YACA_ERROR_NONE)
          /* Error handling */

      if (yaca_encrypt_update(ctx, lorem4096, LOREM4096_SIZE, enc, &written_len) != YACA_ERROR_NONE)
          /* Error handling */

      enc_len = written_len;

      if (yaca_encrypt_finalize(ctx, enc + written_len, &written_len) != YACA_ERROR_NONE)
          /* Error handling */

      enc_len += written_len;

      /* Set the tag length and get the tag after final encryption */
      if (yaca_context_set_property(ctx, YACA_PROPERTY_GCM_TAG_LEN,
                                    (void*)&tag_len, sizeof(tag_len)) != YACA_ERROR_NONE)
          /* Error handling */

      if (yaca_context_get_property(ctx, YACA_PROPERTY_GCM_TAG, (void**)tag, &tag_len) != YACA_ERROR_NONE)
          /* Error handling */

      dump_hex(enc, 16, "Encrypted data (16 of %zu bytes): ", enc_len);

      yaca_context_destroy(ctx);
      ctx = YACA_CONTEXT_NULL;
  }

  /* Decryption */
  {
      if (yaca_decrypt_initialize(&ctx, algo, bcm, key, iv) != YACA_ERROR_NONE)
          /* Error handling */

      /* Provide any AAD data */
      if (yaca_context_set_property(ctx, YACA_PROPERTY_GCM_AAD, aad, aad_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* For the update */
      if (yaca_context_get_output_length(ctx, LOREM4096_SIZE, &output_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* For finalizing */
      if (yaca_context_get_output_length(ctx, 0, &block_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* Calculate the max output: size of update + final chunks */
      dec_len = output_len + block_len;
      if (yaca_malloc(dec_len, (void**)&dec) != YACA_ERROR_NONE)
          /* Error handling */

      if (yaca_decrypt_update(ctx, enc, enc_len, dec, &written_len) != YACA_ERROR_NONE)
          /* Error handling */

      dec_len = written_len;

      /* Set the expected tag value before final decryption */
      if (yaca_context_set_property(ctx, YACA_PROPERTY_GCM_TAG, tag, tag_len) != YACA_ERROR_NONE)
          /* Error handling */

      if (yaca_decrypt_finalize(ctx, dec + written_len, &written_len) != YACA_ERROR_NONE)
          /* Error handling */

      dec_len += written_len;
  }

  yaca_free(enc);
  yaca_free(dec);
  yaca_free(tag);
  yaca_free(aad);
  yaca_context_destroy(ctx);
  yaca_key_destroy(iv);
  yaca_key_destroy(key);
  ```

- Encrypt and decrypt with the simple functions:

  ```
  yaca_encrypt_algorithm_e algo = YACA_ENCRYPT_AES;
  yaca_block_cipher_mode_e bcm = YACA_BCM_ECB;
  size_t key_bit_len = YACA_KEY_LENGTH_256BIT;

  yaca_key_h key = YACA_KEY_NULL;
  yaca_key_h iv = YACA_KEY_NULL;

  char *enc = NULL;
  char *dec = NULL;
  size_t enc_len;
  size_t dec_len;
  size_t iv_bit_len;

  /* Key generation */
  if (yaca_key_derive_pbkdf2("foo bar", "123456789", 10, 1000,
                             YACA_DIGEST_SHA256, key_bit_len, &key) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_encrypt_get_iv_bit_length(algo, bcm, key_bit_len, &iv_bit_len) != YACA_ERROR_NONE)
      /* Error handling */

  if (iv_bit_len > 0 && yaca_key_generate(YACA_KEY_TYPE_IV, iv_bit_len, &iv) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_simple_encrypt(algo, bcm, key, iv, lorem4096, LOREM4096_SIZE, &enc, &enc_len) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_simple_decrypt(algo, bcm, key, iv, enc, enc_len, &dec, &dec_len) != YACA_ERROR_NONE)
      /* Error handling */

  yaca_free(enc);
  yaca_free(dec);
  yaca_key_destroy(iv);
  yaca_key_destroy(key);
  ```

<a name="asymmetric"></a>
## Managing Asymmetric Encryption

To encrypt and decrypt data with asymmetric keys:

- Encrypt and decrypt a message:

  ```
  size_t LOREM4096_SIZE = 4096;
  char lorem4096[LOREM4096_SIZE]; /* Target data for encryption and decryption */

  yaca_encrypt_algorithm_e algo = YACA_ENCRYPT_AES;
  yaca_block_cipher_mode_e bcm = YACA_BCM_CBC;
  size_t key_bit_len = YACA_KEY_LENGTH_256BIT;
  encrypt_seal(algo, bcm, key_bit_len);

  yaca_context_h ctx = YACA_CONTEXT_NULL;
  yaca_key_h key_pub = YACA_KEY_NULL;
  yaca_key_h key_priv = YACA_KEY_NULL;
  yaca_key_h sym_key = YACA_KEY_NULL;
  yaca_key_h iv = YACA_KEY_NULL;

  char *enc = NULL;
  char *dec = NULL;
  size_t enc_len;
  size_t dec_len;

  size_t block_len;
  size_t output_len;
  size_t written_len;

  /* Key generation */
  if (yaca_key_generate(YACA_KEY_TYPE_RSA_PRIV, YACA_KEY_LENGTH_4096BIT, &key_priv) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_key_extract_public(key_priv, &key_pub) != YACA_ERROR_NONE)
      /* Error handling */

  /* Encryption */
  {
      if (yaca_seal_initialize(&ctx, key_pub, algo, bcm, key_bit_len, &sym_key, &iv) != YACA_ERROR_NONE)
          /* Error handling */

      /* For the update */
      if (yaca_context_get_output_length(ctx, LOREM4096_SIZE, &output_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* For finalizing */
      if (yaca_context_get_output_length(ctx, 0, &block_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* Calculate the max output: size of update + final chunks */
      enc_len = output_len + block_len;
      if (yaca_malloc(enc_len, (void**)&enc) != YACA_ERROR_NONE)
          /* Error handling */

      /* Seal and finalize */
      if (yaca_seal_update(ctx, lorem4096, LOREM4096_SIZE, enc, &written_len) != YACA_ERROR_NONE)
          /* Error handling */

      enc_len = written_len;

      if (yaca_seal_finalize(ctx, enc + written_len, &written_len) != YACA_ERROR_NONE)
          /* Error handling */

      enc_len += written_len;

      yaca_context_destroy(ctx);
      ctx = YACA_CONTEXT_NULL;
  }

  /* Decryption */
  {
      if (yaca_open_initialize(&ctx, key_priv, algo, bcm, key_bit_len, sym_key, iv) != YACA_ERROR_NONE)
          /* Error handling */

      /* For the update */
      if (yaca_context_get_output_length(ctx, LOREM4096_SIZE, &output_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* For finalizing */
      if (yaca_context_get_output_length(ctx, 0, &block_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* Calculate the max output: size of update + final chunks */
      dec_len = output_len + block_len;
      if (yaca_malloc(dec_len, (void**)&dec) != YACA_ERROR_NONE)
          /* Error handling */

      /* Open and finalize */
      if (yaca_open_update(ctx, enc, enc_len, dec, &written_len) != YACA_ERROR_NONE)
          /* Error handling */

      dec_len = written_len;

      if (yaca_open_finalize(ctx, dec + written_len, &written_len) != YACA_ERROR_NONE)
          /* Error handling */

      dec_len += written_len;
  }

  yaca_free(dec);
  yaca_free(enc);
  yaca_context_destroy(ctx);
  yaca_key_destroy(sym_key);
  yaca_key_destroy(iv);
  yaca_key_destroy(key_pub);
  yaca_key_destroy(key_priv);
  ```

- Encrypt and decrypt a message with AES GCM:

  ```
  size_t LOREM4096_SIZE = 4096;
  char lorem4096[LOREM4096_SIZE]; /* Target data for encryption and decryption */

  yaca_encrypt_algorithm_e algo = YACA_ENCRYPT_AES;
  yaca_block_cipher_mode_e bcm = YACA_BCM_GCM;
  size_t key_bit_len = YACA_KEY_LENGTH_256BIT;

  yaca_context_h ctx = YACA_CONTEXT_NULL;
  yaca_key_h key_pub = YACA_KEY_NULL;
  yaca_key_h key_priv = YACA_KEY_NULL;
  yaca_key_h sym_key = YACA_KEY_NULL;
  yaca_key_h iv = YACA_KEY_NULL;

  char *enc = NULL;
  char *dec = NULL;
  size_t enc_len;
  size_t dec_len;

  char *aad = NULL;
  char *tag = NULL;
  size_t aad_len = 16;
  size_t tag_len = 13;

  size_t block_len;
  size_t output_len;
  size_t written_len;

  /* Key generation */
  if (yaca_key_generate(YACA_KEY_TYPE_RSA_PRIV, YACA_KEY_LENGTH_4096BIT, &key_priv) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_key_extract_public(key_priv, &key_pub) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_zalloc(aad_len, (void**)&aad) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_randomize_bytes(aad, aad_len) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_zalloc(tag_len, (void**)&tag) != YACA_ERROR_NONE)
      /* Error handling */

  /* Encryption */
  {
      if (yaca_seal_initialize(&ctx, key_pub, algo, bcm, key_bit_len, &sym_key, &iv) != YACA_ERROR_NONE)
          /* Error handling */

      /* Provide any AAD data */
      if (yaca_context_set_property(ctx, YACA_PROPERTY_GCM_AAD, aad, aad_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* For the update */
      if (yaca_context_get_output_length(ctx, LOREM4096_SIZE, &output_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* For finalizing */
      if (yaca_context_get_output_length(ctx, 0, &block_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* Calculate the max output: size of update + final chunks */
      enc_len = output_len + block_len;
      if (yaca_malloc(enc_len, (void**)&enc) != YACA_ERROR_NONE)
          /* Error handling */

      if (yaca_seal_update(ctx, lorem4096, LOREM4096_SIZE, enc, &written_len) != YACA_ERROR_NONE)
          /* Error handling */

      enc_len = written_len;

      if (yaca_seal_finalize(ctx, enc + written_len, &written_len) != YACA_ERROR_NONE)
          /* Error handling */

      enc_len += written_len;

      /* Set the tag length and get the tag after final encryption */
      if (yaca_context_set_property(ctx, YACA_PROPERTY_GCM_TAG_LEN,
                                    (void*)&tag_len, sizeof(tag_len)) != YACA_ERROR_NONE)
          /* Error handling */

      if (yaca_context_get_property(ctx, YACA_PROPERTY_GCM_TAG, (void**)tag, &tag_len) != YACA_ERROR_NONE)
          /* Error handling */

      yaca_context_destroy(ctx);
      ctx = YACA_CONTEXT_NULL;
  }

  /* Decryption */
  {
      if (yaca_open_initialize(&ctx, key_priv, algo, bcm, key_bit_len, sym_key, iv) != YACA_ERROR_NONE)
          /* Error handling */

      /* Provide any AAD data */
      if (yaca_context_set_property(ctx, YACA_PROPERTY_GCM_AAD, aad, aad_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* For the update */
      if (yaca_context_get_output_length(ctx, LOREM4096_SIZE, &output_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* For finalizing */
      if (yaca_context_get_output_length(ctx, 0, &block_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* Calculate the max output: size of update + final chunks */
      dec_len = output_len + block_len;
      if (yaca_malloc(dec_len, (void**)&dec) != YACA_ERROR_NONE)
          /* Error handling */

      if (yaca_open_update(ctx, enc, enc_len, dec, &written_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* Set the expected tag value before final decryption */
      if (yaca_context_set_property(ctx, YACA_PROPERTY_GCM_TAG, tag, tag_len) != YACA_ERROR_NONE)
          /* Error handling */

      dec_len = written_len;

      if (yaca_open_finalize(ctx, dec + written_len, &written_len) != YACA_ERROR_NONE)
          /* Error handling */

      dec_len += written_len;
  }

  yaca_free(dec);
  yaca_free(enc);
  yaca_context_destroy(ctx);
  yaca_key_destroy(sym_key);
  yaca_key_destroy(iv);
  yaca_free(aad);
  yaca_free(tag);
  yaca_key_destroy(key_pub);
  yaca_key_destroy(key_priv);
  ```

- Seal and open a message with AES CCM:

  ```
  size_t LOREM4096_SIZE = 4096;
  char lorem4096[LOREM4096_SIZE]; /* Target data for encryption and decryption */

  yaca_encrypt_algorithm_e algo = YACA_ENCRYPT_AES;
  yaca_block_cipher_mode_e bcm = YACA_BCM_CCM;
  size_t key_bit_len = YACA_KEY_LENGTH_192BIT;

  yaca_context_h ctx = YACA_CONTEXT_NULL;
  yaca_key_h key_pub = YACA_KEY_NULL;
  yaca_key_h key_priv = YACA_KEY_NULL;
  yaca_key_h sym_key = YACA_KEY_NULL;
  yaca_key_h iv = YACA_KEY_NULL;

  char *enc = NULL;
  char *dec = NULL;
  size_t enc_len;
  size_t dec_len;

  char *aad = NULL;
  char *tag = NULL;
  size_t aad_len = 16;
  size_t tag_len = 8;

  size_t block_len;
  size_t output_len;
  size_t written_len;
  size_t len;

  /* Key generation */
  if (yaca_key_generate(YACA_KEY_TYPE_RSA_PRIV, YACA_KEY_LENGTH_3072BIT, &key_priv) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_key_extract_public(key_priv, &key_pub) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_zalloc(aad_len, (void**)&aad) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_randomize_bytes(aad, aad_len) != YACA_ERROR_NONE)
      /* Error handling */

  if (yaca_zalloc(tag_len, (void**)&tag) != YACA_ERROR_NONE)
      /* Error handling */

  /* Encryption */
  {
      if (yaca_seal_initialize(&ctx, key_pub, algo, bcm, key_bit_len, &sym_key, &iv) != YACA_ERROR_NONE)
          /* Error handling */

      /* Set the tag length (optionally) */
      if (yaca_context_set_property(ctx, YACA_PROPERTY_CCM_TAG_LEN,
                                    (void*)&tag_len, sizeof(tag_len)) != YACA_ERROR_NONE)
          /* Error handling */

      /* The total plain text length must be passed (only needed if AAD is passed) */
      if (yaca_seal_update(ctx, NULL, LOREM4096_SIZE, NULL, &len) != YACA_ERROR_NONE)
          /* Error handling */

      /* Provide any AAD data */
      if (yaca_context_set_property(ctx, YACA_PROPERTY_CCM_AAD, aad, aad_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* For the update */
      if (yaca_context_get_output_length(ctx, LOREM4096_SIZE, &output_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* For finalizing */
      if (yaca_context_get_output_length(ctx, 0, &block_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* Calculate the max output: size of update + final chunks */
      enc_len = output_len + block_len;
      if (yaca_malloc(enc_len, (void**)&enc) != YACA_ERROR_NONE)
          /* Error handling */

      if (yaca_seal_update(ctx, lorem4096, LOREM4096_SIZE, enc, &written_len) != YACA_ERROR_NONE)
          /* Error handling */

      enc_len = written_len;

      if (yaca_seal_finalize(ctx, enc + written_len, &written_len) != YACA_ERROR_NONE)
          /* Error handling */

      enc_len += written_len;

      /* Get the tag after final encryption */
      if (yaca_context_get_property(ctx, YACA_PROPERTY_CCM_TAG, (void**)tag, &tag_len) != YACA_ERROR_NONE)
          /* Error handling */

      yaca_context_destroy(ctx);
      ctx = YACA_CONTEXT_NULL;
  }

  /* Decryption */
  {
      if (yaca_open_initialize(&ctx, key_priv, algo, bcm, key_bit_len, sym_key, iv) != YACA_ERROR_NONE)
          /* Error handling */

      /* Set the expected tag value */
      if (yaca_context_set_property(ctx, YACA_PROPERTY_CCM_TAG, tag, tag_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* The total encrypted text length must be passed (only needed if AAD is passed) */
      if (yaca_open_update(ctx, NULL, enc_len, NULL, &len) != YACA_ERROR_NONE)
          /* Error handling */

      /* Provide any AAD data */
      if (yaca_context_set_property(ctx, YACA_PROPERTY_CCM_AAD, aad, aad_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* For the update */
      if (yaca_context_get_output_length(ctx, LOREM4096_SIZE, &output_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* For finalizing */
      if (yaca_context_get_output_length(ctx, 0, &block_len) != YACA_ERROR_NONE)
          /* Error handling */

      /* Calculate the max output: size of update + final chunks */
      dec_len = output_len + block_len;
      if (yaca_malloc(dec_len, (void**)&dec) != YACA_ERROR_NONE)
          /* Error handling */

      /*
         Tag verification is done when you call the final yaca_open_update()
         function, there is no call to the yaca_open_finalize() function
      */
      if (yaca_open_update(ctx, enc, enc_len, dec, &written_len) != YACA_ERROR_NONE)
          /* Error handling */

      dec_len = written_len;
  }

  yaca_free(dec);
  yaca_free(enc);
  yaca_context_destroy(ctx);
  yaca_key_destroy(sym_key);
  yaca_key_destroy(iv);
  yaca_free(aad);
  yaca_free(tag);
  yaca_key_destroy(key_pub);
  yaca_key_destroy(key_priv);
  ```

<a name="certificate"></a>
## Managing X.509 Certificates

You can create, sign, import, export, read, and verify X.509 certificates and Certificate Signing Requests (CSRs), and add attributes and extensions to them.

The examples assume that `yaca_initialize()` has already been called in the current thread. Each example declares all handles up front, initializes them to their NULL values, and releases them in a `cleanup` section, so the cleanup is safe on any error path. Every call checks its return value. When a call fails, the example jumps to `cleanup` and returns the error code in `ret`.

- Create a CSR and sign it:

  ```
  int ret = YACA_ERROR_NONE;
  yaca_key_h priv_key = YACA_KEY_NULL;
  yaca_key_h pub_key = YACA_KEY_NULL;
  yaca_x509_req_h req = YACA_X509_REQ_NULL;

  ret = yaca_key_generate(YACA_KEY_TYPE_RSA_PRIV, YACA_KEY_LENGTH_2048BIT, &priv_key);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_key_extract_public(priv_key, &pub_key);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_x509_req_new(&req);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_x509_req_set_version(req, YACA_X509_REQ_VERSION_1);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_x509_req_set_subject(req, "C = KR, O = Example, CN = device.example.com");
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_x509_req_set_public_key(req, pub_key);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  /* The signature covers the subject, the public key, and the extensions */
  ret = yaca_x509_req_sign(req, priv_key, YACA_DIGEST_SHA256);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  /* The CSR is ready to be exported or used to issue a certificate */

  cleanup:
  yaca_x509_req_destroy(&req);
  yaca_key_destroy(pub_key);
  yaca_key_destroy(priv_key);
  return ret;
  ```

- Verify the CSR signature:

  ```
  int ret = YACA_ERROR_NONE;
  yaca_x509_req_h req = YACA_X509_REQ_NULL;
  yaca_key_h req_pub_key = YACA_KEY_NULL;

  /* req is a CSR imported or created earlier.
   * YACA_ERROR_DATA_MISMATCH means the signature does not match the public key in the CSR. */
  ret = yaca_x509_req_verify(req);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_x509_req_get_public_key(req, &req_pub_key);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  cleanup:
  yaca_key_destroy(req_pub_key);
  yaca_x509_req_destroy(&req);
  return ret;
  ```

- Issue a CA certificate (self-signed) and a leaf certificate from a CSR:

  ```
  int ret = YACA_ERROR_NONE;
  time_t not_before = time(NULL);
  time_t not_after = not_before + 365 * 24 * 3600;

  yaca_key_h ca_priv = YACA_KEY_NULL;
  yaca_key_h ca_pub = YACA_KEY_NULL;
  yaca_x509_req_h ca_req = YACA_X509_REQ_NULL;
  yaca_x509_h ca_cert = YACA_X509_NULL;
  yaca_key_h leaf_priv = YACA_KEY_NULL;
  yaca_key_h leaf_pub = YACA_KEY_NULL;
  yaca_x509_req_h leaf_req = YACA_X509_REQ_NULL;
  yaca_x509_h leaf_cert = YACA_X509_NULL;
  yaca_x509_ext_h ca_ext = YACA_X509_EXT_NULL;

  /* 1. CA key and CSR, with the CA:TRUE basic constraint.
   *    For an intermediate CA, use a config such as "CA:TRUE, pathlen:0" to limit
   *    how many CA certificates may follow it in a chain. */
  ret = yaca_key_generate(YACA_KEY_TYPE_RSA_PRIV, YACA_KEY_LENGTH_2048BIT, &ca_priv);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_key_extract_public(ca_priv, &ca_pub);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_x509_req_new(&ca_req);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_x509_req_set_version(ca_req, YACA_X509_REQ_VERSION_1);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_x509_req_set_subject(ca_req, "C = KR, O = Example, CN = Example Root CA");
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_x509_req_set_public_key(ca_req, ca_pub);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_x509_ext_new_by_config(YACA_EXT_OID_BASIC_CONSTRAINTS, 1, "CA:TRUE", &ca_ext);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_x509_req_add_extensions(ca_req, &ca_ext, 1);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_x509_req_sign(ca_req, ca_priv, YACA_DIGEST_SHA256);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  /* 2. Self-signed CA certificate: ca_cert is YACA_X509_NULL, issuer = subject.
   *    YACA_EXT_COPY_ALL copies the CA:TRUE extension from the CSR. */
  ret = yaca_x509_issue(ca_req, YACA_X509_NULL, ca_priv, NULL,
                        not_before, not_after, YACA_DIGEST_SHA256,
                        YACA_EXT_COPY_ALL, &ca_cert);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  /* 3. Leaf key and CSR */
  ret = yaca_key_generate(YACA_KEY_TYPE_RSA_PRIV, YACA_KEY_LENGTH_2048BIT, &leaf_priv);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_key_extract_public(leaf_priv, &leaf_pub);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_x509_req_new(&leaf_req);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_x509_req_set_version(leaf_req, YACA_X509_REQ_VERSION_1);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_x509_req_set_subject(leaf_req, "C = KR, O = Example, CN = device.example.com");
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_x509_req_set_public_key(leaf_req, leaf_pub);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_x509_req_sign(leaf_req, leaf_priv, YACA_DIGEST_SHA256);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  /* 4. Leaf certificate signed by the CA key. The CA private key must match ca_cert.
   *    Serial NULL: a random serial number is generated. */
  ret = yaca_x509_issue(leaf_req, ca_cert, ca_priv, NULL,
                        not_before, not_after, YACA_DIGEST_SHA256,
                        YACA_EXT_COPY_NONE, &leaf_cert);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  /* Use leaf_cert and ca_cert */

  cleanup:
  yaca_x509_destroy(&leaf_cert);
  yaca_x509_destroy(&ca_cert);
  yaca_x509_req_destroy(&leaf_req);
  yaca_key_destroy(leaf_pub);
  yaca_key_destroy(leaf_priv);
  yaca_x509_ext_destroy(ca_ext);
  yaca_x509_req_destroy(&ca_req);
  yaca_key_destroy(ca_pub);
  yaca_key_destroy(ca_priv);
  return ret;
  ```

- Verify a certificate against a trusted CA certificate:

  ```
  int ret = YACA_ERROR_NONE;
  yaca_x509_verify_result_e result = YACA_X509_VERIFY_OK;
  yaca_x509_h leaf_cert = YACA_X509_NULL;   /* Certificate to verify */
  yaca_x509_h ca_cert = YACA_X509_NULL;     /* Trusted root CA certificate */
  yaca_x509_h trusted[1];
  yaca_x509_h untrusted[1];
  yaca_x509_h inter_cert = YACA_X509_NULL;  /* Intermediate CA certificate (signed by ca_cert) */

  trusted[0] = ca_cert;

  /* Pass NULL and 0 for untrusted certificates when there are none */
  ret = yaca_x509_verify_cert(leaf_cert, trusted, 1, NULL, 0, &result);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  /* A failed verification is not an API error: ret stays YACA_ERROR_NONE
   * and the outcome is in result (expired, untrusted, self-signed, signature, ...) */
  if (result != YACA_X509_VERIFY_OK) {
      /* Handle the failure */
      goto cleanup;
  }

  /* To also require the CA flag on intermediate and root certificates: */
  ret = yaca_x509_verify_cert_with_caflag(leaf_cert, trusted, 1, NULL, 0, &result);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  if (result != YACA_X509_VERIFY_OK) {
      /* Handle the failure */
      goto cleanup;
  }

  /* Chain: leaf_cert -> inter_cert -> ca_cert. Only ca_cert is trusted;
   * inter_cert is passed as an untrusted certificate to complete the chain */
  untrusted[0] = inter_cert;
  ret = yaca_x509_verify_cert(leaf_cert, trusted, 1, untrusted, 1, &result);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  if (result != YACA_X509_VERIFY_OK) {
      /* Handle the failure */
      goto cleanup;
  }

  cleanup:
  return ret;
  ```

- Export a certificate to PEM or DER data, and import it back:

  ```
  int ret = YACA_ERROR_NONE;
  yaca_x509_h cert = YACA_X509_NULL;   /* Certificate to export */
  yaca_x509_h imported = YACA_X509_NULL;
  char *pem = NULL;
  size_t pem_len = 0;

  ret = yaca_x509_export(cert, YACA_CERT_FORMAT_PEM, &pem, &pem_len);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  /* pem_len does not include the terminating null byte */
  ret = yaca_x509_import(YACA_CERT_FORMAT_PEM, pem, pem_len, &imported, NULL);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  cleanup:
  yaca_x509_destroy(&imported);
  yaca_free(pem);
  yaca_x509_destroy(&cert);
  return ret;
  ```

  To store and load a file instead:

  ```
  int ret = YACA_ERROR_NONE;
  yaca_x509_h cert = YACA_X509_NULL;
  yaca_x509_h loaded = YACA_X509_NULL;

  ret = yaca_x509_export_to_file(cert, YACA_CERT_FORMAT_DER, "/tmp/device_cert.der");
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  /* Tries PEM first, then DER */
  ret = yaca_x509_import_from_file("/tmp/device_cert.der", &loaded, NULL);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  cleanup:
  yaca_x509_destroy(&loaded);
  yaca_x509_destroy(&cert);
  return ret;
  ```

- Read the information of a certificate:

  ```
  int ret = YACA_ERROR_NONE;
  yaca_x509_h cert = YACA_X509_NULL;   /* Certificate to read */
  time_t not_before = 0;
  time_t not_after = 0;
  yaca_key_h pub_key = YACA_KEY_NULL;
  char *subject = NULL;
  size_t subject_len = 0;
  char *cn = NULL;
  size_t cn_len = 0;
  unsigned long hash = 0;

  /* Validity period: either output can be NULL if not needed */
  ret = yaca_x509_get_validity(cert, &not_before, &not_after);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_x509_get_public_key(cert, &pub_key);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  /* Full subject name in RFC 4514 format, e.g. "CN = Test, O = Org, C = US" */
  ret = yaca_x509_get_string_field(cert, YACA_X509_FIELD_SUBJECT, &subject, &subject_len);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  /* Only the first CN is returned if there are several */
  ret = yaca_x509_get_string_field(cert, YACA_X509_FIELD_SUBJECT_COMMON_NAME, &cn, &cn_len);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_x509_get_subject_hash(cert, &hash);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  cleanup:
  yaca_free(cn);
  yaca_free(subject);
  yaca_key_destroy(pub_key);
  yaca_x509_destroy(&cert);
  return ret;
  ```

- Import a certificate chain from one buffer. The `consumed` value tells you where the next certificate starts:

  ```
  int ret = YACA_ERROR_NONE;
  const char *chain_pem = NULL;   /* PEM data with several certificates, e.g. read from a file */
  size_t chain_len = 0;
  size_t offset = 0;
  size_t consumed = 0;
  yaca_x509_h cert = YACA_X509_NULL;

  /* Import the first certificate of the chain */
  ret = yaca_x509_import(YACA_CERT_FORMAT_PEM, chain_pem, chain_len, &cert, &consumed);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  /* Use cert, then release it */
  yaca_x509_destroy(&cert);

  /* To import the next certificate, move the buffer pointer by consumed bytes
   * and call yaca_x509_import() again with the remaining length */
  offset += consumed;

  cleanup:
  yaca_x509_destroy(&cert);
  return ret;
  ```

- Export a CSR, import it back, and duplicate it. A CSR must be signed before it is duplicated:

  ```
  int ret = YACA_ERROR_NONE;
  yaca_x509_req_h req = YACA_X509_REQ_NULL;     /* Signed CSR */
  yaca_x509_req_h imported = YACA_X509_REQ_NULL;
  yaca_x509_req_h copy = YACA_X509_REQ_NULL;
  char *pem = NULL;
  size_t pem_len = 0;

  ret = yaca_x509_req_export(req, YACA_CERT_FORMAT_PEM, &pem, &pem_len);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_x509_req_import(YACA_CERT_FORMAT_PEM, pem, pem_len, &imported);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_x509_req_dup(imported, &copy);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  cleanup:
  yaca_x509_req_destroy(&copy);
  yaca_x509_req_destroy(&imported);
  yaca_free(pem);
  yaca_x509_req_destroy(&req);
  return ret;
  ```

  To store a CSR in a file, use `yaca_x509_req_export_to_file()`, and read it back with `yaca_x509_req_import_from_file()`.

- Read the subject and public key of a CSR:

  ```
  int ret = YACA_ERROR_NONE;
  yaca_x509_req_h req = YACA_X509_REQ_NULL;   /* CSR to read */
  char *subject = NULL;
  size_t subject_len = 0;
  yaca_key_h pub_key = YACA_KEY_NULL;
  long version = 0;

  ret = yaca_x509_req_get_version(req, &version);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_x509_req_get_subject(req, &subject, &subject_len);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_x509_req_get_public_key(req, &pub_key);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  cleanup:
  yaca_key_destroy(pub_key);
  yaca_free(subject);
  yaca_x509_req_destroy(&req);
  return ret;
  ```

- Add attributes to a CSR:

  ```
  int ret = YACA_ERROR_NONE;
  yaca_x509_req_h req = YACA_X509_REQ_NULL;   /* CSR being built */
  yaca_x509_attr_h attr = YACA_X509_ATTR_NULL;
  const char *password = "secret";

  /* Create an attribute from its NID and add it to the CSR. The CSR keeps its own copy. */
  ret = yaca_x509_attr_new(YACA_ATTR_NID_CHALLENGE_PASSWORD, YACA_ATTR_DATA_TYPE_UTF8STRING,
                           (const unsigned char *)password, strlen(password), &attr);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  ret = yaca_x509_req_add_attr(req, attr);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  /* Or add it directly by NID, without creating an attribute handle */
  ret = yaca_x509_req_add_attr_by_nid(req, YACA_ATTR_NID_UNSTRUCTURED_NAME,
                                      YACA_ATTR_DATA_TYPE_ASCII,
                                      (const unsigned char *)"device-01", strlen("device-01"));
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  cleanup:
  yaca_x509_attr_destroy(attr);
  yaca_x509_req_destroy(&req);
  return ret;
  ```

  Supported attribute NIDs are `YACA_ATTR_NID_CHALLENGE_PASSWORD`, `YACA_ATTR_NID_UNSTRUCTURED_NAME`, and `YACA_ATTR_NID_EXTENSION_REQUEST`. Supported data types are `YACA_ATTR_DATA_TYPE_UTF8STRING` and `YACA_ATTR_DATA_TYPE_ASCII`.

- Read the attributes of a CSR:

  ```
  int ret = YACA_ERROR_NONE;
  yaca_x509_req_h req = YACA_X509_REQ_NULL;   /* CSR to read */
  size_t count = 0;
  size_t i;
  yaca_attr_nid_e nid = YACA_ATTR_NID_UNKNOWN;
  unsigned char *data = NULL;
  size_t data_len = 0;

  ret = yaca_x509_req_get_attr_count(req, &count);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  for (i = 0; i < count; i++) {
      /* If several attributes share the same type, only the first one of that type is returned */
      ret = yaca_x509_req_get_attr(req, (int)i, &nid, &data, &data_len);
      if (ret != YACA_ERROR_NONE)
          goto cleanup;

      /* Use data (length data_len) */
      yaca_free(data);
      data = NULL;
  }

  /* Delete the attribute at index 0 */
  if (count > 0) {
      ret = yaca_x509_req_delete_attr(req, 0);
      if (ret != YACA_ERROR_NONE)
          goto cleanup;
  }

  cleanup:
  yaca_free(data);
  yaca_x509_req_destroy(&req);
  return ret;
  ```

- Add extensions to a CSR:

  ```
  int ret = YACA_ERROR_NONE;
  yaca_x509_req_h req = YACA_X509_REQ_NULL;   /* CSR being built */
  yaca_x509_ext_h exts[2] = { YACA_X509_EXT_NULL, YACA_X509_EXT_NULL };

  /* Key usage, from a config string */
  ret = yaca_x509_ext_new_by_config(YACA_EXT_OID_KEY_USAGE, 1,
                                    "digitalSignature,keyEncipherment", &exts[0]);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  /* Subject Alternative Name, from an OID string and a config string */
  ret = yaca_x509_ext_new_by_oid_string_config("2.5.29.17", 0,
                                               "DNS:device.example.com,DNS:*.example.com", &exts[1]);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  /* The CSR keeps its own copy, so the extension handles must still be destroyed */
  ret = yaca_x509_req_add_extensions(req, exts, 2);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  cleanup:
  yaca_x509_ext_destroy(exts[1]);
  yaca_x509_ext_destroy(exts[0]);
  yaca_x509_req_destroy(&req);
  return ret;
  ```

Adding extensions to a CSR also adds the `extensionRequest` attribute to it automatically. Do not add that attribute yourself.

- Read the extensions of a CSR or a certificate:

  ```
  int ret = YACA_ERROR_NONE;
  yaca_x509_h cert = YACA_X509_NULL;   /* Certificate to read (use yaca_x509_req_get_extensions() for a CSR) */
  size_t ext_count = 0;
  yaca_x509_ext_h *exts = NULL;
  size_t i = 0;

  ret = yaca_x509_get_extensions(cert, &ext_count, &exts);
  if (ret != YACA_ERROR_NONE)
      goto cleanup;

  for (i = 0; i < ext_count; i++) {
      char *oid = NULL;
      size_t oid_len = 0;
      char *config = NULL;
      size_t config_len = 0;
      int critical = 0;

      ret = yaca_x509_ext_get_oid(exts[i], &oid, &oid_len);
      if (ret != YACA_ERROR_NONE)
          goto cleanup_ext;

      ret = yaca_x509_ext_get_critical(exts[i], &critical);
      if (ret != YACA_ERROR_NONE)
          goto cleanup_ext;

      /* The value as a config string, e.g. "CA:TRUE" or "DNS:example.com" */
      ret = yaca_x509_ext_get_data_str(exts[i], &config, &config_len);
      if (ret != YACA_ERROR_NONE)
          goto cleanup_ext;

      /* Use oid, critical, and config */

  cleanup_ext:
      yaca_free(config);
      yaca_free(oid);
      yaca_x509_ext_destroy(exts[i]);
      exts[i] = YACA_X509_EXT_NULL;
      if (ret != YACA_ERROR_NONE)
          goto cleanup;
  }

  cleanup:
  /* Destroy the extensions that were not reached after an error */
  for (; exts != NULL && i < ext_count; i++)
      yaca_x509_ext_destroy(exts[i]);
  yaca_free(exts);
  yaca_x509_destroy(&cert);
  return ret;
  ```

  Each extension handle must be destroyed with `yaca_x509_ext_destroy()`, and the array itself must be freed with `yaca_free()`.

## Related Information
- Dependencies
  - Since Tizen 3.0
  - Since Tizen 10.1 (X.509 certificates, CSRs, attributes, and extensions)