# gbs changelog

Subcommand changelog is used to generate changelog file in ./packaging dir. It is mostly used for creating a changelog before submitting code. You can get the usage of subcommand changelog by using '$ gbs changelog --help'

```bash
$ gbs changelog --help
```

Examples:

```bash
test@test-desktop:~/acpid$ gbs ch --since=bed424ad5ddf74f907de0c19043e486f36e594b9
info: Change log has been updated.
test@test-desktop:~/acpid$ head packaging/acpid.changes
* Wed May 30 2012 xxxx <xxxx@example.com> 2.0.14@5c5f459
- cleanup specfile for packaging
* Wed May 30 2012 - xxxx <xxxx@example.com> - 2.0.10
```

 