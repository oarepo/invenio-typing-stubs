# `invenio-typing-stubs`

This is a package that provides typing support for the InvenioRDM
source base. It is intended as a temporary solution until InvenioRDM
itself provides typing support.

As such, it is a collection of type stubs for the InvenioRDM
source base, as well as some utility functions to help with typing.

It must not contain any runtime code, it is intended to be used
only for type checking.

## Warning

These stubs were generated mostly automatically and only some have been
manually checked. They will surely contain some errors. Please report any
issues you find.

## Usage

Please install the package directly from github:

```bash
pip install git+https://github.com/oarepo/invenio-typing-stubs.git
```

If you add the dependency to your `pyproject.toml` built with hatchling, do it like:

```toml
[project.optional-dependencies]
dev = [
    "invenio-typing-stubs @ git+https://github.com/oarepo/invenio-typing-stubs.git",
]
```

## How it was generated

### Initial sources

The types were initially generated using monkeytype:

```bash
A=<this_repo-root>
B=invenio_drafts_resources

cd <invenio_drafts_resources_root>
# install it
# uv pip install monkeytype
# replace run-tests.sh: monkeytype run -m pytest ...
# ./run-tests.sh
$A/generate_stubs_from_monkeytype.sh $B $A$/${B}-monkey
mv A/${B}-stub/${B}/* A/${B}-stubs/
```

Then stubgen was used as monkeytype does not cover all cases:

```bash
stubgen .venv/lib/python3.13/site-packages/${B} -o .
mv $B $B-stubs
```

### Automatic pre-process

Automatic pre-processing was done using Claude. Prompts:

#### Monkeytype cleanup

provided context: ${B}-monkey, .venv site-packages/${B}
  

```text
Let's have B=invenio_requests.

You are a python typing expert. In the ${B}-monkey directory, there are some type stubs
that were generated using monkeytype. These stubs are mostly correct, but
there are some issues that need to be fixed. Going systematically file by file, 
please fix the following issues:

1. If there are Any inside the types, please check with the source code that it really
   cannot be more specific. If it can be more specific, please change it to the
   correct type.

2. If there are types that clearly come from testing code (such as mocks or test-looking 
   classes, please remove them. In the places where
   type is used (for example, blah: SomeTestClass or () -> SomeTestClass), please replace 
   it with the correct type. If you are not sure what the correct type is, please use
   _typeshed.Incomplete instead of Any.

3. If there are complicated Union types, please simplify them if possible. For example,
   if there is Union[A, B, None], please change it to Optional[Union[A, B]]. Also, if they
   need similar types, simplify them even it is not strictly correct. For example, if there
    is Union[dict[str, A, B, C, D, E, F] | dict[str, G, H]], try to find the base class and 
    change it just to this. If unable, please change it to
    dict[str, Any].

4. Parent classes might be missing in the generated stubs. Please check the source code
   and add any missing parent classes. If you are not sure what the correct parent class is,
   please add a # TODO comment there.

5. For missing type stubs, do not replace them with Any or Incomplete,
   as we will define the stubs later. Just leave them as is. NEVER do
   "The error is about missing stubs for invenio_search.engine, but we can use Any for that."
```

provided context: ${B}-monkey, .venv site-packages/${B}
  

```text
Let's have B=invenio_requests.

You are a python typing expert. In the ${B}-monkey directory, some type stubs can be improved.
Going systematically file by file, please improve the following issues:

1. If you see Any to be used as a parameter type/return value type, 
   please check it with the source code. If they can be more
   specific, change them to the correct type.

2. If you find "record: Any" and you do not have a better type, 
   please change it to invenio_records_resources.records.api.Record.
```

provided context: ${B}-monkey, .venv site-packages/${B}
  

```text
Let's have B=invenio_requests.

You are a python typing expert. In the $B-monkey directory, there
are polished type stubs that were generated using monkeytype.

In the $B-stubs, there are the same files, but generated using
stubgen. 

Please systematically file by file, compare the two
versions and merge them together into the $B-stubs.
DO NOT optimize to pick just the most important files,
we need to go through all the files. Do not consider time
constraints, we need to be thorough. If we can not manage
to finish in one go, we can continue later.

In each file, do it field by field, preferring the $B-monkey 
version if it looks more complete. 
If there are any differences, please check the source
code to see which one is correct. If you are not sure, please
use the $B-stubs version. Immediately after a file has been merged,
remove the $B-monkey version of the file before proceeding to the 
next file. DO NOT remove any file that has not been explicitly merged.

For unknown/missing types, please use _typeshed.Incomplete instead of Any, we will deal with them later.
```

