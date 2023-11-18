# Installation
```
pip install d3rlpy==1.1.1

vim /anaconda/envs/dql/lib/python3.8/site-packages/pybullet_envs/__init__.py
change to:
  if id not in gym.envs.registry

git clone https://github.com/Lifelong-ML/CompoSuite.git
cd CompoSuite
pip install -r requirements_default.txt
pip install -e .

pip uninstall numba
pip install -U numba

python off_comp_rl/d3rl_runner.py --algo bc --dataset-type medium-replay-subsampled
python off_comp_rl/d3rl_runner.py --algo bc --dataset-type expert

# use pip install instead of conda, for the case of not compatible pytorch version for your machine
pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113

[info     ] Model parameters are saved to d3rlpy_default_bc_logs/IIWA_Box_None_Push_20231118035354/model_300000.pt

python off_comp_rl/d3rl_eval.py --algo bc --dataset-type medium-replay-subsampled --dataset-split single_task --model_path d3rlpy_default_bc_logs/IIWA_Box_None_Push_20231118035354/

```

# Robotic Manipulation Datasets for Offline Compositional Reinforcement Learning

This is the repository for our Robotic Manipulation Offline Compositional Reinforcement Learning Datasets and the corresponding code.
These datasets were collected using the [CompoSuite benchmark](https://github.com/Lifelong-ML/CompoSuite) which builds on top of [robosuite](https://github.com/ARISE-Initiative/robosuite) and uses the [Mujoco simulator](https://github.com/deepmind/mujoco). The datasets were collected in an effort to provide a large collection of offline reinforcement learning tasks for control that can be used to train multi-task offline reinforcement learning agents and provide a testbed to study compositional offline reinforcement learning algorithms.

The datasets are themselves are provided on [dryad](https://datadryad.org/stash) under the following link [https://datadryad.org/stash/dataset/doi:10.5061/dryad.9cnp5hqps](https://datadryad.org/stash/dataset/doi:10.5061/dryad.9cnp5hqps). Dryad is a non-profit publishing platform and community for open availability of research data. All data is hosted using a CC0 License to encourage open science.

## Training and Testing Task List

Since the tasks included in the benchmark are of varying difficulty, we provide several task lists that contain train-test splits of the set of tasks. These can be used to maintain a fixed set of tasks for experiment comparability. The splits come as uniform task sampling, compositional task sampling and restricted task sampling as described by the technical report. The lists are contained in the train_test_splits folder and contain 10 random split for each configuration. Of course, users are free to create their own splits as well if needed.

## Installation

    pip install -r requirements.txt

## Running the code

To reproduce our experiments, we provide a training and evaluation file for running d3rlpy with our datasets and network architecture. Before you start, make sure to correctly set the dataset and datasplit paths in both d3rl_runner.py and d3rl_eval.py. Note that, these paths expect a pointer to a folder that has the following structure.

├ root_data  
│   ├ expert  
│   │   ├ IIWA_Box_None_Push  
│   │   ├ ...  
│   ├ medium  
│   │   ├ ...  
│   ├ random  
│   │   ├ ...  
│   ├ medium-replay-subsampled  
│   │   ├ ...  

The data you can download on dryad is split by robot arm so you have to recreate the above folder structure by moving the different robot arm folders into a single folder.

To train a model, navigate to off_comp_rl and exectute

```python
python d3rl_runner.py --use-task-list-path
```

The following arguments can be used to execute specific training configurations.

    --dataset-split: The split list that you would like to use. Options are "default", "compositional", "holdout"
    --dataset-type: The difficulty of the dataset you would like to use. Options are "random", "medium", "expert", "medium-replay-subsampled"
    --data-seed: The random seed to set. If using data split lists, this needs to be a number from 0-9.
    --use-task-list-path: If this is not set, only a single task according to the robot, object, obstacle and objective args will be run
    --algo: The offline algorithm to use. Options are "bc" and "iql".
    --encoder: The policy encoder to use. Options are "default" or "compositional". "compositional" is currently only supported for algo="iql".

Once you have trained the model, you can evaluate it using

```python
python d3rl_eval.py --path <your_path>
```

again with the corresponding args set correctly as before.
