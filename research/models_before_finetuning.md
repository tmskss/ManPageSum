# This file summarizes the models' performances before finetuning.
### Models
I used the following pre-trained models for the experiments:
- [GPT-2 XL](https://huggingface.co/gpt2-xl)
- [Flan-T5 Base](https://huggingface.co/google/flan-t5-base)
- [BART Large](https://huggingface.co/facebook/bart-large)

### Datasets
I used the following dataset for the experiments:
- [linux-man-pages](https://huggingface.co/datasets/tmskss/linux-man-pages-tldr-summarized)

I used the first row (chgrp command) for the experiments. I created a baseline summary by concatenating the first 3 sentences of the description:
```
The chgrp utility shall set the group ID of the file named by each file operand
to the group ID specified by the group operand.
For each file operand, or, if the -R option is used, each file encountered while
walking the directory trees specified by the file operands, the chgrp utility
shall perform actions equivalent to the chown() function defined in the System
Interfaces volume of POSIX.1‐2017, called with the following arguments: * The
file operand shall be used as the path argument.
* The user ID of the file shall be used as the owner argument.
```

### Generated texts
- GPT-2 XL
```chgrp -R or -O -R -P chgrp -N or -O -N chgrp -H For the file operands specified
above, chmod shall use the same set of options as for the chgrp utility, except
that following execution of command, -H, the last file operand becomes
```
- Flan-T5 Base
```Set the group ID of the file named by each file operand.
Set the set-user-ID and set-group-ID bits of a regular file.
Confirm the implementation of the chgrp utility.
```

- BART Large
```The chgrp utility shall conform to the Base Definitions volume of POSIX.1‐2017,
Section 12.2, Utility Syntax Guidelines. For each file operand, or, if the -R
option is used, each file encountered while walking the directory trees
specified by the file operands, the chgrP utility shall perform actions
equivalent to the chown() function.
```

### Evaluation

I used ROUGE for evaluation of the models performance before finetuning.
These are the results:
| Model | ROUGE-1 | ROUGE-2 | ROUGE-L | ROUGE-Lsum |
| ------------ | ------------- | ------------- | ------------- | ------------- |
| baseline | 0.270270 | 0.010929 | 0.205405 | 0.237838 |
| flan-t5 | 0.250000 | 0.016949 | 0.216667 | 0.233333 |
| gpt2 | 0.244275 | 0.031008 | 0.167939 | 0.213740 |
| bart | 0.211268 | 0.000000 | 0.169014 | 0.211268 |


### Side note
The whole code used to conclude this experiment can be found in [this notebook](colab/ModelComparison.ipynb)




