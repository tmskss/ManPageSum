# ManPageSum

## Project description
Summarize linux man pages using a fine-tuned version of an AI model

## Usage
Prompt example:
```
summarize: ls
```
Output:
```
List directory contents. More information: https://www.gnu.org/software/coreutils/ls.

List files one per line:
ls -1

List all files, including hidden files:
ls -a

List all files, with trailing / added to directory names:
ls -F

Long format list (permissions, ownership, size, and modification date) of all files:
ls -la

Long format list with size displayed using human-readable units (KiB, MiB, GiB):
ls -lh

Long format list sorted by size (descending):
ls -lS

Long format list of all files, sorted by modification date (oldest first):
ls -ltr

Only list directories:
ls -d */
```

## Model
To Be Determined

## Training data
The model was trained on all the man pages available on [man7.org](https://man7.org).
The summarized texts were generated using the [TLDR GIthub repo](https://github.com/tldr-pages/tldr.git).
