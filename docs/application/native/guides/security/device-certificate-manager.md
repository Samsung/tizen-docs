# Device Certificate Manager

The Device Certificate Manager (DCM) provides cryptography services (digital certificates and keys) for authentication and secure communication with another system. Device certificate and key was embedded in device storage.

The main features of the Device Certificate Manager API include:

- Getting key type/length

- Getting certificate chain

- Creating digital signatures

## Prerequisites

To enable your application to use the Device Certificate Manager functionality:

1. To use the Device Certificate Manager API (in [mobile](../../api/mobile/latest/group__CAPI__DEVICE__CERTIFICATE__MANAGER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__DEVICE__CERTIFICATE__MANAGER__MODULE.html) applications), the application must request permission by adding the following privilege to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <privilege>http://tizen.org/privilege/devicecertificate</privilege>
   </privileges>
   ```

2. Before using the Device Certificate Manager API, check whether the device supports the device certificate feature with the `system_info_get_platform_bool()` function. If the device supports the Device Certificate Manager API, the function returns `true` in the second parameter.

   ```
   bool dcm_support;
   system_info_get_platform_bool("http://tizen.org/feature/security.device_certificate", &dcm_support);
   ```

3. To use the functions and data types of the Device Certificate Manager API, include the `<device_certificate_manager.h>` header file in your application:

   ```
   #include <device_certificate_manager.h>
   ```

<a name="device_certificate_manager"></a>
## Device Certificate Manager API usage example

- Getting key type/length:
  ```
    int result;
    void *key_ctx = NULL;
    char *key_type = NULL;
    size_t key_len;

    result = dcm_create_key_context("example_client", "test_usage", "", &key_ctx);
    if(result != DCM_ERROR_NONE) {
        printf("Can't create context\n");
        goto exit;
    }

    result = dcm_get_key_type(key_ctx, &key_type);
    if(result != DCM_ERROR_NONE) {
        printf("Can't get key type\n");
        goto exit;
    }

    result = dcm_get_key_bit_length(key_ctx, &key_len);
    if(result != DCM_ERROR_NONE) {
        printf("Can't get key length\n");
        goto exit;
    }

    printf("Private key is %s\n", key_type);
    printf("Private key is %d bits\n", key_len);

  exit:
    free(key_type);
    dcm_free_key_context(key_ctx);

    return result;
  ```
- Getting certificate chain:
  ```
    int result;
    void *key_ctx = NULL;
    char *cert_chain = NULL;
    size_t cert_chain_len;

    result = dcm_create_key_context("example_client", "test_usage", "", &key_ctx);
    if(result != DCM_ERROR_NONE) {
        printf("Can't create context\n");
        goto exit;
    }

    result = dcm_get_certificate_chain(key_ctx, &cert_chain, &cert_chain_len);
    if(result != DCM_ERROR_NONE) {
        printf("Can't get cert chain\n");
        goto exit;
    }

    printf("Cert is %d bytes\n", cert_chain_len);
    printf("Received cert %s\n", cert_chain);

  exit:
    free(cert_chain);
    dcm_free_key_context(key_ctx);

    return result;
  ```

- Creating digital signatures:
  ```
    int result;
    void *key_ctx = NULL;
    char *signature = NULL;
    size_t signature_len;

    result = dcm_create_key_context("example_client", "test_usage", "", &key_ctx);
    if(result != DCM_ERROR_NONE) {
        printf("Can't create context\n");
        goto exit;
    }

    result = dcm_create_signature(key_ctx, DCM_DIGEST_SHA256, "12345678901234567890123456789012", 32, &signature, &signature_len);
    if(result != DCM_ERROR_NONE) {
        printf("Can't create signature\n");
        goto exit;
    }

    for(int i = 0; i < signature_len; i++) {
        printf("%x ", (int)(*(unsigned char*)(&signature[i])));
    }
    printf("\n");

  exit:
    free(signature);
    dcm_free_key_context(key_ctx);

    return result;
  ```

## Related information
- Dependencies
  - Tizen 5.0 and Higher for Mobile
  - Tizen 5.0 and Higher for Wearable
