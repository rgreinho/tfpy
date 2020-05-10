# Detailed usage

**Usage**:

```console
$ tfpy [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `generate`: Generate Terraform stacks.
* `list`: List all the stacks and their environment(s).
* `regenerate`: Regenerate all stacks.

## `tfpy generate`

Generate Terraform stacks.

**Usage**:

```console
$ tfpy generate [OPTIONS] PROJECT
```

**Options**:

* `--environment TEXT`
* `-v, --verbose`
* `--help`: Show this message and exit.

## `tfpy list`

List all the stacks and their environment(s).

**Usage**:

```console
$ tfpy list [OPTIONS]
```

**Options**:

* `--detailed`
* `--help`: Show this message and exit.

## `tfpy regenerate`

Regenerate all stacks.

**Usage**:

```console
$ tfpy regenerate [OPTIONS]
```

**Options**:

* `-v, --verbose`
* `--help`: Show this message and exit.

