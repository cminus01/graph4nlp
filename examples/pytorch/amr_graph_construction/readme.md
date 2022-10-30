# Graph2Tree for math word problem (MWP) For AMR graph and RGCN

## Setup

### Install and set

install the amrlib and the fast_align, and set the environment variables as follows
```bash
export FABIN_DIR=path_to_fast_align
export TOKENIZERS_PARALLELISM=True
```

### Run with following

```python
python examples/pytorch/math_word_problem/mawps/src/runner.py
```

## Results (Solution accuracy for MAWPS)

| SAGE |undirected |  
| ---- | ---- |  
| Dynamic_node_emb | 76.4 |  
