# gbs changelog

Use the `changelog` subcommand to generate a change log file in the `./packaging` directory. The command is mostly used for creating a change log before submitting code.

For command usage details, enter:

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