```text
Let's have B=invenio_records_resources.

You are a python typing expert whose task is to make sure that typing information
in stub files corresponds to the source code. Today you will be working on sources
from the InvenioRDM project. The codebase uses python 3.13, so that syntax is allowed
and preferred.

You are provided with two directories: ${B} which contains the source code and 
${B}-stubs which contains type stubs for the source code. Your task is to exhaustively
and methodically go through all files in the source code directory and check that
the typing information in the corresponding stub file is correct. If not, please
fix it.

To do so, follow these steps:

1. If there is no all_files.txt file in the ${B}-stubs directory, please create it
   and add all python files in the source code directory (${B}) to it, one per line. You
   will use this file to see which files are present in the source code directory.

2. If there is no file_list.txt file in the ${B}-stubs directory, please create it.
   This file will contain the list of files that have already been checked and NEVER
   must be checked again.

3. Systematically have a look at each file in the all_files.txt file that is NOT in
   file_list.txt, and compare it agains the corresponding file in the ${B}-stubs directory.:
   If there is no corresponding file in the ${B}-stubs directory, please extract typing 
   information from the source code and create a new stub file.

4. If there are any differences between the source code and the stub file, please
   fix the stub file to correspond to the source code.

During the process, please pay special attention to the following issues:

0. IMPORTANT: think hard about each file. Gather as much context as possible because
   sometimes the correct type is not obvious. NEVER count on mypy that passing it means
   that the stubs are correct. ALWAYS check the source code and think hard about it.
   NEVER do stuff in batches to save time, we need to be thorough.
   NEVER skip a file without inspecting the source!

a. Try to avoid using Any. If possible, always use more specific types. 
   NEVER use the "object" type. Also check the already generated code for Any
   and try to make it more specific if possible.

b. Words like "record", "request", "community" suggest that the type might be
   invenio_records_resources.records.api.Record, invenio_requests.records.api.Request,
   invenio_communities.communities.records.api.Community, respectively. Please check 
   the source code to confirm.

c. Please consult other -stubs files in the root directory of the project as they are
   part of the same project and might give you hints about the correct types and the
   typing conventions used in the project.

d. You might see lines containing python comments with "keep typing" or "ignore typing".
   These were hand crafted and you must NEVER change or remove these typings and comments.

e. Some imports might have missing type stubs. This is expected, do not try to fix them
   by using Any or _typeshed.Incomplete, just leave them as is. NEVER do
   from x import X
   X: Any

f. Add typing for class properties as well. Always do it with typing.ClassVar[Type].

g. For properties on class instances set within __init__ or other methods of the class,
   please add them to the class definition as well, with the correct type. If you are not
   sure what the correct type is, please use _typeshed.Incomplete instead of Any, we will 
   deal with them later. Add private properties as well (those starting with _).

h. If you see/generate complicated Union types, please simplify them if possible. For example,
   if there is Union[A, B, None], please change it to Optional[Union[A, B]]. Also, if they
   need similar types, simplify them even it is not strictly correct. For example, if there
    is Union[dict[str, A, B, C, D, E, F] | dict[str, G, H]], try to find the base class and 
    change it just to this. If unable, please change it to dict[str, Any].

i. Always use absolute imports in stubs, NEVER generate relative imports.

j. Do not add a method/property if it is already defined on a parent class.

k. Please also run `.venv/bin/mypy --check-untyped-defs --ignore-missing-imports --follow-imports=silent file.pyi`
   after each file to make sure that the stubs are ok.

l. It seems that some tools can not see reexported symbols in __init__.py if they are 
   correctly imported as from x import y as y. To work around this, please copy the
   __all__ list from the original module into the stub.

m. To add lines to file_list.txt, do not use bash & echo command, edit the file directly.

After you have processed a file, please add its name to file_list.txt,
so that we do not check it again.

If you need to run mypy or similar python programs, run them from venv,
that is .venv/bin/mypy .

For unknown/missing types, please use _typeshed.Incomplete instead of Any, we will 
deal with them later.
```

### Manual checks

Some manual checks were done to ensure the stubs are correct.

### Final checks

Checked with

```bash
mypy --check-untyped-defs --ignore-missing-imports invenio_records_resources-stubs/
```

